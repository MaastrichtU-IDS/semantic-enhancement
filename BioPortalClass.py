import json
import requests
import pandas as pd
from pandas import DataFrame

#Class search using column names in BioPortal
#save results to files
#the code need to be run for each dataframe

df = DataFrame.from_csv('geneData\\genes.tsv', sep='\t') #pharmgkb
# df = DataFrame.from_csv('geneData\\hgnc_complete_subset.tsv', sep='\t') #hgnc
# df = DataFrame.from_csv('geneData\\CTD_chem_gene_ixns.tsv', sep='\t') #ctd
# df = pd.read_csv('geneData\\genage_human.csv') #
cols = df.columns.values
# print (json.dumps(parsed, indent=4, sort_keys=True))
vocab_list=[]
results_list=[]
list_dict=[]
count = 0
for col in cols:
    if "_" in col:
        col=col.replace("_"," ")
    parameters = {"q": col, "apikey": "d5e33918-f82b-43d7-9b13-8063c516550f",'require_exact_match':'true'}

    # print(col)
    response = requests.get("http://data.bioontology.org/search?", params=parameters)
    parsed = json.loads(response.content)

    vocab_list=[]
    for x in range(len(parsed["collection"])):
        if parsed["collection"][x]["@id"]:
            # print(parsed["collection"][x]["@id"])
            count+=1
            print(parsed["collection"][x]["@id"])
            if parsed["collection"][x]["@id"] not in results_list:
                results_list.append(parsed["collection"][x]["@id"])
            if parsed["collection"][x]["links"]["ontology"] not in vocab_list:
                vocab_list.append(parsed["collection"][x]["links"]["ontology"])
    # print(parsed["nextPage"])
    # print(parsed["pageCount"])

    while parsed["nextPage"]and parsed["nextPage"]<= parsed["pageCount"]:
        parameters = {"q": col, "apikey": "d5e33918-f82b-43d7-9b13-8063c516550f",'require_exact_match':'true'}
        # print(col)
        response = requests.get(parsed["links"]["nextPage"], params=parameters)
        parsed = json.loads(response.content)
        for x in range(len(parsed["collection"])):
            if parsed["collection"][x]["@id"]:
                # print(parsed["collection"][x]["@id"])
                count+=1
                if parsed["collection"][x]["@id"] not in results_list:
                    results_list.append(parsed["collection"][x]["@id"])
                # print(count)
                if parsed["collection"][x]["links"]["ontology"] not in vocab_list:
                    vocab_list.append(parsed["collection"][x]["links"]["ontology"])
    d = {'column_name': col, 'no_results(complete)': count, 'no_results(noduplicates)':len(results_list),'results':results_list, 'vocab_list': str(vocab_list)}
    vocab_list=[]
    results_list=[]
    count=0
    list_dict.append(d)
    d={}


# print(list_dict)
dfres = pd.DataFrame(list_dict)
# print(dfres)
# dfres.to_csv('BioPortalProperty\\results_genage_class.csv') #uncomment this line to save to a file.csv

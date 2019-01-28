import json
import requests
import pandas as pd
from pandas import DataFrame

#Property search using column names in BioPortal
#save results to files
#the code need to be run for each dataframe
#for the generic seacrch ont parameter should not be included, same for the require_exact_match':'true'
#ont is the list of ontologies for restriction for each dataset
3

# df = DataFrame.from_csv('geneData\\genes.tsv', sep='\t') #pharmgkb
# df = DataFrame.from_csv('geneData\\hgnc_complete_subset.tsv', sep='\t') #hgnc
df = DataFrame.from_csv('geneData\\CTD_chem_gene_ixns.tsv', sep='\t') #ctd
# df = pd.read_csv('genage_human.csv')#genage
cols = df.columns.values

vocab_list=[]
results_list=[]
list_dict=[]
count = 0
countd=0
proplab={}

ont="NIFSTD,ORTH" #ctd
# ont="ADALAB-META,ERO,SEDI,HORD" #genage
# ont="ORTH,ADALAB-META,NIFSTD"#pharmgkb record no of classes of properties for conlc of why it is the highest
# ont="HGNC,HUGO,PTS"
for col in cols:
    if "_" in col:
        col=col.replace("_"," ")

# parameters = {"q": col, "apikey": "d5e33918-f82b-43d7-9b13-8063c516550f","ontologies":ont,'require_exact_match':'true'} #use this version for ontology restriction
                                                                                                                           # and long match restriction
    parameters = {"q": col, "apikey": "d5e33918-f82b-43d7-9b13-8063c516550f","ontologies":ont} #use this version for ontology restriction
    #parameters = {"q": col, "apikey": "d5e33918-f82b-43d7-9b13-8063c516550f"} #use this for search with no restriction
    # print(col)
    response = requests.get("http://data.bioontology.org/property_search?", params=parameters)
    parsed = json.loads(response.content)
# print(response.url)
    vocab_list=[]
# print (json.dumps(parsed, indent=4, sort_keys=True))
    for x in range(len(parsed["collection"])):
        if parsed["collection"][x]["@id"]:
            # print(parsed["collection"][x]["@id"])
            count+=1
            if parsed["collection"][x]["@id"] not in results_list:
                results_list.append(parsed["collection"][x]["@id"])
                countd+=1
                print("prop" + parsed["collection"][x]["@id"])
                print("ont" + parsed["collection"][x]["links"]["ontology"])
                try:
                    if parsed["collection"][x]["label"]:
                        proplab[parsed["collection"][x]["@id"]]=parsed["collection"][x]["label"]
                except KeyError:
                    proplab[parsed["collection"][x]["@id"]]="none"
            else:
                print("propc"+parsed["collection"][x]["@id"])
                print("ontc"+parsed["collection"][x]["links"]["ontology"])
            if parsed["collection"][x]["links"]["ontology"] not in vocab_list:
                vocab_list.append(parsed["collection"][x]["links"]["ontology"])
    # print(parsed["nextPage"])
    # print(parsed["pageCount"])

    while parsed["nextPage"] and parsed["nextPage"]<= parsed["pageCount"]:
        # parameters = {"q": col, "apikey": "d5e33918-f82b-43d7-9b13-8063c516550f","ontologies":ont,'require_exact_match':'true'} #use this version for ontology restriction
        # and long match restriction
        parameters = {"q": col, "apikey": "d5e33918-f82b-43d7-9b13-8063c516550f","ontologies": ont}  # use this version for ontology restriction
        # parameters = {"q": col, "apikey": "d5e33918-f82b-43d7-9b13-8063c516550f"} #use this for search with no restriction
        # print(col)
        response = requests.get(parsed["links"]["nextPage"], params=parameters)
        parsed = json.loads(response.content)
        for x in range(len(parsed["collection"])):
            if parsed["collection"][x]["@id"]:
                # print(parsed["collection"][x]["@id"])
                count+=1
                if parsed["collection"][x]["@id"] not in results_list:
                    results_list.append(parsed["collection"][x]["@id"])
                    countd += 1
                    try:
                        if parsed["collection"][x]["label"]:
                            proplab[parsed["collection"][x]["@id"]] = parsed["collection"][x]["label"]
                    except KeyError:
                        proplab[parsed["collection"][x]["@id"]] = "none"
                else:
                    print("prop" + parsed["collection"][x]["@id"])
                    print("ont" + ["collection"][x]["links"]["ontology"])
                if parsed["collection"][x]["links"]["ontology"] not in vocab_list:
                    vocab_list.append(parsed["collection"][x]["links"]["ontology"])
    d = {'column_name': col, 'no_results(duplicates)': count, 'no_results(no duplicates)':countd,'results':results_list,'vocab_list': str(vocab_list)}
    list_dict.append(d)
    vocab_list=[]
    results_list=[]
    count=0
    countd=0
    d={}


# print(list_dict)
dfres = pd.DataFrame(list_dict)
dfres.append(list_dict)
# print(dfres)
# dfres.to_csv('results_pharmgkb_restricted_label.csv') #uncomment this line to save to a file.csv

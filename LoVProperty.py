import json
import requests
import pandas as pd
from pandas import DataFrame
#Search using column names in LOV
#save results to files
#the code need to be run for each dataframe
df = DataFrame.from_csv('geneData\\genes.tsv', sep='\t') #pharmgkb
# df = DataFrame.from_csv('geneData\\hgnc_complete_subset.tsv', sep='\t') #hgnc
# df = DataFrame.from_csv('geneData\\CTD_chem_gene_ixns.tsv', sep='\t') #ctd
# df = pd.read_csv('geneData\\genage_human.csv')
cols = df.columns.values

#(saved_column)
# dfres = pd.DataFrame(columns = ['column_name', 'results', 'no_results', 'vocab_list'])
vocab_list=[]
results_list=[]
list_dict=[]

for col in cols:
    # if "_" in col:
    #     col=col.replace("_"," ")
    parameters = {"q": col,"tag":"Biology","type":"property"}
    # print(col)
    # Make a get request with the parameters.
    response = requests.get("https://lov.linkeddata.es/dataset/lov/api/v2/term/search?",params=parameters)
    parsed = json.loads(response.content)
    # print(response.content)
    try:
        no_r=parsed["aggregations"]["tags"]["buckets"][0]["doc_count"]
    except IndexError:
        no_r=0
    # print("number"+str(no_r))
    for i in range(len(parsed["aggregations"]["vocabs"]["buckets"])):
        vocab_list.append(parsed["aggregations"]["vocabs"]["buckets"][i]["key"])
        # print(vocab_list)
    if no_r>10:
        page_nr=no_r
        j=0
        while page_nr>=10:
            j+=1
            parameters = {"q": "" + col + "", "tag": "Biology", "type": "property","page":str(j)}
            response = requests.get("https://lov.linkeddata.es/dataset/lov/api/v2/term/search?", params=parameters)
            parsed = json.loads(response.content)


            for x in range(len(parsed["results"])):
                results_list.append(parsed["results"][x]["uri"][0])
            # print("list"+str(len(results_list)))
            page_nr=page_nr-10

        if page_nr<10:
            j+=1
            # print(j)
            parameters = {"q": "" + col + "", "tag": "Biology", "type": "property", "page": str(j)}
            response = requests.get("https://lov.linkeddata.es/dataset/lov/api/v2/term/search?", params=parameters)
            parsed = json.loads(response.content)

            for x in range(len(parsed["results"])):
                results_list.append(parsed["results"][x]["uri"][0])

    else:
        # for i in range(len(parsed["aggregations"]["vocabs"]["buckets"])):
        #     vocab_list.append(parsed["aggregations"]["vocabs"]["buckets"][i]["key"])
        # # print(vocab_list)
        for x in range(len(parsed["results"])):
            results_list.append(parsed["results"][x]["uri"][0])
    # print(len(results_list))
    # print(no_r)
    d={'column_name':col, 'results':str(results_list),'no_results':no_r,'vocab_list':str(vocab_list)}
    results_list = []
    vocab_list = []
    # print(d)
    list_dict.append(d)
    # print(list_dict)
    d = {}


# print(list_dict)
dfres = pd.DataFrame(list_dict)
# dfres.append(list_dict)
print(dfres)
# dfres.to_csv('results_genage_bioportal.csv')

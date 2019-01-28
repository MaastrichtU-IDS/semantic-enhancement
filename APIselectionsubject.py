
import pandas as pd
from pandas import DataFrame
import warnings
import json
import requests

df = DataFrame.from_csv('geneData\\genes.tsv', sep='\t',index_col=None) #pharmgkb
# df = DataFrame.from_csv('geneData\\hgnc_complete_subset.tsv', sep='\t',index_col=None) #hgnc
# df = DataFrame.from_csv('geneData\\CTD_chem_gene_ixns.tsv', sep='\t',index_col=None) #ctd
# print(simple_aberowl_go_query(""))
cols=list(df)
print(cols)
vocab_list=[]
results_list=[]
list_dict=[]
count = 0
countd=0
proplab={}
# p = requests.post(url = 'http://nourishedcloud.com:9999/api/runQuery.groovy',
#                  data = json.dumps({ 'type': 'subeq', 'labels': 'true', 'query': query }))

g = requests.get('http://aber-owl.net/api/queryontologies/?query=gene')

ontologies=''
parsed = json.loads(g.content)
for x in range(len(parsed)):
    if (parsed[x]['ontology']) != "XPO":
        ontologies+=(parsed[x]['ontology'])+','

print (ontologies)

for col in cols:
    if "_" in col:
        col=col.replace("_"," ")
#     print(col)
    parameters = {"q": col, "apikey": "d5e33918-f82b-43d7-9b13-8063c516550f","ontologies":ontologies}
    # print(col)
    response = requests.get("http://data.bioontology.org/property_search?", params=parameters)
    parsed = json.loads(response.content)
    print(response.url)
    vocab_list=[]
    print (json.dumps(parsed, indent=4, sort_keys=True))
    for x in range(len(parsed["collection"])):
        if parsed["collection"][x]["@id"]:
            # print(parsed["collection"][x]["@id"])
            count+=1
            if parsed["collection"][x]["@id"] not in results_list:
                results_list.append(parsed["collection"][x]["@id"])
                countd+=1
                # print("prop" + parsed["collection"][x]["@id"])
                # print("ont" + parsed["collection"][x]["links"]["ontology"])
                try:
                    if parsed["collection"][x]["label"]:
                        proplab[parsed["collection"][x]["@id"]]=parsed["collection"][x]["label"]
                except KeyError:
                    proplab[parsed["collection"][x]["@id"]]="none"
            # else:
            #     print("propc"+parsed["collection"][x]["@id"])
            #     print("ontc"+parsed["collection"][x]["links"]["ontology"])
            if parsed["collection"][x]["links"]["ontology"] not in vocab_list:
                vocab_list.append(parsed["collection"][x]["links"]["ontology"])
    # print(parsed["nextPage"])
    # print(parsed["pageCount"])
#
    while parsed["nextPage"] and parsed["nextPage"]<= parsed["pageCount"]:
        parameters = {"q": col, "apikey": "d5e33918-f82b-43d7-9b13-8063c516550f", "ontologies": ontologies}
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
                # else:
                    # print("prop" + parsed["collection"][x]["@id"])
                    # print("ont" + ["collection"][x]["links"]["ontology"])
                if parsed["collection"][x]["links"]["ontology"] not in vocab_list:
                    vocab_list.append(parsed["collection"][x]["links"]["ontology"])
    d = {'column_name': col, 'no_results(duplicates)': count, 'no_results(no duplicates)':countd,'results':results_list,'vocab_list': str(vocab_list)}
    list_dict.append(d)
    vocab_list=[]
    results_list=[]
    # proplab={}
    count=0
    countd=0
# print(d)
# print(d)
# print(vocab_list)
# print(results_list)
#
#     # d={}
#
#
# # print(list_dict)
dfres = pd.DataFrame(list_dict)
dfres.append(list_dict)
print(dfres)
# dfres.to_csv('results_hgnc2_classification.csv')

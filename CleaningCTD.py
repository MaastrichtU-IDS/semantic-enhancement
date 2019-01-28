import json
import requests
import pandas as pd
from pandas import DataFrame
import numpy as np
# import csv
# reader = csv.reader(open(r"CTD_chem_gene_ixns.tsv"),delimiter=' ')
# filtered = filter(lambda p: 'Homo sapiens' == p[2], reader)
# csv.writer(open(r"ctd.csv",'w'),delimiter=' ').writerows(filtered)

#####used for cleaning CTD of rows with missing values-resulting file ctd3
#####and further filtering for HOMO SAPIENS rows ctd1
dfg = DataFrame.from_csv('geneData\\genes.tsv', sep='\t') #pharmgkb

df = DataFrame.from_csv('geneData\\ctd3.csv', sep=',',index_col=0) #ctd
symbol=[]
sh={}
sn={}
symbol=dfg['Symbol'].tolist()
hgnc_id=dfg['HGNC ID'].tolist()
ncbi_id=dfg['NCBI Gene ID'].tolist()
symbol_CTD=df['Gene Symbol'].tolist()
# print(symbol[0])
sublist_h=[]
sublist_n=[]
for i in range(len(symbol)):
    l=[]
    p=[]
    if symbol[i]=="":
        symbol[i]="Null"
    if symbol[i] == "":
        symbol[i] = "Null"
    l.append(symbol[i])
    p.append(symbol[i])
    l.append(hgnc_id[i])
    p.append(ncbi_id[i])

    sublist_h.append(l)
    sublist_n.append(p)

sh=dict(sublist_h)
print(sh)
# sn=dict(sublist_n)
hgnc_id_col=[]
# for x in symbol_CTD:
#     if x in sh.keys():
#         print(x)
#         print(sh[x])
#         hgnc_id_col.append(sh[x])
#     else:
#         hgnc_id_col.append("Null")
#
# se = pd.Series(hgnc_id_col)
#
# df['hgnc_id'] = se.values
# df.to_csv('geneData\\ctd3.csv')
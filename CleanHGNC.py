from pandas import DataFrame
import pandas as pd

# csv_table=pd.read_table('C:\\Users\\DELL\\PycharmProjects\\rdf-datatype-detection\\geneData\\hgnccomplete.tsv',sep='\t',encoding='ISO-8859-1')
# csv_table.to_csv('C:\\Users\\DELL\\PycharmProjects\\rdf-datatype-detection\\geneData\\hgnccom.csv',index=False)

dfH = DataFrame.from_csv('geneData\\hgnccom.csv',index_col=None) #hgnc
dfg = DataFrame.from_csv('geneData\\genes.tsv', sep='\t') #pharmgkb

#clean hgnc_id
#
# lhi=[]
# lhi=dfH['hgnc_id'].tolist()
# new_lhi=[]
#
# for x in lhi:
#     x=x.replace('HGNC:','')
#     new_lhi.append(x)
#
# print(new_lhi[0])
# se = pd.Series(new_lhi)
# dfH['hgnc_id_n'] = se.values
# dfH.to_csv('geneData\\hgnccom.csv')

#add ncbi id
#
# symbol=[]
# sh={}
# sn={}
# symbol=dfg['Symbol'].tolist()
# ncbi_id=dfg['NCBI Gene ID'].tolist()
# symbol_H=dfH['symbol'].tolist()
# # print(symbol[0])
#
# sublist_n=[]
# for i in range(len(symbol)):
#     p=[]
#     if symbol[i]=="":
#         symbol[i]="Null"
#     if symbol[i] == "":
#         symbol[i] = "Null"
#     p.append(symbol[i])
#     p.append(ncbi_id[i])
#     sublist_n.append(p)
#
# sh=dict(sublist_n)
# print(sh)
#count[]
# ncbi_id_col=[]
# for x in symbol_H:
#     if x in sh.keys():
#         print(x)
#         print(sh[x])
#         ncbi_id_col.append(sh[x])
#     else:
#         ncbi_id_col.append("Null")
#
# se = pd.Series(ncbi_id_col)
#
# dfH['ncbi_id'] = se.values
# dfH.to_csv('geneData\\hgnccom.csv')

#clean null rows

# dfH=dfH[dfH['ncbi_id'] != 'Null']
# dfH.to_csv('geneData\\hgnccom.csv')
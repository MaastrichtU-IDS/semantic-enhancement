from pandas import DataFrame
import math
#Collect HGNC Id from all datasets and write them into a new file




dfH = DataFrame.from_csv('geneData\\hgnccom.csv',index_col=None) #hgnc
dfg = DataFrame.from_csv('geneData\\genes.tsv', sep='\t') #pharmgkb
dfc = DataFrame.from_csv('geneData\\ctdHomoSapiens.csv',index_col=None)
columns=[]
entries=[]

hgnc_id = dfH['hgnc_id_n'].tolist()
hgnc_id_g=dfg['HGNC ID'].tolist()
hgnc_id_c=dfc['hgnc_id'].tolist()



# hgnc_id=[str(i) for i in hgnc_id]

# index_hgnc_id = {idx: el for el, idx in hgnc_id_index.items()}

#write hgnc id from ctd to file
# with open('newdatahgnc.csv','a') as file:
#     for id in hgnc_id_c:
#         file.write("hgnc_id_c,"+ str(id))
#         file.write('\n')



#clean file for nulll,nan values, write to new file
# df_hgnc=DataFrame.from_csv('newdatahgnc.csv',index_col=None,header=None)
# # print(df_hgnc[1])
# df_hgnc=df_hgnc[df_hgnc[1] != "Null"]
# df_hgnc2=df_hgnc[df_hgnc[1] != 'nan']
# df_hgnc2.to_csv('newdatahgnc2.csv',index=None,header=None)
df_hgnc=DataFrame.from_csv('newdatahgnc2.csv',index_col=None,header=None)
# df_hgnc=df_hgnc[df_hgnc[1] != math.nan]
# df_hgnc.to_csv('newdatahgnc2.csv',index=None,header=None)


id_h = df_hgnc[0].tolist()
id_h_2= df_hgnc[1].tolist()

# newh=[]
# newh2=[]
# for x in range(len(id_h_2)):
#     if math.isnan(id_h_2[x])==False:
#         # if id_h_2[x] not in newh2 and id_h[x] not in newh:
#             newh.append(id_h[x])
#             newh2.append(int(id_h_2[x]))
#     # else:
#     #     print(x)
# tupleid=list(zip(newh, newh2))
# newt=[]
#
# for x in tupleid:
#     if x not in newt:
#         newt.append(x)
#         # print(x)
# # print(newt)

# with open("tupleshgnc.txt","w") as f:
#     for line in newt:
#         strs=" ".join(str(x) for x in line)
#         f.write(strs+"\n")

# tuples=[]
# with open("tupleshgnc.txt","r") as file:
#         for line in file:
#             nline=line.split(" ")
#             nline[1]=nline[1].strip()
#             tuples.append(nline)
# # print(tuples)
#
#create unique list of hgnc_id
# uniq=[]
# for j in range(len(tuples)):
#     if int(tuples[j][1]) not in uniq:
#         uniq.append(int(tuples[j][1]))
# print(uniq)

#
# hgnc_id_index = {el: idx for idx, el in enumerate(uniq)}
# with open("columnMappingUniqueIndex\\hgncpairs.txt","w") as f:
#     for key, value in hgnc_id_index.items():
#         strs=str(key)+","+str(value)
#         f.write(strs+"\n")


#transform hgnc_id from different datasets into indexes
# for j in range(len(tuples)):
#     if tuples[j][0]=="hgnc_id":
#         tuples[j][0]=0
#     if tuples[j][0]=="HGNC_ID":
#         tuples[j][0]=1
#     if tuples[j][0]=="hgnc_id_c":
#         tuples[j][0]=2
#     tuples[j][1]=hgnc_id_index[int(tuples[j][1])]
#
# print(tuples[0])
# with open("tupleshgnctraining.txt","w") as f:
#     for line in tuples:
#         strs=" ".join(str(x) for x in line)
#         f.write(strs+"\n")
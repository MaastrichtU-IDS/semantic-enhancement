from pandas import DataFrame
from pyjarowinkler import distance

#extract name for training from all data
#newdata2 contains names from hgnc
#newdata3 contains names from pgkb
#newdata contains all names from both files
#tuplesnametraining1 contains training with names
dfH = DataFrame.from_csv('geneData\\hgnccom.csv',index_col=None) #hgnc
dfg = DataFrame.from_csv('geneData\\genes.tsv', sep='\t') #pharmgkb


name = dfH['name'].tolist()
name_g=dfg['Name'].tolist()
#
# name_c=[]
# name_g_c=[]
# # print(len(name))
# for i in name:
#     if i not in name_c:
#         name_c.append(i)
# # print(len(name_c))
# for j in name_g:
#     if j not in name_c:
#         name_g_c.append(j)
# print(len(name_g_c))

#previous version
# with open('FilesUsedToBuildtraining\\newdataname.txt','w') as file:
#     for name in name_c:
#         file.write("name|"+ name)
#         file.write('\n')
# with open('newdataname.txt','a') as file:
#     for name in name_g_c:
#         file.write("Name|"+ name)
#         file.write('\n')
##data is appended to newdataname.txt
# tuples=[]
# with open("FilesUsedToBuildtraining\\newdataname.txt","r") as file:
#         for line in file:
#             nline=line.split("|")
#             if len(nline)==3:
#                 print('aa')
#                 print(nline)
#             nline[1]=nline[1].strip()
#             tuples.append(nline)
# # print(tuples[20951])
#
# make unique list of names to have their indexes
# uniq=[]
# for k in range(len(tuples)):
#     if tuples[k][1] not in uniq:
#         uniq.append(tuples[k][1])
# print(len(uniq))
# print(len(tuples))
#
#
# name_index = {el: idx for idx, el in enumerate(uniq)}
# print(name_index["myosin light chain, phosphorylatable, fast skeletal muscle"])
# # # add indexs instead of Name,name ( so for each dataset a new index)
# for j in range(len(tuples)):
#     if tuples[j][0]=="name":
#         tuples[j][0]=0
#     if tuples[j][0]=="Name":
#         tuples[j][0]=1
#     tuples[j][1]=int(name_index[tuples[j][1]])
#     # print(tuples[j][1])
#
#
#
# print(tuples[10629])
# with open("tuplesnametraining.txt","w") as f:
#     for line in tuples:
#         strs=" ".join(str(x) for x in line)
#         f.write(strs+"\n")

#current version
categories=[]
with open("categories.txt", "r") as file:
        for line in file:
            line=line.replace(" ",'')
            nline=line.strip()
            categories.append(nline)
# print(categories)
#make unique list of names to have their indexes (unique list is from categories)
name_index = {el: idx for idx, el in enumerate(categories)}
# print(name_index["GTP-bindingprotein10(putative)"])
# print(len(name_index))
for key,value in name_index.items():
    name_index[key]=value+61912

with open("columnMappingUniqueIndex\\namepairs.txt","w") as f:
    for key, value in name_index.items():
        strs=str(key)+"|"+str(value)
        f.write(strs+"\n")

# new_n=[]

# for j in name_g:
#     max=distance.get_jaro_distance(j, categories[1], winkler=True, scaling=0.1)
#     for i in categories:
#         dist=distance.get_jaro_distance(j, i, winkler=True, scaling=0.1)
#         if dist>max:
#             max=dist
#             new=i
#     new_n.append(new)
#
# with open('FilesUsedToBuildtraining\\newdatasname3.txt','w') as file:
#     for name in new_n:
#         file.write("Name|"+ name)
#         file.write('\n')
# name 6
# Name 7
tuples=[]
with open("FilesUsedToBuildtraining\\newdatasname3.txt","r") as file:
        for line in file:
                if "Name" in line:
                    nline = line.split("|")
                    # print(nline)
                    # if len(nline) == 3:
                    #     print('aa')
                    #     print(nline)
                    nline[1] = nline[1].strip()
                    tuples.append(nline)

uniq=[]
for m in range(len(tuples)):
    if tuples[m][1] not in uniq:
        uniq.append(tuples[m][1])
# print(len(uniq))
# print(len(tuples))

#
# with open('tuplesnametraining1.txt.txt','a') as file:
#     for name in uniq:
#         n=name_index[name]
#         file.write("7 "+ str(n))
#         file.write('\n')
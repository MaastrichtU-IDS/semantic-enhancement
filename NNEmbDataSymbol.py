from pandas import DataFrame
import csv
#extract symbol for training from all data
#newdatasymbol contains all names from both files
#tuplessymboltraining contains training with symbols
#symbolpairs contains each unique symbol with computed id
dfH = DataFrame.from_csv('geneData\\hgnccom.csv',index_col=None) #hgnc
dfg = DataFrame.from_csv('geneData\\genes.tsv', sep='\t') #pharmgkb
dfc = DataFrame.from_csv('geneData\\ctdHomoSapiens.csv',index_col=None)

symbol= dfH['symbol'].tolist()
symbol_g=dfg['Symbol'].tolist()
symbol_c=dfc['Gene Symbol'].tolist()

symbol_co= []
symbol_g_c=[]
symbol_c_c=[]

for i in symbol:
    if i not in symbol_co:
        symbol_co.append(i)
# print(len(name_c))
for j in symbol_g:
    if j not in symbol_g_c:
        symbol_g_c.append(j)
for k in symbol_c:
    if k not in symbol_c_c:
        symbol_c_c.append(k)


# with open('FilesUsedToBuildtraining\\newdatasymbol.txt','w') as file:
#     for name in symbol_co:
#         file.write("symbol|"+ name)
#         file.write('\n')
# with open('FilesUsedToBuildtraining\\newdatasymbol.txt','a') as file:
#     for name in symbol_g_c:
#         file.write("Symbol|"+ str(name))
#         file.write('\n')
# with open('FilesUsedToBuildtraining\\newdatasymbol.txt','a') as file:
#     for name in symbol_c_c:
#         file.write("Gene Symbol|"+ str(name))
#         file.write('\n')
tuples=[]
with open("FilesUsedToBuildtraining\\newdatasymbol.txt","r") as file:
        for line in file:
            nline=line.split("|")
            if len(nline)==3:
                print('aa')
                print(nline)
            nline[1]=nline[1].strip()
            tuples.append(nline)
# print(tuples[20951])

#unique list for indexes
uniq=[]
for m in range(len(tuples)):
    if tuples[m][1] not in uniq:
        uniq.append(tuples[m][1])
print(len(uniq))
# print(len(tuples))


symbol_index = {el: idx for idx, el in enumerate(uniq)}
#add 28954
for key,value in symbol_index.items():
    symbol_index[key]=value+28954

with open("columnMappingUniqueIndex\\symbolpairs.txt","w") as f:
    for key, value in symbol_index.items():
        strs=str(key)+","+str(value)
        f.write(strs+"\n")

print(len(symbol_index))
print(symbol_index["A1BG"])

# #
# for j in range(len(tuples)):
#     if tuples[j][0]=="symbol":
#         tuples[j][0]=3
#     if tuples[j][0]=="Symbol":
#         tuples[j][0]=4
#     if tuples[j][0]=="Gene Symbol":
#         tuples[j][0]=5
#     tuples[j][1]=int(symbol_index[tuples[j][1]])+
#     # print(tuples[j][1])
#
#
#
# # print(tuples[10629])
# with open("tuplessymboltraining.txt","w") as f:
#     for line in tuples:
#         strs=" ".join(str(x) for x in line)
#         f.write(strs+"\n")

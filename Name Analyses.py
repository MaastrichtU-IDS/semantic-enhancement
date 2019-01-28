from pandas import DataFrame
from nltk.tokenize import word_tokenize
from collections import Counter
from pyjarowinkler import distance

#creates name categories so that similar names will have the same index
#saves categories to categories.txt

dfH = DataFrame.from_csv('geneData\\hgnccom.csv',index_col=None) #hgnc
dfg = DataFrame.from_csv('geneData\\genes.tsv', sep='\t') #pharmgkb
nameH=dfH['name'].tolist()
nameG=dfg['Name'].tolist()


# print(distance.get_jaro_distance(nameH[48], nameH[49], winkler=True, scaling=0.1))
# print(nameH[48])
# print(nameH[49])

categories=[]
lis=[[]]
flag=False

for j in range(len(nameH)):
    flag = any(distance.get_jaro_distance(nameH[j], category, winkler=True, scaling=0.1) > 0.7 for category in categories)
    if flag==False:
        categories.append(nameH[j])
        # print(nameH[j])

print(len(categories))
for k in range(len(nameG)):
    flag = any(distance.get_jaro_distance(nameG[k], category, winkler=True, scaling=0.1) > 0.7 for category in categories)
    if flag==False:
        categories.append(nameG[k])
        # print(nameG[k])
print(len(categories))

name_index = {el: idx for idx, el in enumerate(categories)}
with open("categories.txt","w") as f:
    for line in name_index:
        strs=" ".join(str(x) for x in line)
        f.write(strs+"\n")

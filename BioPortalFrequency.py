import numpy as np
import pandas as pd
from collections import Counter
import ast
import matplotlib.pyplot as plt
import  matplotlib
from numpy import *
# data = loadtxt('data.txt',dtype=int,usecols=(4,)) #loading 5th column of csv file into array named data.
#creates frequency graph distribution for each data file and save it with savefig
#needs to be run for each file
#for top ontology distribution restrict the frequncy with val


df = pd.read_csv('BioPortalProperty\\results_ctd_bioportal.csv')
cols = df.columns.values

# print(df['vocab_list'])
# print(Counter(df['vocab_list']))
full_list=[]
font = {'family' : 'normal',
        'size'   : 5}

matplotlib.rc('font', **font)
for index, row in df.iterrows():
   # print (type(row['vocab_list']))
   list = ast.literal_eval(row['vocab_list'])
   full_list.extend(list)
   # print(list)
# print(full_list)
full_list_new=[]
for x in full_list:
    x=x.replace('http://data.bioontology.org/ontologies/','')
    x=x.replace('http://da1ta.bioontology.org/ontologies/','')
    full_list_new.append(x)
print(full_list_new)
print(Counter(full_list))
dict=Counter(full_list_new)
print(dict)
myDict = {key:val for key, val in dict.items() if val>8}
# print(len(myDict))
# print(len(dict))
print(myDict)

plt.bar(myDict.keys(), myDict.values(), width=0.3, color='g')

plt.show()
# plt.tight_layout()

# plt.savefig("FrequencyDistributions\\genage_frequency_8.png") #uncomment this to save the plot to a file

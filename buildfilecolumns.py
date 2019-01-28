from nltk.corpus import wordnet as wn
import random
from random import randrange

#the 5 heuristic steps for creating more names
#each step needs to be run separately, will be saved to file

with open('col_fileorg.txt') as f:
    lines = f.read().splitlines()

print(lines)

#ALL CAPS
cap=[]
for x in lines:
    x=x.upper()
    cap.append(x)
# print(cap)
# with open('col_file.txt', 'w') as f:
#         for item in cap:
#             f.write("%s\n" % item)

# #############################
#
# # #LOWER CASE
low=[]
for x in lines:
    x=x.lower()
    low.append(x)
print(low)
# with open('col_file.txt', 'a') as f:
#         for item in low:
#             f.write("%s\n" % item)

# #REPLACE SPACE WITH UNDERSCORE
#
underscore=[]
for x in lines:
    if " " in x:
        x =x.replace(" ","_")
        underscore.append(x)
print(underscore)
underscorel=[]
underscorec=[]
for x in low:
    if " " in x:
        x =x.replace(" ","_")
        underscorel.append(x)
for x in cap:
    if " " in x:
        x =x.replace(" ","_")
        underscorec.append(x)
print(underscorec)



##REPLACE UNDERSCORE WITH DOT

newl=[]
dotl=[]
newl=underscorec+underscorel
for x in newl:
    x=x.replace("_",".")
    dotl.append(x)
print(dotl)
total=[]
total=cap+low+underscore+underscorel+underscorec
with open('col_file.txt', 'a') as f:
        for item in total:
            f.write("%s\n" % item)


##SPLIT TERMS AND THEN APPEND RANDOM THE PARTS OBTAINED
newl=[]
for l in lines:
    if " " in l:
        nl=l.split(" ")
        for x in nl:
            newl.append(x)
    elif "." in l:
        nl=l.split(".")
        for x in nl:
            newl.append(x)
    elif "_" in l:
        nl=l.split("_")
        for x in nl:
            newl.append(x)
    else:
        newl.append(l)
conc=[]
for name in newl:
    rand=random.randint(0, len(newl)-1)
    conc.append(name+newl[rand])
with open('col_file.txt', 'a') as f:
        for item in conc:
            f.write("%s\n" % item)
print(conc)
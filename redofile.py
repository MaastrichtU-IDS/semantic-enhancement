# First file is hgnc so get max of this file to add to the next category( which is symbol)
# listt=[]
# with open("tupleshgnctraining.txt", "r") as file:
#     for line in file:
#         nline = line.split(" ")
#         nline[1] = nline[1].strip()
#         listt.append(nline)
#
# max=0
#
# for x in range(len(listt)):
#     listt[x][1]=int(listt[x][1])
#     if listt[x][1]>max:
#         max=listt[x][1]
#
# print(max)#28954

################################################################symbolredo
# tuples=[]
# with open("newdatasymbol.txt","r") as file:
#         for line in file:
#             nline=line.split("|")
#             if len(nline)==3:
#                 print('aa')
#                 print(nline)
#             nline[1]=nline[1].strip()
#             tuples.append(nline)
# print(tuples[20951])

# uniq=[]
# for m in range(len(tuples)):
#     if tuples[m][1] not in uniq:
#         uniq.append(tuples[m][1])
# print(len(uniq))
# # print(len(tuples))
#
#
# symbol_index = {el: idx for idx, el in enumerate(uniq)}
# print(len(symbol_index))
# print(symbol_index["A1BG"])
# #
# for j in range(len(tuples)):
#     if tuples[j][0]=="symbol":
#         tuples[j][0]=3
#     if tuples[j][0]=="Symbol":
#         tuples[j][0]=4
#     if tuples[j][0]=="Gene Symbol":
#         tuples[j][0]=5
#     tuples[j][1]=int(symbol_index[tuples[j][1]])+max
#     # print(tuples[j][1])
# # print(tuples[10629])
# with open("training\\pos2\\tuplessymboltrainingnew.txt","w") as f:
#     for line in tuples:
#         strs=" ".join(str(x) for x in line)
#         f.write(strs+"\n")
#
#
#
#
# listt=[]
# with open("training\\pos2\\tuplessymboltrainingnew.txt", "r") as file:
#     for line in file:
#         nline = line.split(" ")
#         nline[1] = nline[1].strip()
#         listt.append(nline)
#
# max=0
#
# for x in range(len(listt)):
#     listt[x][1]=int(listt[x][1])
#     if listt[x][1]>max:
#         max=listt[x][1]
#
# print(max)#61912

##########################################################redoname
# list2=[]
# with open("training\\pos\\tuplesnametraining1.txt", "r") as file:
#     for line in file:
#         nline = line.split(" ")
#         nline[1] = nline[1].strip()
#         list2.append(nline)
#
#
#
# for x in range(len(list2)):
#     list2[x][1]=int(list2[x][1])+max
#
#
# with open("training\\pos2\\tuplesnametrainingnew.txt","w") as f:
#     for line in list2:
#         strs=" ".join(str(x) for x in line)
#         f.write(strs+"\n")

########################################################redo datagene neg
# listt=[]
# with open("training\\pos2\\tuplesnametrainingnew.txt", "r") as file:
#     for line in file:
#         nline = line.split(" ")
#         nline[1] = nline[1].strip()
#         listt.append(nline)
#
# max=0
#
# for x in range(len(listt)):
#     listt[x][1]=int(listt[x][1])
#     if listt[x][1]>max:
#         max=listt[x][1]
#
# print(max)#63098
# list2=[]
# with open("training\\neg\\negativedatagene.txt", "r") as file:
#     for line in file:
#         nline = line.split(" ")
#         nline[1] = nline[1].strip()
#         list2.append(nline)
#
# max2=0
#
# for x in range(len(list2)):
#     if list2[x][0]=="8":
#         list2[x][1]=int(list2[x][1])+max
#
# for x in range(len(list2)):
#     if list2[x][0]=="8":
#         if int(list2[x][1])>max2:
#             max2=int(list2[x][1])
#
# for x in range(len(list2)):
#     if list2[x][0]!="8":
#         list2[x][1] = int(list2[x][1]) + max2
# print(max2) #63123
#
# with open("training\\neg2\\negativedatagenenew.txt","w") as f:
#     for line in list2:
#         strs=" ".join(str(x) for x in line)
#         f.write(strs+"\n")
#
# max3=0
# for x in range(len(list2)):
#     if list2[x][0]!="8":
#         if int(list2[x][1])>max3:
#             max3=int(list2[x][1])
# print(max3)#161874
########################################################redo hgnc date
# list2=[]
# with open("training\\neg\\negativedatahgnc.txt", "r") as file:
#     for line in file:
#         nline = line.split(" ")
#         nline[1] = nline[1].strip()
#         list2.append(nline)
#
#
# max=161874
# for x in range(len(list2)):
#     list2[x][1]=int(list2[x][1])+max
#
# max_new=0
# for x in range(len(list2)):
#     if int(list2[x][1])>max_new:
#         max_new=int(list2[x][1])
# print(max_new) #165412
# with open("training\\neg2\\negativedatahgnc.txt","w") as f:
#     for line in list2:
#         strs=" ".join(str(x) for x in line)
#         f.write(strs+"\n")
########################################################redo hgnc loc
list2=[]
with open("training\\neg\\negativedatahgncloc.txt", "r") as file:
    for line in file:
        nline = line.split(" ")
        nline[1] = nline[1].strip()
        list2.append(nline)


max=165412
for x in range(len(list2)):
    list2[x][1]=int(list2[x][1])+max
max_new=0
for x in range(len(list2)):
    if int(list2[x][1])>max_new:
        max_new=int(list2[x][1])
print(max_new)#167250
# with open("training\\neg2\\negativedatahgnclocnew.txt","w") as f:
#     for line in list2:
#         strs=" ".join(str(x) for x in line)
#         f.write(strs+"\n")

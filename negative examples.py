from pandas import DataFrame
import math



dfH = DataFrame.from_csv('geneData\\hgnccom.csv',index_col=None) #hgnc
dfg = DataFrame.from_csv('geneData\\genes.tsv', sep='\t',index_col=None) #pharmgkb
#for first approach the numbers from unique sum need to be eliminated
############################## loc from HGNC file

d1_l = dfH['location'].tolist()
d2_l=dfH['location_sortable'].tolist()
d1_lc =[]
d2_lc=[]
for i in d1_l:
    if i not in d1_lc:
        d1_lc.append(i)
for j in d2_l :
    if j not in d2_lc:
        d2_lc.append(j)
uniq=[]

for x in d1_lc:
    if x not in uniq:
        uniq.append(x)
for y in d2_lc:
    if y not in uniq:
        uniq.append(y)

# print(len(uniq))
# print(len(d1_lc))
# print(len(d2_lc))
uniq_index={el: idx for idx, el in enumerate(uniq)}
for key,value in uniq_index.items():
    uniq_index[key]=value+165412
with open("training\\neg2\\hgnclocpairs.txt","a") as f:
    for key, value in uniq_index.items():
        strs=str(key)+","+str(value)
        f.write(strs+"\n")
# print(len(uniq_index))
# with open('training\\neg\\negativedatahgncloc.txt','w') as file:
#     for name in d1_lc:
#         ind=uniq_index[name]
#         file.write("13 "+ str(ind))
#         file.write('\n')
#     for name in d2_lc:
#         ind = uniq_index[name]
#         file.write("14 "+ str(ind))
#         file.write('\n')

######################################## date from HGNC

# d1_h = dfH['date_approved_reserved'].tolist()
# d2_h=dfH['date_modified'].tolist()
# d1_hc=[]
# d2_hc=[]
#
# uniq=[]
# for i in d1_h:
#     if i not in d1_hc:
#         d1_hc.append(i)
# for j in d2_h :
#     if j not in d2_hc:
#         d2_hc.append(j)
#
# for x in d1_hc:
#     if x not in uniq:
#         uniq.append(x)
# for y in d2_hc:
#     if y not in uniq:
#         uniq.append(y)
# #
# # print(len(uniq))
# # print(len(d2_hc))
# # print(len(d1_hc))
# uniq_index={el: idx for idx, el in enumerate(uniq)} #161874
#
# for key,value in uniq_index.items():
#     uniq_index[key]=value
# ##+161874
# with open("training\\neg2\\hgncdatepairs.txt","a") as f:
#     for key, value in uniq_index.items():
#         strs=str(key)+","+str(value)
#         f.write(strs+"\n")
# print(len(uniq_index))
#
# with open('training\\neg\\negativedatahgnc.txt','w') as file:
#     for name in d1_hc:
#         ind=uniq_index[name]
#         file.write("11 "+ str(ind))
#         file.write('\n')
#     for name in d2_hc:
#         ind = uniq_index[name]
#         file.write("12 "+ str(ind))
#         file.write('\n')



######################## chromosome from PGKB

# ch1_g = dfg['Chromosome'].tolist()
# ch2_g = dfg['Chromosomal Start - GRCh37.p13'].tolist()
# ch3_g =dfg['Chromosomal Stop - GRCh37.p13'].tolist()
# ch4_g = dfg['Chromosomal Start - GRCh38.p7'].tolist()
# ch5_g =dfg['Chromosomal Stop - GRCh38.p7'].tolist()
# ch1_gc=[]
# ch2_gc=[]
# ch3_gc=[]
# ch4_gc=[]
# ch5_gc=[]
# #
# for i in ch1_g:
#     if i not in ch1_gc:
#         ch1_gc.append(i)
# for j in ch2_g :
#     if j not in ch2_gc and math.isnan(j) == False:
#         ch2_gc.append(j)
# for x in ch3_g:
#     if x not in ch3_gc and math.isnan(x) == False:
#         ch3_gc.append(x)
# for q in ch4_g :
#     if q not in ch4_gc and math.isnan(q) == False:
#         ch4_gc.append(q)
# for w in ch5_g:
#     if w not in ch5_gc and math.isnan(w) == False:
#         ch5_gc.append(w)
# uniq=[]
#
# #
# for k in ch2_gc:
#     if k not in uniq:
#         uniq.append(k)
# for n in ch3_gc:
#     if n not in uniq:
#         uniq.append(n)
# for m in ch4_gc:
#     if m not in uniq:
#         uniq.append(m)
# for t in ch5_gc:
#     if t not in uniq:
#         uniq.append(t)
# #
# ch1_index = {el: idx for idx, el in enumerate(ch1_gc)}
# # for key,value in ch1_index.items():
# #     ch1_index[key]=value
# ###+63098
# # with open("training\\neg2\\genepairs.txt","w") as f:
# #     for key, value in ch1_index.items():
# #         strs=str(key)+","+str(value)
# #         f.write(strs+"\n")
#
# ch_index = {el: idx for idx, el in enumerate(uniq)} #63123
#
# for key,value in ch_index.items():
#     ch_index[key]=value
# ##+63123
# with open("genepairs.txt","a") as f:
#     for key, value in ch_index.items():
#         strs=str(key)+","+str(value)
#         f.write(strs+"\n")
# print(len(ch1_index))
# print(len(ch_index))

# # print(uniq)
# # print(ch_index[58858172.0])
#
#
#
# with open('training\\neg\\negativedatagene.txt','w') as file:
#     for name in ch1_gc:
#         ind=ch1_index[name]
#         file.write("8 "+ str(ind))
#         file.write('\n')
#     for name in ch2_gc:
#         ind = ch_index[name]
#         file.write("9 "+ str(ind))
#         file.write('\n')
#     for name in ch3_gc:
#         ind = ch_index[name]
#         file.write("10 "+ str(ind))
#         file.write('\n')
#     for name in ch4_gc:
#         ind = ch_index[name]
#         file.write("15 "+ str(ind))
#         file.write('\n')
#     for name in ch5_gc:
#         ind = ch_index[name]
#         file.write("16 "+ str(ind))
#         file.write('\n')

######################## pgkbid
#this is not in the file yet
# pgkb = dfg['PharmGKB Accession Id'].tolist()
# pgkb_c=[]
#
# for i in pgkb:
#     if i not in pgkb_c:
#         pgkb_c.append(i)
#
#
# print(len(pgkb_index))
#
# with open('training\\neg\\negativedatagene.txt','a') as file:
#     for name in pgkb_c:
#         ind=pgkb_index[name]
#         file.write("17 "+ str(ind))
#         file.write('\n')



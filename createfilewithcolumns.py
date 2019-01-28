# #
import pandas
from pandas import DataFrame
import pandas as pd


#extract all column names and store them in col_file.txt (do it separetly for each file)
# df = DataFrame.from_csv('geneData\\genes.tsv', sep='\t',index_col=None) #pharmgkb
# df = pandas.DataFrame.from_csv('geneData\\hgnc_complete_subset.tsv', sep='\t', index_col=None) #hgnc
# df = DataFrame.from_csv('geneData\\CTD_chem_gene_ixns.tsv', sep='\t',index_col=None) #ctd
# df = pd.read_csv('geneData\\genage_human.csv',index_col=None)
# cols = df.columns.values
# print(cols)
# column_list=[]
# for x in cols:
#     column_list.append(x)
# print(column_list)
# with open('col_fileorg.txt','a') as f: #after first df change w(write) to a (append)
#     for item in column_list:
#         f.write("%s\n" % item)



#generate more names using a neural network


##RNN Training
from textgenrnn import textgenrnn
from keras.models import load_model

# textgen = textgenrnn()
# textgen.train_from_file('col_file.txt', num_epochs=500)
# textgen.save('RNNModels\\text5_attempt2.h5')

#
# ##RNN generating new names from trained and saved model
textgen=textgenrnn('RNNModels\\text5_attempt2.h5')
text=textgen.generate(1000,return_as_list=True)

with open('RNNfiles\\col_filen51000.txt', 'w') as f:
    for item in text:
        f.write("%s\n" % item)
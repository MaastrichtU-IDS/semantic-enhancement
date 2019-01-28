from pandas import DataFrame
import pandas as pd

dfH = DataFrame.from_csv('C:\\Users\\DELL\\PycharmProjects\\rdf-datatype-detection\\geneData\\hgnccomWithoutNull.csv',index_col=None) #hgnc
dfg = DataFrame.from_csv('C:\\Users\\DELL\\PycharmProjects\\rdf-datatype-detection\\geneData\\genes.tsv', sep='\t') #pharmgkb
dfC3 = DataFrame.from_csv('ctd3.csv', sep=',',index_col=0) #ctd
dfC1 = DataFrame.from_csv('ctd1.csv', sep=',',index_col=0) #ctd


#create new data file
# new_df=DataFrame()
# #hgnc_id
# Hhi=dfH['hgnc_id_n'].tolist()
# Ghi=dfg['HGNC ID'].tolist()
# Chi3=dfC3['hgnc_id'].tolist()
# Chi1=dfC1['hgnc_id'].tolist()
# newchi=Hhi+Ghi+Chi1+Chi3
#
# se1 = pd.Series(newchi)
# #
# new_df['hgnc_id'] = se1.values
# # dfH.to_csv('C:\\Users\\DELL\\PycharmProjects\\rdf-datatype-detection\\geneData\\hgnccom.csv')
#
# #ncbi_id
# Hni=dfH['ncbi_id'].tolist()
# Gni=dfg['NCBI Gene ID'].tolist()
# Cni3=dfC3['Gene ID'].tolist()
# Cni1=dfC1['Gene ID'].tolist()
# newcni=Hni+Gni+Cni1+Cni3
# se2 = pd.Series(newcni)
# #
# new_df['ncbi_id'] = se2.values
# # dfH.to_csv('C:\\Users\\DELL\\PycharmProjects\\rdf-datatype-detection\\geneData\\hgnccom.csv')
#
#
# #symbol
# Hs=dfH['symbol'].tolist()
# Gs=dfg['Symbol'].tolist()
# Cs3=dfC3['Gene Symbol'].tolist()
# Cs1=dfC1['Gene Symbol'].tolist()
# newcs=Hs+Gs+Cs1+Cs3
# se3 = pd.Series(newcs)
# #
# new_df['symbol'] = se3.values
# # dfH.to_csv('C:\\Users\\DELL\\PycharmProjects\\rdf-datatype-detection\\geneData\\hgnccom.csv')
#
# new_df.to_csv('datacomplete.csv')
df = DataFrame.from_csv('datacomplete.csv', sep=',',index_col=0) #ctd
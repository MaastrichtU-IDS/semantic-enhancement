# semantic-enhancement
Folder structure:
ANNModel - contains variations of the trained Artificial Neural Network for binary classification of the Gene concept using column names
BioPortalClassLM- contains csv files for each dataset with results from using The BioPortal API for class search with parameter require_exact_match={true}

BioPortalProperty -contains csv files for each dataset with results from using The BioPortal API for property search with no parameter restrictions
BioPortalPropertyOntologyRestricted- contains 3 types of csv files (for each dataset):(i)results from using The BioPortal API for property search with restriction of parameter ontology_list={ontology1,ontology2,..,}(results_dataset_restricted.csv ),(ii)results from using The BioPortal API for property search with restriction of parameter ontology_list={ontology1,ontology2,..,} and require_exact_match={true}(results_dataset_restricted_long.csv), (iii) files with categorized matches for the second option(datasetmatched.xslx)
FilesUsedToBuildtraining-contains files that were created in the process of writing complete training files for the Neural Network Embedding Model
FrequnecyDistributions-contains graphs for complete and restricted ontology frequecy distributions for each dataset(the used threshold for each dataset is in the file name)
MatchClassification

                                                

from keras.models import load_model
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from keras import models
from keras import layers
from sklearn.metrics import classification_report, confusion_matrix
df1=pd.read_csv('RNNfiles\\colfile1074.csv',header=None)
df2=pd.read_csv('RNNfiles\\colfile2.csv',encoding = "ISO-8859-1",header=None)
df3=pd.read_csv('RNNfiles\\colfile3.csv',header=None)
df4=pd.read_csv('RNNfiles\\colfile4.csv',header=None)
df5=pd.read_csv('RNNfiles\\colfile5.csv',header=None)

namelist = df1[0].tolist()+df2[0].tolist()+df3[0].tolist()+df4[0].tolist()+df5[0].tolist()
# namelist = df1[0].tolist()+df2[0].tolist()+df3[0].tolist()+df4[0].tolist()
maxsize=len(max(namelist, key=len)) #chromOsomaL Start - gRCRoss-referencEs

classlist = df1[1].tolist()+df2[1].tolist()+df3[1].tolist()+df4[1].tolist()+df5[1].tolist()
# print(len(namelist))
number_matrix=[]
listperword=[] #vector for a word

for x in namelist:
    for i in x:
        listperword.append(ord(i))# add ASCII code
    while len(listperword)<maxsize:
        listperword.append(0)
    number_matrix.append(listperword)
    listperword=[]
# print(len(number_matrix))#vectorematrix
# print(classlist.count(1))
# print(classlist.count(0))
X=np.asarray(number_matrix)
Y=np.asarray(classlist)

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.33, random_state=42) #build train/test set
print(X_train.shape)

#build ANNN
model = models.Sequential()
# Input - Layer
model.add(layers.Dense(maxsize, activation = "relu", input_shape=(38, )))
# Hidden - Layers
# model.add(layers.Dropout(0.3, noise_shape=None, seed=None))
model.add(layers.Dense(20, activation = "relu"))
# model.add(layers.Dropout(0.4, noise_shape=None, seed=None))
# model.add(layers.Dense(10, activation = "relu"))
# Output- Layer
model.add(layers.Dense(1, activation = "sigmoid"))
model.summary()
# compiling the model
model.compile(
 optimizer = "adam",
 loss = "binary_crossentropy",
 metrics = ["accuracy"]
)
# results = model.fit(
#     X_train, y_train,
#  epochs= 150,
#  # batch_size = 50,
#  validation_data = (X_test, y_test)
# )
results = model.fit(
    X_train, y_train,
 epochs= 10,
 # batch_size = 50,
    validation_split=0.2,
shuffle=True
)
model.save('ANNModel\\NNA1attempt.h5')

                       ###############  Plots    #################
import matplotlib.pyplot as plt

#  "Plot Accuracy" #uncomment
# plt.plot(results.history['acc'])
# plt.plot(results.history['val_acc'])
# plt.title('model accuracy')
# plt.ylabel('accuracy')
# plt.xlabel('epoch')
# plt.legend(['train', 'validation'], loc='upper left')
# plt.show()


# # "Plot Loss" #uncomment
# plt.plot(results.history['loss'])
# plt.plot(results.history['val_loss'])
# plt.title('model loss')
# plt.ylabel('loss')
# plt.xlabel('epoch')
# plt.legend(['train', 'validation'], loc='upper left',prop={'size': 15})
# plt.show()




# scores = model.evaluate(X_test,y_test, verbose=0)

#  "Plot Confusion matrix"
# y_pred=model.predict_classes(X_test)
# print(y_pred.shape)
# label=[0,1]
# cnf_matrix = confusion_matrix(y_test, y_pred)
# cm = confusion_matrix(y_test, y_pred,labels=[0,1])
# cm=cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
# plt.imshow(cm, cmap=plt.cm.Blues)
# plt.xlabel("Predicted labels")
# plt.ylabel("True labels")
# tick_marks = np.arange(len(label))
# plt.xticks(tick_marks, label)
# plt.yticks(tick_marks, label)
# plt.title('Confusion matrix ')
# plt.colorbar()
# plt.show()

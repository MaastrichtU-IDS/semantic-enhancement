from keras.models import load_model
# from keras.models import load_weights
import pickle
import numpy as np
import random
import os
from keras.layers import Input, Embedding, Dot, Reshape, Dense
from keras.models import Model
pos_pairs=[]
neg_pairs=[]
pos_pairskey=[]
neg_pairskey=[]
##################build complete training set with second approach and test with batches over 100 iterations
dir_pos="training\\pos2\\"
dir_neg="training\\neg2\\"

with open(dir_pos+"tupleshgnctraining.txt","r") as file:
        for line in file:
            nline=line.split(" ")
            nline[1]=nline[1].strip()
            pos_pairs.append(nline)
with open(dir_pos+"tuplesnametrainingnew.txt", "r") as file:
    for line in file:
        nline = line.split(" ")
        nline[1] = nline[1].strip()
        pos_pairs.append(nline)
with open(dir_pos+"tuplessymboltrainingnew.txt", "r") as file:
        for line in file:
            nline = line.split(" ")
            nline[1] = nline[1].strip()
            pos_pairs.append(nline)

with open(dir_neg+"negativedatagenenew.txt","r") as file:
    for line in file:
        nline=line.split(" ")
        nline[1]=nline[1].strip()
        neg_pairs.append(nline)

with open(dir_neg+"negativedatahgnc.txt","r") as file:
    for line in file:
        nline=line.split(" ")
        nline[1]=nline[1].strip()
        neg_pairs.append(nline)

with open(dir_neg+"negativedatahgnclocnew.txt","r") as file:
    for line in file:
        nline=line.split(" ")
        nline[1]=nline[1].strip()
        neg_pairs.append(nline)
# print(len(pos_pairs))
# print(len(pos_pairs) // 1024)
random.seed(100)
print(pos_pairs[100])
random.shuffle(pos_pairs)
print(pos_pairs[100])
random.seed(100)
random.shuffle(neg_pairs)
trainp=[]
trainn=[]
testp=[]
testn=[]

#
for i in range(len(pos_pairs)):
    if i<=int(0.8*len(pos_pairs)):
        trainp.append(pos_pairs[i])
    else:
        # print(i)
        testp.append(pos_pairs[i])
for i in range(len(neg_pairs)):
    if i<=int(0.8*len(neg_pairs)):
        trainn.append(neg_pairs[i])
    else:
        testn.append(neg_pairs[i])

# with open("testp.txt", "wb") as f:
#     pickle.dump(testp, f)
# with open("testn.txt", "wb") as f:
#     pickle.dump(testn, f)
#
# with open("testp.txt", "rb") as fp:   # Unpickling
#        testp = pickle.load(fp)
# with open("testn.txt", "rb") as fp:  # Unpickling
#     testn = pickle.load(fp)

# print(len(trainp))
def generate_batch(p_pairs,n_pairs, n_positive = 50, negative_ratio = 1.0, classification=True):
    # """Generate batches of samples for training"""
    batch_size = n_positive * (1 + negative_ratio)
    batch = np.zeros((batch_size, 3))
    # print(batch_size)
    # Adjust label based on task
    if classification:
        neg_label = 0
    else:
        neg_label = -1 #regression

    # This creates a generator
    while True:
        # randomly choose positive examples
        for idx, (col, data) in enumerate(random.sample(p_pairs, int(batch_size/2))):
            batch[idx, :] = (col, data, 1)

        # Increment idx by 1
        idx += 1

        # Add negative examples until reach batch size
        while idx < batch_size:
            # print(random.sample(n_pairs,1))
            randneg=random.sample(n_pairs, 1)
            batch[idx, :] = (randneg[0][0], randneg[0][1], neg_label)
            idx += 1

        # Make sure to shuffle order
        np.random.shuffle(batch)
        np.savetxt('outputgeneratedtrain.txt', batch, fmt='%i', delimiter=',')
        yield {'col': batch[:, 0], 'data': batch[:, 1]}, batch[:, 2]



# x, y = next(generate_batch(pos_pairs,neg_pairs, n_positive = 2, negative_ratio = 2))
# # #
# # Show a few example training pairs
# for label, c_idx, d_idx in zip(y, x['col'], x['data']):
#     print(f'Book: {c_idx:30} Link: {d_idx:40} Label: {label}')


def book_embedding_model(embedding_size=50, classification=True):
    """Model to embed col and values """

    # Both inputs are 1-dimensional
    col = Input(name='col', shape=[1]) #col
    data = Input(name='data', shape=[1]) #data

    # Embedding the col (shape will be (None, 1, 50))
    col_embedding = Embedding(name='col_embedding',
                              input_dim=17,#17
                              output_dim=embedding_size)(col)


    # Embedding the data (shape will be (None, 1, 50))
    data_embedding = Embedding(name='data_embedding',
                               input_dim=167251,#140050
                               output_dim=embedding_size)(data)

    # Merge the layers with a dot product along the second axis (shape will be (None, 1, 1))
    merged = Dot(name='dot_product', normalize=True, axes=2)([col_embedding, data_embedding])

    # Reshape to be a single number (shape will be (None, 1))
    merged = Reshape(target_shape=[1])(merged)


    # If classifcation, add extra layer and loss function is binary cross entropy
    if classification:
        merged = Dense(1, activation='sigmoid')(merged)
        model = Model(inputs=[col, data], outputs=merged)
        model.compile(optimizer='Adam', loss='binary_crossentropy', metrics=['accuracy'])

    # Otherwise loss function is mean squared error
    else:
        model = Model(inputs=[col, data], outputs=merged)
        model.compile(optimizer='Adam', loss='mse')

    return model



# # Instantiate model and show parameters
nmodel = book_embedding_model()
# print(model.summary())

n_positive = 1024
gen=generate_batch(trainp,trainn, n_positive, negative_ratio = 2,classification = True)



#generate test
def generateagain(plist,nlist):
    p = [1] * len(plist)
    n=[0]*len(nlist)
    l=p+n
    larray=np.array(l)
    test=plist+nlist
    batch= np.array(test)
    print(len(l))
    newarray=larray.reshape(45121,1)
    batch=np.append(batch,newarray,axis=1)
    # batch=np.loadtxt('outputgeneratedtrain.txt',delimiter=',',dtype=int)#
    np.random.shuffle(batch)

    nbatch=batch[:10,:]
    np.save('outputgenerated.npy', nbatch)
    yield {'col': nbatch[:, 0], 'data': nbatch[:, 1]}, nbatch[:, 2]
    # return batch
gent=generateagain(testp,testn)


# Train
h = nmodel.fit_generator(gen, epochs = 2,
                         steps_per_epoch=100,
                        verbose = 2)#10
nmodel.save("EmbeddingModels\\testattempt2.h5")
nmodel.save_weights('EmbeddingModels\\testattempt2w.h5')
# nmodel.save('EmbeddingModels\\fifth_attempt10epoch100steps.h5')
# nmodel.save_weights("EmbeddingModels\\fifth_attempt10epoch100stepsweights.h5")


# model = load_model("EmbeddingModels\\fifth_attempt10epoch100steps.h5")
# model.load_weights("EmbeddingModels\\fifth_attempt10epoch100stepsweights.h5")
model = load_model("EmbeddingModels\\testattempt2.h5")
model.load_weights("EmbeddingModels\\testattempt2w.h5")


#
def class_assigment(y):
    classes=[]
    for item in y:
        if item>0.8:
            classes.append(1)
        else:
            classes.append(0)
    return classes
results=[]
for t in range(100):
    gent = generateagain(testp, testn)
    y=model.predict_generator(gent,steps =1)
    c=class_assigment(y)
    # print(c)
    batch=np.load('outputgenerated.npy')
    test=list(batch[:,2])
    test=[int(j) for j in test]
    matches=0
    # print(test)
    for i in range(len(c)):
        if c[i]==test[i]:
            matches+=1
    results.append(matches/len(c)*100)
print(results)
import matplotlib.pyplot as plt
# plt.plot(results,linewidth=4.0)
# plt.plot(results,'ro')
# plt.ylabel('Results')
# plt.show()
# Create some random data
x = np.arange(0,100,1)
y = results
# y = [random.random()*5 for i in x]

# Calculate the simple average of the data
y_mean = [np.mean(y)]*len(x)

fig,ax = plt.subplots()

# Plot the data
data_line = ax.plot(x,y, label='Data', marker='o')

# Plot the average line
mean_line = ax.plot(x,y_mean, label='Mean', linestyle='--')

# Make a legend
legend = ax.legend(loc='upper right',prop={'size': 15})

plt.show()





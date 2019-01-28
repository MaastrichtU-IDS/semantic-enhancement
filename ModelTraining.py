import numpy as np
import random
import os
from keras.layers import Input, Embedding, Dot, Reshape, Dense
from keras.models import Model
##################build complete training set with first approach
pos_pairs=[]
neg_pairs=[]

dir_pos="training\\pos\\"
dir_neg="training\\neg\\"


with open(dir_pos + "tupleshgnctraining.txt", "r") as file:
    for line in file:
        nline = line.split(" ")
        nline[1] = nline[1].strip()
        pos_pairs.append(nline)
with open(dir_pos + "tuplesnametraining1.txt", "r") as file:
    for line in file:
        nline = line.split(" ")
        nline[1] = nline[1].strip()
        pos_pairs.append(nline)
with open(dir_pos + "tuplessymboltraining.txt", "r") as file:
    for line in file:
        nline = line.split(" ")
        nline[1] = nline[1].strip()
        pos_pairs.append(nline)
with open(dir_neg+"negativedatagene.txt","r") as file:
    for line in file:
        nline=line.split(" ")
        nline[1]=nline[1].strip()
        neg_pairs.append(nline)

with open(dir_neg+"negativedatahgnc.txt","r") as file:
    for line in file:
        nline=line.split(" ")
        nline[1]=nline[1].strip()
        neg_pairs.append(nline)

with open(dir_neg+"negativedatahgncloc.txt","r") as file:
    for line in file:
        nline=line.split(" ")
        nline[1]=nline[1].strip()
        neg_pairs.append(nline)
# print(len(pos_pairs))
# print(len(neg_pairs))
random.seed(100)
# X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.2)
# print X_train.shape, y_train.shape
# print X_test.shape, y_test.shape

def generate_batch(p_pairs,n_pairs, n_positive = 50, negative_ratio = 1.0, classification=False):
    """Generate batches of samples for training"""
    batch_size = n_positive * (1 + negative_ratio)
    batch = np.zeros((batch_size, 3))

    # Adjust label based on task
    if classification:
        neg_label = 0
    else:
        neg_label = -1 #regression

    # This creates a generator
    while True:
        # randomly choose positive examples
        for idx, (col, data) in enumerate(random.sample(p_pairs, n_positive)):
            batch[idx, :] = (col, data, 1)

        # Increment idx by 1
        idx += 1
        # Add negative examples until reach batch size
        # print("batch"+str(batch_size))
        while idx < batch_size:
            # print(random.sample(n_pairs,1))
            randneg=random.sample(n_pairs, 1)
            batch[idx, :] = (randneg[0][0], randneg[0][1], neg_label)
            # # random selection

            #     # Add to batch and increment index

            idx += 1

        # Make sure to shuffle order
        np.random.shuffle(batch)
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
    # print(book)
    # Embedding the book (shape will be (None, 1, 50))
    col_embedding = Embedding(name='col_embedding',
                              input_dim=17,#17
                              output_dim=embedding_size)(col)

    # Embedding the link (shape will be (None, 1, 50))
    data_embedding = Embedding(name='data_embedding',
                               input_dim=140050,#140050
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

gen = generate_batch(pos_pairs,neg_pairs, n_positive, negative_ratio = 2)


# Train
h = nmodel.fit_generator(gen, epochs = 15,
                        steps_per_epoch = len(pos_pairs) // n_positive,
                        verbose = 2)


# nmodel.save('EmbeddingModels\\first_attempt.h5')
#
# col_layer = nmodel.get_layer('col_embedding')
# col_weights = col_layer.get_weights()[0]
# col_weights.shape
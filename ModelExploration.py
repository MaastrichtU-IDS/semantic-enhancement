from keras.models import load_model
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#########Test how the similarity between columns works
model = load_model("EmbeddingModels\\first_attempt.h5") #load the model
col_layer = model.get_layer('col_embedding')
col_weights = col_layer.get_weights()[0]


col_weights = col_weights / np.linalg.norm(col_weights, axis = 1).reshape((-1, 1))

plt.style.use('fivethirtyeight')
plt.rcParams['font.size'] = 15



columns=["hgnc_id","HGNC_ID","hgnc_id_c","symbol","Symbol","Gene Symbol","name","Name","Chromosome","Chromosomal Start GRCh37.p13","Chromosomal Stop GRCh37.p13","date_approved_reserved","date_modified","location","location_sortable","Chromosomal Start GRCh38.p13","Chromosomal Stop GRCh38.p13","PharmGKB Accession Id"]
indext = {el: idx for idx, el in enumerate(columns)}
rindext = {idx: link for link, idx in indext.items()}
# print(rindext[10])
# print(indext["date_approved_reserved"])
# print(rindext[11])
def find_similar(name, weights, index_name='col', n=10, least=False, return_dist=False, plot=False):
    """Find n most similar items (or least) to name based on embeddings. Option to also plot the results"""

    # Select index and reverse index
    if index_name == 'col':
        index = indext
        rindex = rindext
    # elif index_name == 'page':
    #     index = link_index
    #     rindex = index_link

    # Check to make sure `name` is in index
    try:
        # Calculate dot product between book and all others
        dists = np.dot(weights, weights[index[name]])
    except KeyError:
        print(f'{name} Not Found.')
        return

    # Sort distance indexes from smallest to largest
    sorted_dists = np.argsort(dists)

    # Plot results if specified
    if plot:

        # Find furthest and closest items
        furthest = sorted_dists[:(n // 2)]
        closest = sorted_dists[-n - 1: len(dists) - 1]
        # print(closest)
        items = [rindex[c] for c in furthest]
        items.extend(rindex[c] for c in closest)

        # Find furthest and closets distances
        distances = [dists[c] for c in furthest]
        distances.extend(dists[c] for c in closest)

        colors = ['r' for _ in range(n // 2)]
        colors.extend('g' for _ in range(n))

        data = pd.DataFrame({'distance': distances}, index=items)

        # Horizontal bar chart
        data['distance'].plot.barh(color=colors, figsize=(10, 8),
                                   edgecolor='k', linewidth=2)
        plt.xlabel('Cosine Similarity');
        plt.axvline(x=0, color='k');

        # Formatting for italicized title
        name_str = f'{index_name.capitalize()}s Most and Least Similar to'
        for word in name.split():
            # Title uses latex for italize
            name_str += ' $\it{' + word + '}$'
        plt.title(name_str, x=0.2, size=28, y=1.05)

        return None

    # If specified, find the least similar
    if least:
        # Take the first n from sorted distances
        closest = sorted_dists[:n]

        print(f'{index_name.capitalize()}s furthest from {name}.\n')

    # Otherwise find the most similar
    else:
        # Take the last n sorted distances
        closest = sorted_dists[-n:]

        # Need distances later on
        if return_dist:
            return dists, closest

        print(f'{index_name.capitalize()}s closest to {name}.\n')

    # Need distances later on
    if return_dist:
        return dists, closest

    # Print formatting
    max_width = max([len(rindex[c]) for c in closest])

    # Print the most similar and distances
    for c in reversed(closest):
        print(f'{index_name.capitalize()}: {rindex[c]:{max_width + 2}} Similarity: {dists[c]:.{2}}')



find_similar('hgnc_id', col_weights) #choose a column
# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BudiBEuHprr7czpFvVEoX5fKqg0rFhoW
"""

import keras
from keras.layers import Activation, Dense, Dropout, Conv2D, \
                         Flatten, MaxPooling2D
from keras.models import Sequential
import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt

# Read Data
data = pd.read_csv('music.csv')
data.head(5)

data = data.drop(["artist.id", "artist.name", "artist_mbtags","location", "song.id","latitude", "key", "longitude", "release.id","release.name","similar", "title", "year"], axis=1)

data=data.drop(["terms_freq", "time_signature", "time_signature_confidence"], axis=1)
data=data.dropna()
data=data[0:100]

x=data[data.columns[0:18]]
y=data["terms"]
Y=np.array(y)
X=np.array(x)

from sklearn import preprocessing
min_max_scaler = preprocessing.MinMaxScaler()
X= min_max_scaler.fit_transform(X)
X

from sklearn.manifold import TSNE
m=TSNE(learning_rate=50)

tsne_data=m.fit_transform(X)

tsne_df=pd.DataFrame(tsne_data)
tsne_data.shape

tsne_df=pd.concat([tsne_df,pd.Series(Y)], axis=1)

colname=list(["Dimension1", "Dimension2", "Label"])
tsne_df.columns=colname
tsne_df.head()

sns.FacetGrid(tsne_df, hue="Label",height=9).map(plt.scatter, "Dimension1", "Dimension2")
plt.legend()
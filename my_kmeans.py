import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

def add_clusters(df, n):
    X = df[["latitude", "longitude"]]
    model = KMeans(n_clusters=n)
    # print(X.head())
    df['cluster'] = model.fit_predict(X)
    print("wtf")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import pickle
from sklearn.cluster import KMeans

def run():
    file_path = 'E:\Zahra - Data Bootcamp\K-means\k-means-homework\data\Mall_Customers.csv'

    sns.set()
    data = pd.read_csv(file_path)

    x = data.iloc[:,3:5]

    n_cluster = 3

    kmeans = KMeans(n_cluster)
    kmeans.fit(x)

    with open('E:\Zahra - Data Bootcamp\K-means\k-means-homework\output\kmeans_location.pkl', 'wb') as f:
        pickle.dump(kmeans, f)

if __name__ == '__main__':
    run()
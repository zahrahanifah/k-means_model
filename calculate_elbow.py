import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans

def elbow(max_cluster):
    sns.set()

    data = pd.read_csv('E:\Zahra - Data Bootcamp\K-means\k-means-homework\data\Mall_Customers.csv')

    print(data)

    x = data.iloc[:, 3:5]

    print(x)

    # within cluster sum of square (jumlah kuadrat dari node-node yang ada dalam cluster)
    wcss=[]
    number_clusters = range(1,max_cluster)

    for i in number_clusters:
        kmeans = KMeans(i)

        kmeans.fit(x)

        wcss_iter = kmeans.inertia_

        wcss.append(wcss_iter)

    print(wcss)

    plt.plot(number_clusters,wcss)
    plt.title('The Elbow Method')
    plt.xlabel('Number of clusters')
    plt.ylabel('WCSS')

    plt.savefig("E:\Zahra - Data Bootcamp\K-means\k-means-homework\output\elbow.png")

if __name__ == '__main__':
    elbow(7)

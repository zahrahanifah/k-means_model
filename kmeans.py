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

    with open('E:\Zahra - Data Bootcamp\K-means\k-means-homework\output\kmeans_location.pkl', 'rb') as f:
         k_means_model = pickle.load(f)

    identified_clusters = k_means_model.fit_predict(x)

    data_with_clusters = data.copy()
    data_with_clusters['Clusters'] = identified_clusters

    plt.scatter(data_with_clusters['Income'], data_with_clusters['Spending'], c=data_with_clusters['Clusters'], cmap='rainbow')

    # label plot
    plt.title('Clustered Customer using K-Means')
    plt.xlabel('Income')
    plt.ylabel('Spending')

    # anotasi plot
    for i, txt in enumerate(data_with_clusters['CustomerID']):
      plt.annotate(txt, (x.loc[i, 'Income'], x.loc[i, 'Spending']))

    plt.savefig("E:\Zahra - Data Bootcamp\K-means\k-means-homework\output\clustered_customer.png") 

if __name__ == '__main__':
    run()
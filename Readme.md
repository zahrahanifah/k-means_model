# Clustering Customer based on their income and spending
We will use algorithm K-means to cluster customer based on income and spending. The general step would be:
1. Create python script/file to find the best n-cluster using elbow method
2. After we find the best n-cluster, we will use it to create K-means model and store it into `.pkl` file
3. The last step is identified the cluster of each customer using K-means model in `.pkl` file 

#### Step
1. Prepare file `calculate_elbow.py`, do not forget to change the path
2. run `python calculate_elbow.py` in your terminal, find the potential n cluster by take a look into the output of elbow in `/output/`
3. Prepare file `kmeans_pickle.py` to create pickle file for the model
4. run `python kmeans_pickle.py` in your terminal, and find there is `.pkl` file in `/output/`
5. Prepare file `kmeans.py` to identified the cluster of each customer
6. run `python kmeans.py` in your terminal, and find there is `clustered_customer.png` file in `/output/`

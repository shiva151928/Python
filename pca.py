import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris

data = load_iris()
x = data.data
y = data.target

scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

pca = PCA(n_components=2)
x_scaled = pca.fit_transform(x_scaled)

print("Explained variance ratio of each principal component:")
print(pca.explained_variance_ratio_)

plt.figure(figsize=(8, 5))
plt.scatter(x_scaled[:, 0], x_scaled[:, 1], c=y, cmap='viridis',
            edgecolor='k', s=100)

plt.title("PCA Visualization - 2 Principal Components")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.colorbar(label="Class Label")
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

#generar datos

X, y = make_blobs(n_samples=200, centers=2, random_state=42)

#grafitar datos
sns.scatterplot(x=X[:,0], y=X[:, 1], hue=y, palette='viridis')
plt.title("Clusters generados con make_blobs")
plt.show()
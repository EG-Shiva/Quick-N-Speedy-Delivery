import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

sns.set()

sns.set()

data = pd.read_csv('G:/PPT/2 - 2/DAA/Project/Dataset/Dataset1.csv')
plt.scatter(data['Longitude'], data['Latitude'])
plt.xlim(-180, 180)
plt.ylim(-90, 90)
plt.show()

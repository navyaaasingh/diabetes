
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("diabetes-data.csv")


print(df.shape)
print(df.info())
print(df.describe())

print(df.isnull().sum())

df['Outcome'].value_counts().plot(kind='bar')
plt.show()

plt.hist(df['Glucose'], bins=20)
plt.show()

plt.imshow(df.corr())
plt.colorbar()
plt.show()
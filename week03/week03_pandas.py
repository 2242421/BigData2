import pandas as pd

data = [ [14, 72, 100],
         [51, 8, 11],
         [6, 72, 12]]

df = pd.DataFrame(data, index=[1, 2, 3], columns=['a', 'b', 'c'])

print(df)
print(df.shape, df.dtypes)
print(df['b'].value_counts())
print(df['b'].nunique())
print(df.describe())
import pandas as pd

df = pd.DataFrame(
    [
            [14, 72, 100],
            [51, 8, 11],
            [6, 72, 12]
        ],
        index=[1, 2, 3], columns=['a', 'b', 'c'])

print(df)
import pandas as pd
import matplotlib.pyplot as plt

desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 25)


df = pd.read_csv('final_matrix.csv')

df = df.dropna()
print(df)
df.to_csv('final_matrix_clean.csv', index=False)
print(df.shape)

import pandas as pd

url = 'https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/'

dfs = pd.read_html(url)

print(type(dfs))
print(len(dfs))

#Portanto, temos nosso DataFrame com uma lista que contém apenas uma tabela.
df_bancos = dfs[0]

print(df_bancos.shape)
print(df_bancos.dtypes)

df_bancos.head()
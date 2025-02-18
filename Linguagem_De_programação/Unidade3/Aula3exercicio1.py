import pandas as pd

df_selic = pd.read_json('https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json')

print(df_selic.info())

#verificar duplicidade de linhas (passo muito importante), utilizando a função drop_duplicates()
df_selic.drop_duplicates(keep='last', inplace=True)
#mantem o ultimo registro (keep='last')
#através do parâmentro inplace=True, faz com que a transformação seja salva no DataFrame
#no nosso caso não existe linhas duplicadas.

#adicionando colunas
from datetime import date
from datetime import datetime as dt

data_extracao = date.today()

df_selic['data_extracao'] = data_extracao

df_selic['responsavel'] = 'Thais'

print(df_selic.info())

df_selic.head(10)
df_selic.loc[[5,10,20]]

teste = df_selic['valor'] < 0.01
print(type(teste))
print(teste)
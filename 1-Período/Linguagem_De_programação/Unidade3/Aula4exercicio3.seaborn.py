import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style='whitegrid') # opções: darkgrid, whitegrid, dark, white, ticks

df_tips = sns.load_dataset('tips')
print(df_tips)

fig, ax = plt.subplots(1, 3, figsize=(15, 5)) #subplots

sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[0]) #media por sexo

sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[1], estimator=sum) #estimator calcula a média

sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[2], estimator=len)
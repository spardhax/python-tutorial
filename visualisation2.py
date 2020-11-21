import seaborn as sns
import pandas as pd
import numpy as np

tipsy=sns.load_dataset('tips')
tipsy.head()

tipsy=tipsy.rename(columns={'total_bill':'bill'})

sns.barplot(x='sex',y='bill',data=tipsy,estimator=np.std)

sns.countplot(x='sex',data=tipsy)
sns.countplot(y='time',data=tipsy)
sns.boxplot(x='sex',y='bill',data=tipsy)

sns.boxplot(x='day',y='bill',data=tipsy,hue='sex')
sns.violinplot(x='day',y='bill',data=tipsy)
sns.violinplot(x='day',y='bill',data=tipsy,split=True)
sns.distplot(tipsy['bill'])
sns.distplot(tipsy['bill'],kde=False,bins=30,color='y')
sns.kdeplot(tipsy['bill'])
sns.jointplot(x='bill',y='tip',data=tipsy)
sns.jointplot(x='bill',y='tip',data=tipsy,color='g',kind='hex')
sns.jointplot(x='bill',y='tip',data=tipsy,color='black',kind='reg')
sns.pairplot(tipsy,hue='sex')
tipsy.head()

tipsycor=tipsy.corr()
sns.heatmap(tipsycor)

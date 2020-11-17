import cv2
import numpy as np

pokemons={
    "height":np.random.randint(1,100,5),
    "weight":np.random.randint(50,150,5),
    "power":np.random.randint(200,250,5)
}

import pandas as pd

df=pd.DataFrame(pokemons)
print(df)

df.head(n=3)

df.columns

#create CSV(comma separtae)file
df.to_csv('pokemons_data.csv')

#read a data frame
df=pd.read_csv('pokemons_data.csv')

df.head()
df.drop(columns=['Unnamed: 0'])

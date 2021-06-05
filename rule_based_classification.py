import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

df = pd.read_csv("datasets/persona.csv")

print(df.shape)

print(df.head())

print(df.info())

df.groupby(["COUNTRY","SOURCE","SEX","AGE"]).agg({"PRICE": "sum"})

agg_df =  (df.groupby(["COUNTRY","SOURCE","SEX","AGE",]).agg({"PRICE": "sum"} )).sort_values("PRICE",ascending=False)
agg_df

agg_df = agg_df.reset_index()
agg_df

df["AGE"].nunique()

agg_df["AGE_CAT"] = pd.cut(agg_df["AGE"], [0, 18, 25, 35, 45, 67], labels=['0_18', '19_25', '26_35', '36-45', '46_67'])
agg_df

agg_df["customers_level_based"] = [col[0].upper() + "_" + col[1].upper() + "_" + col[2].upper() + "_" + col[5].upper() for col in agg_df.values]
agg_df.head()

agg_df = agg_df.groupby("customers_level_based").agg({"PRICE": "mean"})

agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"], 4 , labels = ["D","C","B","A"])
agg_df

agg_df.groupby("SEGMENT").agg({"PRICE": ["mean","max","sum"]})

agg_df = agg_df.reset_index()
agg_df

# 33 yaşında ANDROID kullanan bir Türk kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir?

user_1  = "TUR_ANDROID_FEMALE_26_35"
agg_df[agg_df["customers_level_based"] ==  user_1 ]  # 413.75  B
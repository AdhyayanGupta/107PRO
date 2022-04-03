
import pandas as pd
import csv
import plotly_express as px


df = pd.read_csv("data107.csv")
#student_df = df.loc[df['student_id']=="TRL_xsl"]
print(df.groupby("level")["attempt"].mean())

fig = px.scatter(
     x = df.groupby("level")["attempt"].mean(),
    y = ['Level 1','Level2','Level3','Level4'],
)
fig.show()

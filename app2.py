import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



st.title("Toronto Covid Infections :chart_with_upwards_trend:")


df = pd.DataFrame(
    np.random.randn(20, 2) / [50, 15] + [43.68, -79.4],
    columns=['lat', 'lon'])

st.map(df)

st.markdown('The Covid Cases in Toronto is controlled, and today we have a low range of new cases, so we are in a good position')

df = sns.load_dataset('Dati.csv')
df = df[ (df['PHU_NAME'] == 'TORONTO')]

lista = ['ACTIVE_CASES', 'RESOLVED_CASES', 'DEATHS']
fig = plt.figure(figsize=(18,10))

ax = plt.gca()
#for i in lista:
for i in lista:
    sns.countplot(kind='line', x='FILE_DATE', y=i, ax=ax)

st.pyplot(fig)
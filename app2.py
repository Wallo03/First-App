import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



st.title("Toronto Covid Infections :chart_with_upwards_trend:")


df = pd.DataFrame( np.random.randn(20, 2) / [50, 15] + [43.68, -79.4], columns=['lat', 'lon'])

st.map(df)

st.markdown('The Covid Cases in Toronto is controlled, and today we have a low range of new cases, amd a high range of resolved cases, so we are in a good position')
st.title("Toronto Covid Chart :chart_with_upwards_trend:")

####################################################################

#fig = plt.figure(figsize=(18,10))
# ax = plt.gca()  ----> NON SI USA QUESTO SU STREAMLIT
# #for i in lista:
# for i in lista:
#sns.countplot(y='ACTIVE_CASES', data=df)
#st.pyplot(fig)

####################################################################

df = pd.read_csv('csvFolder/Dati.csv')
df = df[ (df['PHU_NAME'] == 'TORONTO')]
df1 = pd.DataFrame(df,
    columns=['ACTIVE_CASES', 'RESOLVED_CASES', 'DEATHS'])

st.line_chart(df1)

#PROVA GIT
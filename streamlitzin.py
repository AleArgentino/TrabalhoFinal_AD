#Libraries

import streamlit as st
import pandas as pd
import urllib3
from urllib3 import request
from io import BytesIO
import requests

#Títulos

st.title("Trabalho Final de Análise de Dados")
st.header("Desenvolvido por Alexandre M. Argentino e Nicholas C. Tonhi")
st.subheader("Prof. Massaki Igarashi")

#Tabela Geral

st.write("")
st.write("Tabela Geral:")

http = urllib3.PoolManager()
rD = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vSdXh5LgfEPrWYfXBlR-qNK25CmO-VgIHO1h_CEjChC1eMHl5z5ds3UPjIo5TNb34EQIFrK-bUICDev/pub?gid=0&single=true&output=csv')
dataD = rD.content
df = pd.read_csv(BytesIO(dataD))
df

#Tabela de uma lavoura específica

st.write("")
st.write("Tabela de Lavoura:")

lav_escolhida = df['Nome Lavoura'] == st.selectbox("Escolha um produto",["Guaraná", "Cana-de-açucar", "Soja", "Café", "Goiaba"])
dfLav = df[lav_escolhida]
dfLav

#Tabela de um ano específico

st.write("")
st.write("Tabela de Ano:")

ano_escolhido = df['Ano'] == int(st.slider("Escolha um ano que deseja se aprofundar:", 1990, 2021))
dfAno = df[ano_escolhido]
dfAno

#Gráficos

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

echo "backend: TkAgg" >> ~/.matplotlib/matplotlibrc

#Info's Graf

sele_G = dfAno['Nome Lavoura']=="Guaraná"
dfG = dfAno[sele_G]

sele_C = dfAno['Nome Lavoura']=="Cana-de-açucar"
dfC = dfAno[sele_C]

sele_S = dfAno['Nome Lavoura']=="Soja"
dfS = dfAno[sele_S]

sele_Ce = dfAno['Nome Lavoura']=="Café"
dfCe = dfAno[sele_Ce]

sele_Go = dfAno['Nome Lavoura']=="Goiaba"
dfGo = dfAno[sele_Go]

#Gráfico de Área

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

labels = 'Cana-de-Açucar', 'Guaraná', 'Soja', 'Café', 'Goiaba'
data = [float(dfC['Área Colhida (em milhares de hectares)']), float(dfG['Área Colhida (em milhares de hectares)']), float(dfS['Área Colhida (em milhares de hectares)']), float(dfCe['Área Colhida (em milhares de hectares)']), float(dfGo['Área Colhida (em milhares de hectares)'])]
explode = (0.1, 0.1, 0.1, 0.1, 0.1)

def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return f"{pct:.1f}%\n({absolute:d} ha*10³)"

wedges, texts, autotexts = ax.pie(data, explode = explode, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="black"))

ax.legend(wedges, labels,
          title="Produtos",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")

ax.set_title("Percentual de Área Colhida")

Atotal = float(dfG['Área Colhida (em milhares de hectares)']) + float(dfC['Área Colhida (em milhares de hectares)']) + float(dfS['Área Colhida (em milhares de hectares)']) + float(dfCe['Área Colhida (em milhares de hectares)']) + float(dfGo['Área Colhida (em milhares de hectares)'])

st.write("A área total utilizada no ano escolhido: " + str(Atotal) + " milhares de hectares.")
st.write()

plt.show()
st.pyplot()

#Gracinha

x = st.selectbox("Gostou dessa inovação?",["Não", "Sim"])

if x == "Sim":
  st.balloons()

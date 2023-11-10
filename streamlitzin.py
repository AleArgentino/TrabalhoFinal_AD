#Libraries
import streamlit as st
import pandas as pd
import urllib3
from urllib3 import request
from io import BytesIO
import requests
#import matplotlib.pyplot as plt
import numpy as np

st.title("Trabalho Final de Análise de Dados")
st.header("Desenvolvido por Alexandre M. Argentino e Nicholas C. Tonhi")
st.subheader("Prof. Massaki Igarashi")

#Gráfico Base
http = urllib3.PoolManager()
rD = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vSdXh5LgfEPrWYfXBlR-qNK25CmO-VgIHO1h_CEjChC1eMHl5z5ds3UPjIo5TNb34EQIFrK-bUICDev/pub?gid=0&single=true&output=csv')
dataD = rD.content
df = pd.read_csv(BytesIO(dataD))
df

#Gráfico de um ano específico
ano_escolhido = df['Ano'] == int(st.slider("Escolha um ano que deseja se aprofundar:", 1990, 2021))
dfAno = df[ano_escolhido]
dfAno

#Seleção da lavoura
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

print("A área total utilizada no ano escolhido: " + str(Atotal) + " milhares de hectares.")
print()

plt.show()
print()

fig, ax = plt.subplots()

labels = 'Cana-de-Açucar', 'Guaraná', 'Soja', 'Café', 'Goiaba'
data = [float(dfC['Área Colhida (em milhares de hectares)']), float(dfG['Área Colhida (em milhares de hectares)']), float(dfS['Área Colhida (em milhares de hectares)']), float(dfCe['Área Colhida (em milhares de hectares)']), float(dfGo['Área Colhida (em milhares de hectares)'])]

bar_labels = ['blue', 'orange', 'green', 'brown', 'red']
bar_colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:brown', 'tab:red']

ax.bar(labels, data, label=labels, color=bar_colors)

ax.set_ylabel('Milhares de Hectares')
ax.set_title('Área Colhida')
ax.legend(title='Produtos')

plt.show()

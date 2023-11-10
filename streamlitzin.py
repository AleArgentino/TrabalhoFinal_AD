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
st.write("")
st.write("Tabela Geral:")

http = urllib3.PoolManager()
rD = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vSdXh5LgfEPrWYfXBlR-qNK25CmO-VgIHO1h_CEjChC1eMHl5z5ds3UPjIo5TNb34EQIFrK-bUICDev/pub?gid=0&single=true&output=csv')
dataD = rD.content
df = pd.read_csv(BytesIO(dataD))
df

#Gráfico de uma lavoura específico
lav_escolhida = df[Nome Lavoura] == st.selectbox("Escolha um produto",["Guaraná", "Cana-de-açucar", "Soja", "café", "Goiaba"])
dfLav = df[lav_escolhida]
dfLav

#Gráfico de um ano específico
ano_escolhido = df['Ano'] == int(st.slider("Escolha um ano que deseja se aprofundar:", 1990, 2021))
dfAno = df[ano_escolhido]
dfAno

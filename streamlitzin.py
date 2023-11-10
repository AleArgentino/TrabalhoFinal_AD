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

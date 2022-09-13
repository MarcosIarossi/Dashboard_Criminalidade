# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 00:02:12 2022

@author: Marcos Caceres
"""
# importar pacotes
import streamlit as st
import pandas as pd
import pydeck as pdk


# carregar arquivo
df = pd.read_csv("criminalidade_sp.csv")

# dashboard
st.title("Criminalidade em São Paulo")
st.markdown(
    """
    A **criminalidade** é um problema recorrente no Brasil.
   Esta aplicação foi desenvolvida baseada em conceitos de Ciências de Dados, afim de demonstrar regiões onde há maior indíce de criminalidade.  
   Você poderá visualizar a determinada área desejada, navegando pelo 'Mapa de Criminalidade em São Paulo' abaixo e escolher o ano desejado à esquerda que varia de 2010 a 2018.
    """
)

# informaçao
st.sidebar.info("Foram carregados {} delitos.".format(df.shape[0]))

if st.sidebar.checkbox("Ver dados dos delitos"):
    st.header("Detalhamento de delitos")
    st.write(df)

df.time = pd.to_datetime(df.time)
ano_selecionado = st.sidebar.slider("Selecione um ano", 2010, 2018, 2010)
df_selected = df[df.time.dt.year == ano_selecionado]

st.subheader("Mapa da Criminalidade em São Paulo")
st.map(df_selected)

# st.pydeck_chart(pdk.Deck(
#     initial_view_state=pdk.ViewState(
#         latitude=-23.567145	,
#         longitude=-46.648936,
#         zoom=8,
#         pitch=50
#     ),
#     layers=[
#         pdk.Layer(
#             'HexagonLayer',
#             data=df_selected[['latitude', 'longitude']],
#             get_position='[longitude,latitude]',
#             auto_highlight=True,
#             elevation_scale=50,
#             pickable=True,
#             elevation_range=[0, 3000],
#             extruded=True,
#             coverage=1
#         )
#     ],
# ))



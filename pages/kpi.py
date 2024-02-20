import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import json

st.title('Indicadores Relevantes')




data = pd.read_csv('data.csv', sep=';', index_col=0)

##fig = px.scatter(data, x="PRECIO", y="TOTAL_CONSUMO", color="TIPO_COMBUSTIBLE")
##fig.show()

st.plotly_chart(px.scatter(data, x="PRECIO", y="NOMBRE_PLACA", color="TIPO_COMBUSTIBLE", title="Mapeo del precio de combustible por Tipo de Combustible"))

st.markdown("&nbsp,")

st.plotly_chart(px.scatter(data, x="PRECIO", y="NOMBRE_PLACA", color="DISTRITO", title="Mapeo del precio de combustible por Distrito"))


fig = px.bar(data, x="DISTRITO",y="TIPO_COMBUSTIBLE", color="TIPO_COMBUSTIBLE", barmode="group", 
             title="Usuarios de cada tipo de combustible por distrito")
st.plotly_chart(fig)



import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
from PIL import Image

############
###CONFIG###
############
st.set_page_config(
    page_title="Analiza danych uderzeń meteorytów w Ziemię",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)
##############
### SIDEBAR ###
##############
image = Image.open('asteroid.png')
st.sidebar.image(image, use_column_width="auto")

############
### BODY ###
############
#opis kolumn
st.subheader("Opis kolumn")
st.divider()
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
   st.markdown("**name**", help="Więcej informacji: https://pl.wikipedia.org/wiki/Meteoryt#Nazewnictwo")
   st.write("Meteoryty otrzymują nazwy zgodnie z miejscem upadku lub znalezienia. Meteoryt po znalezieniu może otrzymać nazwę (w języku kraju, w którym spadł) najbliższego charakterystycznego punktu geograficznego, np. rzeki.")
   st.write("**id**")
   st.write("Numer porządkowy, nadany chronologicznie od najsterszego meteorytu.")

with col2:
   st.write("**nametype**")
   st.write("Valid oznacza że meteoryt został sklasyfikowany. Relict oznacza że obiekt został odnaleziony ale nie da się go jednoznaczenie sklasyfikować.")
   st.markdown("**recclass**", help="Więcej informacji: http://www.ptmet.org.pl/old/kat-3-kla.htm")
   st.write("System klasyfikacji meteorytów próbuje grupować podobne meteoryty i umożliwia naukowcom komunikowanie się przy ich omawianiu za pomocą ujednoliconej terminologii. Meteoryty są klasyfikowane według różnych cech, zwłaszcza właściwości mineralogicznych, petrologicznych, chemicznych i izotopowych.")

with col3:
   st.markdown("**mass (g)**", help="Więcej informacji:https://pl.wikipedia.org/wiki/Meteoryt#Rekordy")
   st.write("Meteoryty osiągają masę od paru gram nawet do 60 ton (największy odnaleziony meteoryt Hoba). W Polsce największy odnaleziony meteoryt to Morasko (271kg).")
   st.write("**fall**")
   st.write("Fell oznacza że uderzenie zostało zaobserwowane a metoryt odnaleziony. Found oznacza że meteoryt został odnaleziony.")

with col4:
   st.write("**year**")
   st.write("Rok w którym odnaleziono meteoryt.")
   st.write("**reclat**")
   st.write("Szerokość geograficzna odnalezionego meteorytu.")

with col5:
   st.write("**reclong**")
   st.write("Długość geograficzna odnalezionego meteorytu.")
   st.write("**GeoLocation**")
   st.write("Szerokość i długość geograficzna odnalezionego meteorytu.")







   
   
   


#tabela
st.divider()
file_path = "Meteorite_Landings.csv" 
try:
    df = pd.read_csv(file_path)
    st.subheader("Surowe dane")
    st.dataframe(df, 1600, 500)
except FileNotFoundError:
    st.error(f"Plik CSV o nazwie '{file_path}' nie został znaleziony.")

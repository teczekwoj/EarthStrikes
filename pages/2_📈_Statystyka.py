import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from PIL import Image

st.set_page_config(
    page_title="Analiza danych uderzeń meteorytów w Ziemię",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)
##############
### SIDEBAR ###
##############
image = Image.open('images/asteroid.png')
st.sidebar.image(image, use_column_width="auto")

####################
### WPROWADZENIE ###
####################
#odczyt z sortowaniem year i usuwaniem nulli
df = pd.read_csv("Meteorite_Landings.csv").dropna(subset=['year']).sort_values(by='year', ascending=True)
col1, col2 = st.columns([0.7, 0.3])
with col1:
    #select slider year count
    start_year, end_year = st.select_slider('Wybierz zakres lat', options=df["year"], value=(1930, 2012))
    #wykres year count 
    filtered_df = df[(df["year"] >= start_year) & (df["year"] <= end_year)]
    st.plotly_chart(px.histogram(filtered_df,"year"), use_container_width=True)
with col2:
    #opis wykresu year count
    st.markdown('''
    **Opis**
    - Magna irure incididunt eiusmod nulla eu aliqua laborum sint Lorem mollit consectetur esse.
    - Magna irure incididunt eiusmod nulla eu aliqua laborum sint Lorem mollit consectetur esse.
    - Magna irure incididunt eiusmod nulla eu aliqua laborum sint Lorem mollit consectetur esse.
    - Magna irure incididunt eiusmod nulla eu aliqua laborum sint Lorem mollit consectetur esse.
    ''')
st.divider()
col1, col2 = st.columns([0.3, 0.7])
with col1:
    #opis wykresu fall count
    st.markdown('''
    **Opis**
    - Magna irure incididunt eiusmod nulla eu aliqua laborum sint Lorem mollit consectetur esse.
    - Magna irure incididunt eiusmod nulla eu aliqua laborum sint Lorem mollit consectetur esse.
    - Magna irure incididunt eiusmod nulla eu aliqua laborum sint Lorem mollit consectetur esse.
    - Magna irure incididunt eiusmod nulla eu aliqua laborum sint Lorem mollit consectetur esse.
    ''')
with col2:
#wykres fall count
    fig = px.histogram(df,"fall")
    st.plotly_chart(fig, use_container_width=True)
st.divider() 
col1, col2 = st.columns([0.7, 0.3])
with col1:
    #wykres reclass count
    # Sortowanie danych po ilości wystąpień recclass
    sorted_df = df["recclass"].value_counts().reset_index()
    sorted_df.columns = ["recclass", "count"]

    #multiselect
    options = st.multiselect(
    'Wybierz jaki rodzaj meteorytu chcesz widzieć na wykresie (posortowane rosnąco)', options= sorted_df['recclass'], default=sorted_df['recclass'][:20])
    filtered_df = sorted_df[sorted_df['recclass'].isin(options)]
    # Tworzenie wykresu
    fig = px.bar(filtered_df, x="recclass", y="count", title="Reclass Count - Posortowane malejąco")
    st.plotly_chart(fig, use_container_width=True)
with col2:
    #opis wykresu fall count
    st.markdown('''
    **Opis**
    - Magna irure incididunt eiusmod nulla eu aliqua laborum sint Lorem mollit consectetur esse.
    - Magna irure incididunt eiusmod nulla eu aliqua laborum sint Lorem mollit consectetur esse.
    - Magna irure incididunt eiusmod nulla eu aliqua laborum sint Lorem mollit consectetur esse.
    - Magna irure incididunt eiusmod nulla eu aliqua laborum sint Lorem mollit consectetur esse.
    ''')

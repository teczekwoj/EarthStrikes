import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt

st.set_page_config(
    page_title="Analiza danych uderzeń meteorytów w Ziemię",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

####################
### WPROWADZENIE ###
####################

# Wczytywanie pliku CSV z folderu "Projekt_v1"
file_path = "Meteorite_Landings.csv" 
# Sprawdź, czy plik istnieje
try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    st.error(f"Plik CSV o nazwie '{file_path}' nie został znaleziony.")

    # Utwórz wykres w Altair
chart = alt.Chart(df).mark_bar().encode(
    x=alt.X('year:N', title='Rok'),
    y=alt.Y('count():Q', title='Ilość wystąpień')
).properties(
    title='Ilość wystąpień w danym roku'
)
# Wyświetlenie wykresu w Streamlit
st.altair_chart(chart)
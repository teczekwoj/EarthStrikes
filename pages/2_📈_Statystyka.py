import streamlit as st
import pandas as pd
import plotly.express as px
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
**Wykres przedstawia ilość wystąpień uderzeń meteorytów na Ziemię w zależności od lat.**  
Na osi Y znajduje się liczba wystąpień, a na osi X umieszczone są kolejne lata, w których te uderzenia miały miejsce.  
Całkowita liczba wystąpień wynosi 45 715, co stanowi sumę wszystkich zarejestrowanych przypadków uderzeń meteorytów.             
Zauważalna jest pewna zmienność w ilości uderzeń w poszczególnych latach, co może sugerować różnice w intensywności zjawiska w różnych okresach czasu.   
Zależy ona najpewniej od:
- intensywności spdadków meteorytów w danym roku.
- ruchu Ziemi po orbicie wokół Słońca i systematycznych przelotach w pobliżu Ziemi różnych obiektów typu meteory, komety, ławice itp.
- zapisu danych przez naukowców, nagły wzrost zapisów widać po 1974r.
- najstarszy skatalogowany meteoryt to Nogata L6 o masie 472g z 860r.

    ''')
st.divider()
col1, col2 = st.columns([0.3, 0.7])
with col1:
    #opis wykresu fall count
    st.markdown('''
**Wykres przedstawia ilość wystąpień uderzeń meteorytów na Ziemię w zależności od parametru fall.**  
Oś Y reprezentuje liczbę wystąpień, a oś X zawiera dwie kategorie: "Fell" oraz "Found".

Liczba zdarzeń w kategorii "Fell" wynosi 1107.  
Liczba zdarzeń w kategorii "Found" wynosi 44318.  
Otrzymane wartości wskazują, że większość zarejestrowanych uderzeń meteoroidów została odnaleziona 97.55%, podczas gdy niewielki procent zdarzeń pozostaje jedynie zaobserwowany 2,45%.  
To może wynikać z postępującej technologii i zdolności do systematycznego monitorowania i odnajdywania meteorytów po ich uderzeniu, co z kolei prowadzi do zdecydowanie większej liczby odnalezionych przypadków w porównaniu do zaobserwowanych.
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
    https://almukantarat.pl/wiedza/meteoroidy-meteory-meteoryty/
    - Magna irure incididunt eiusmod nulla eu aliqua laborum sint Lorem mollit consectetur esse.
    - Magna irure incididunt eiusmod nulla eu aliqua laborum sint Lorem mollit consectetur esse.
    - Magna irure incididunt eiusmod nulla eu aliqua laborum sint Lorem mollit consectetur esse.
    ''')

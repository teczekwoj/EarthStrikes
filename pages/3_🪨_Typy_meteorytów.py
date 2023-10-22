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
############sssssss
### BODY ###
############

col1, col2, col3, col4 = st.columns(4)
with col1: 
    category = st.selectbox(
    'Wybierz kategorię meteorytów',
    ('Chondryty', 'Achondryty', 'Żelazne (klasyfikacja strukturalna)','Żelazne (klasyfikacja chemiczna)', 'Kamienno-żelazne'))

irons = None
case = []
chondrites_zwyczajne = None
if category == 'Chondryty':
    with col2:
        chondrites_types = st.selectbox(
        'Wybierz podkategorię',
        ('Chondryty enstatytowe', 'Chondryty zwyczajne', 'Chondryty węgliste', 'Kakangari-type', 'Rumurutiites'))
    with col3:
         
         if chondrites_types == 'Chondryty zwyczajne':
                chondrites_zwyczajne = st.selectbox(
                'Wybierz podkategorię',
                ('Chondryty H', 'Chondryty L', 'Chondryty LL'))
             
    st.divider()
    st.markdown('''   
    tekst o Chondrytach
    ''')
    if chondrites_types == 'Chondryty enstatytowe':
            st.markdown('''   
            tekst o Chondryty enstatytowe
            ''')
    if chondrites_types == 'Chondryty węgliste':
            st.markdown('''   
            tekst o Chondryty węgliste
            ''')
    if chondrites_types == 'Kakangari-type':
            st.markdown('''   
            tekst o Kakangari-type
            ''')        
    if chondrites_types == 'Rumurutiites':
            st.markdown('''   
            tekst o Rumurutiites
            ''')    
    if chondrites_zwyczajne == 'Chondryty H':
            st.markdown('''   
            tekst o Chondryty H
            ''')
    elif chondrites_zwyczajne == 'Chondryty L':
            st.markdown('''   
            tekst o Chondryty L
            ''')
    elif chondrites_zwyczajne == 'Chondryty LL':
            st.markdown('''   
            tekst o Chondryty LL
            ''')

if category == 'Achondryty':
    with col2:
        case = st.multiselect(
        'Wybierz grupę Achondytów',
        ['Howardites', 'Eucrites', 'Diogenite', 'Shergottites','Nakhlites','Chassignite','Lunar','Aubrites','Acapulcoite','Lodranite','Ureilites','Angrite','Brachinite','Winonaite'])
    st.divider()
    st.markdown('''   
    Tabela o Achondrytach
    ''')

for selected_case in case:
        if selected_case == 'Howardites':
            st.markdown('Tekst o Howardites')
        elif selected_case == 'Eucrites':
            st.markdown('Tekst o Eucrites')
        elif selected_case == 'Diogenite':
            st.markdown('Tekst o Diogenite')
        elif selected_case == 'Shergottites':
            st.markdown('Tekst o Shergottites')
        elif selected_case == 'Nakhlites':
            st.markdown('Tekst o Nakhlites')
        elif selected_case == 'Chassignite':
            st.markdown('Tekst o Chassignite')
        elif selected_case == 'Lunar':
            st.markdown('Tekst o Lunar')
        elif selected_case == 'Aubrites':
            st.markdown('Tekst o Aubrites')
        elif selected_case == 'Acapulcoite':
            st.markdown('Tekst o Acapulcoite')
        elif selected_case == 'Lodranite':
            st.markdown('Tekst o Lodranite')
        elif selected_case == 'Ureilites':
            st.markdown('Tekst o Ureilites')
        elif selected_case == 'Angrite':
            st.markdown('Tekst o Angrite')
        elif selected_case == 'Brachinite':
            st.markdown('Tekst o Brachinite')
        elif selected_case == 'Winonaite':
            st.markdown('Tekst o Winonaite')
        
if category == 'Żelazne (klasyfikacja strukturalna)':
    with col2:
        irons = st.selectbox(
        'Wybierz podkategorię',
        ('Heksaedryty', 'Oktaedryty', 'Ataksyty'))
    st.divider()
    st.markdown('''   
    Tabela o Meteorytach z żelaza (klasyfikacja strukturalna)
        ''')
if irons == 'Heksaedryty':
            st.markdown('''   
            tekst o Heksaedryty
            ''')
if irons == 'Oktaedryty':
            st.markdown('''   
            tekst o Oktaedryty
            ''')
if irons == 'Ataksyty':
            st.markdown('''   
            tekst o Ataksyty
            ''')

if category == 'Żelazne (klasyfikacja chemiczna)':
    st.divider()
    st.markdown('''   
    Tabela o Meteorytach z żelaza (klasyfikacja chemiczna)
        ''')
    
if category == 'Kamienno-żelazne':
    with col2:
        irons = st.selectbox(
        'Wybierz podkategorię',
        ('Pallasyty', 'Mezosyderyty'))
    st.divider()
    st.markdown('''   
    Tabela o Meteorytach Kamienno-żelazne
        ''')
if irons == 'Pallasyty':
            st.markdown('''   
            tekst o Pallasyty
            ''')
if irons == 'Mezosyderyty':
            st.markdown('''   
            tekst o Mezosyderyty
            ''')

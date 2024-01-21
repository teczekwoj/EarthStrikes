import streamlit as st
import pandas as pd
from PIL import Image
from zmienne_tekstowe import *

############
###CONFIG###
############

st.set_page_config(
    page_title="Analiza danych uderzeń meteorytów w Ziemię",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded")

##############
### SIDEBAR ##
##############

image = Image.open('images/asteroid.png')
st.sidebar.image(image, use_column_width="auto")

############
### BODY ###
############

col1, col2, col3 = st.columns([4,4,6])
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
        'Wybierz typ budowy',
        ('Chondryty enstatytowe', 'Chondryty zwyczajne', 'Chondryty węgliste', 'Kakangari-type', 'Rumurutiites'))
    with col1:
         
         if chondrites_types == 'Chondryty zwyczajne':
                chondrites_zwyczajne = st.selectbox(
                'Wybierz typ szczegółowy typ budowy',
                ('Chondryty H', 'Chondryty L', 'Chondryty LL'))
         
    st.divider()
    st.markdown('''   
    tekst o Chondrytach
    ''')
    if chondrites_types == 'Chondryty zwyczajne':
            st.markdown('''   
            tekst o Chondryty zwyczajne
            ''')
    if chondrites_types == 'Chondryty enstatytowe':
            st.markdown('''   
            tekst o Chondryty enstatytowe
            ''')
            with col3:
                st.dataframe(pd.DataFrame(
                {
                "Cechy wyróżniające/charakter":["Obfite","Wyraźne","Mniej wyraźne","Niewyraźne","Stopione"],
                "Kod": ["E3, EH3, EL3", "E4, EH4. EL4","E5, EH5, EL5","E6, EH6, EL6", "E7" ]
                }),hide_index= True)

    if chondrites_types == 'Chondryty węgliste':
            st.markdown('''   
            tekst o Chondryty węgliste
            ''')
            with col3:
                st.dataframe(pd.DataFrame(
                    {
                    "Kod": ["CI", "	CM1-CM2", "CV2-CV3.3","CR", "CO3-CO3.7", "CK", "CB", "CH","TAG"],
                    "Miejscowość": ["Ivuna", "Mighei", "Vigarano","Renazzo", "Ornans", "Karoonda","Bencubbin", "High Iron", "Tagish Lake"],
                    "Cechy wyróżniające/charakter": ["Friable, more water. Minerals:  Phyllosilicates, magnetite", "Friable, more water. Minerals:  Phyllosilicates, magnetite", "Fe rich olivine, CAIs","Minerals:  Phyllosilicates, pyroxene, olivine, metal", "Minerals: Olivine, Pyroxene, CAIs, metal", "Minerals:  Olivine, CAIs","Minerals:  Metal, Pyroxene.  [ongoing research suggests the product of asteroidal collisions.]", "Minerals:  Pyroxene, metal, olivine.  [May be related to Bencubbinites]", "This is a unique meteorite that samples the D asteroid family"],  
                    }),hide_index= True)
    if chondrites_types == 'Kakangari-type':
            st.markdown('''   
            tekst o Kakangari-type
            ''')     
            with col3:
                st.dataframe(pd.DataFrame(
                    {
                    "Kod": ["K"],
                    }),hide_index= True)               
    if chondrites_types == 'Rumurutiites':
            st.markdown('''   
            tekst o Rumurutiites
            ''')    
            with col3:
                st.dataframe(pd.DataFrame(
                    {
                    "Kod": ["R"],
                    "Cechy wyróżniające/charakter": [" Minerals: Olivine, pyroxene, plagioclase, sulfide."],  
                    }),hide_index= True)
    if chondrites_zwyczajne == 'Chondryty H':
            st.markdown('''   
            tekst o Chondryty H
            ''')
            with col3:
                st.dataframe(pd.DataFrame(
                {
                "Cechy wyróżniające/charakter":["Obfite","Wyraźne","Mniej wyraźne","Niewyraźne","Stopione"],
                "Kod": ["H3-H3.9", "H4","H5","H6", "H7" ]
                }),hide_index= True)

    elif chondrites_zwyczajne == 'Chondryty L':
            st.markdown('''   
            tekst o Chondryty L
            ''')
            with col3:
                st.dataframe(pd.DataFrame(
                {
                "Cechy wyróżniające/charakter":["Obfite","Wyraźne","Mniej wyraźne","Niewyraźne","Stopione"],
                "Kod": ["L3-L3.9", "L4","L5","L6", "L7" ]
                }),hide_index= True)

    elif chondrites_zwyczajne == 'Chondryty LL':
            st.markdown('''   
            tekst o Chondryty LL
            ''')
            with col3:
                st.dataframe(pd.DataFrame(
                {
                "Cechy wyróżniające/charakter":["Obfite","Wyraźne","Mniej wyraźne","Niewyraźne","Stopione"],
                "Kod": ["LL3-LL3.9", "LL4","LL5","LL6", "LL7" ]
                }),hide_index= True)


if category == 'Achondryty':
    with col2:
        case = st.multiselect(
        'Wybierz grupę Achondytów',
        ['Howardites', 'Eucrites', 'Diogenite', 'Shergottites','Nakhlites','Chassignite','Lunar','Aubrites','Acapulcoite','Lodranite','Ureilites','Angrite','Brachinite','Winonaite'])
    st.divider()
    st.markdown('''   
    Tabela o Achondrytach
    ''')
    with col3:
        st.dataframe(pd.DataFrame(
            {
            "Kod": ["HOW", "EUC2", "DIO", "SHE", "NAK", "CHA", "LUN", "AUB","ACAP","LOD","URE","ANGR", "BRACH", "WIN"],
            "Grupa": ["Howardites", "Eucrites", "Diogenite", "Shergottites", "Nakhlites", "Chassignite", "Lunar", "Aubrites","Acapulcoite","Lodranite","Ureilites","Angrite", "Brachinite", "Winonaite"],
            "Pochodzenie": ["Vesta regolith", "Vesta basaltic crust", "Vesta deeper/plutonic", "Marian Basalt--shocked", "Martian plutonic rock", "	Martian plutonic rock", "The Moon", "Melted E Chondrite","Melted E Chondrite","	Same as ACAP--more melt","Melted C-chondrite body","Non-HED Basalt", "A or S type Asteroids", "Like IAB & IIICD incl."],  
            "Skład": ["Eucrite-diogenite mix", "Anorthite-pigeonite", "Hypersthene", "Basaltic", "Diopside-olivine", "Olivine", "Basalt and Regolith", "Enstatite","Olivine, Pyroxene","Olivine, Pyroxene","Olivine-pigeonite","Olvn, Pyrx., Plagioclase", "Olivine", ""],
            }),hide_index= True)
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
        'Wybierz typ budowy',
        ('Heksaedryty', 'Oktaedryty', 'Ataksyty'))
    st.divider()
    st.markdown('''   
    Tabela o Meteorytach z żelaza (klasyfikacja strukturalna)
        ''')
    if irons == 'Heksaedryty':
            st.markdown('''   
            tekst o Heksaedryty
            ''')
            with col3:
                st.dataframe(pd.DataFrame(
            {
            "Kod": ["H"],
            "Rozmiar": [">50mm"],  
            }),hide_index= True)      

    if irons == 'Oktaedryty':
            st.markdown('''   
            tekst o Oktaedryty
            ''')
            with col3:
                st.dataframe(pd.DataFrame(
            {
            "Kod": ["Ogg","Og", "Om", "Of", "Off", "Opl"],
            "Rozmiar": ["Najgrubszy","Gruby", "Średni", "Drobny", "Najdrobniejszy", "Plessyt"],
            "Wymiary": ["3.3-50mm","1.3-3.3mm", "5-1.3mm", "0.2-0.5mm", "0.2mm", "0.2mm Wrzeciona Kamacytowe"],  
            }),hide_index= True)      

    if irons == 'Ataksyty':
            st.markdown('''   
            tekst o Ataksyty
            ''')
            with col3:
                st.dataframe(pd.DataFrame(
            {
            "Kod": ["D"],
            "Rozmiar": ["Bez struktury"],  
            }),hide_index= True)  

if category == 'Żelazne (klasyfikacja chemiczna)':
    st.divider()
    st.markdown('''   
    Tabela o Meteorytach z żelaza (klasyfikacja chemiczna)
        ''')
    
if category == 'Kamienno-żelazne':
    with col2:
        irons = st.selectbox(
        'Wybierz typ budowy',
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

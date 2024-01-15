import streamlit as st
from PIL import Image


############
###CONFIG###
############
st.set_page_config(
    page_title="Analiza danych uderzeń meteorytów w Ziemię",
    page_icon="🚀",
    layout="centered",
    initial_sidebar_state="expanded"
)
##############
### SIDEBAR ###
##############
image = Image.open('images/asteroid.png')
st.sidebar.image(image, use_column_width="auto")

############
### BODY ###
############
t1 = '''
Witaj w Twoim zaawansowanym narzędziu do analizy danych dotyczących uderzeń meteorytów w naszą Planetę!  
Platforma oferuje fascynujący wgląd w niebiańskie zjawiska, które kształtują historię naszej planety.
'''
t2 = '''
Od czasów prehistorycznych, uderzenia meteorytów stanowiły nieodłączną część ewolucji Ziemi.
Te tajemnicze skarby kosmiczne przynoszą ze sobą nie tylko wyzwania,
ale także niesamowite możliwości naukowe. Aplikacja została stworzona,
aby pomóc w zgłębianiu tajemnic tych uderzeń i zrozumieniu ich wpływu na naszą planetę.
'''
t3 = '''
Nasza aplikacja webowa dostarcza dane gromadzone przez NASA, narzędzia wizualizacji 
i zaawansowanych analiz, które pozwalają na zgłębienie wiedzy na temat uderzeń 
meteorytów na Ziemi. Dzięki temu narzędziu możesz:  
  
◾ **Odkrywać dane** - Przeglądaj ogromną ilość informacji na temat uderzeń meteorytów, włączając w to ich rozmiary, lokalizacje i daty.  
◾ **Analizować trendy** - Śledź zmiany w częstotliwości uderzeń meteorytów na przestrzeni lat i zrozum, jak wpływają na naszą planetę.  
◾ **Wizualizować dane** - Korzystaj z interaktywnych wykresów i map, aby bardziej przejrzysto przedstawić wyniki analizy danych.  
◾ **Dzielić się wiedzą** - Udostępniaj swoje wnioski i analizy z innymi badaczami lub pasjonatami astronomii.  
'''
st.write("## Aplikacja do analizy danych uderzeń meteorytów w Ziemię 🚀")
st.divider()
st.write(t1)
st.write(t2)
st.divider() 
st.write(t3)
st.divider()  # 👈 Draws a horizontal rule

with st.expander("Czym jest meteoryt?"):
    st.write('''
Ponieważ pojęcia meteoroidu, meteoru i opisywanego meteorytu są często mylone ze sobą, istotne jest wskazanie różnic pomiędzy nimi:

Meteoroidy są to małe ciała znajdujące się w kosmosie (najdrobniejsze tworzą pył kosmiczny). Na ogół są to fragmenty planetoid, bądź komet, powstałych podczas formowania się Układu Słonecznego, bardzo rzadko ze zderzeń planetoid. Najwięcej meteoroidów krąży między orbitami Marsa i Jowisza w pasie planetoid. W przestrzeni kosmicznej meteoroidy zderzają się ze sobą przez co ulegają dalszej fragmentacji, wypadają ze swoich orbit i niekiedy wpadają na kurs kolizyjny z Ziemią. Te, które wpadną w atmosferę ziemską, przelatują przez nią z początkową prędkością ok. 20 km/s, a na skutek oporu powietrza wyhamowują na wysokości 20–40 km, rozgrzewając się i świecąc. Ich świetlne ślady nazywa się meteorami. W trakcie hamowania, na skutek wzrostu temperatury, następuje najczęściej całkowite unicestwienie takiego meteoroidu. Jednak czasami, w przypadku większych obiektów, zdarza się, że ich ocalałe części docierają do powierzchni Ziemi i to one właśnie nazywane są meteorytami.

Większe meteoroidy przy wkraczaniu w atmosferę, ze względu na dużą masę i prędkość, rozpadają się i spadają na powierzchnię Ziemi jako „deszcz meteorytowy”. Powierzchnię spadku nazywamy elipsą rozsiania.  
Więcej informacji: https://pl.wikipedia.org/wiki/Meteoryt
''')
    
with st.expander("Misja DART"):
    st.write('''
Bezzałogowa misja sondy kosmicznej, której celem był test technologii zapobiegających kolizji obiektów NEO z Ziemią. Zadaniem sondy DART była planowana kolizja impaktora z Dimorphosem – księżycem planetoidy Didymos, w celu sprawdzenia, czy celowe rozbicie sondy kosmicznej o asteroidę jest efektywnym sposobem na zmianę jej kursu. Sonda DART została wyniesiona na orbitę 24 listopada 2021 z Vandenberg Space Force Base w Kalifornii za pomocą rakiety nośnej Falcon 9 i zderzyła się z asteroidą docelową 27 września 2022 o 01:14  
Więcej informacji: https://pl.wikipedia.org/wiki/Double_Asteroid_Redirection_Test             
''')







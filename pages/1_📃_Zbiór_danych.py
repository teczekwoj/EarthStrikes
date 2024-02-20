import streamlit as st
import pandas as pd
from PIL import Image

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

st.subheader("Źródło danych", anchor=False)
st.divider()
col1, col2 = st.columns([0.6, 0.4])

with col1:
   url = "https://meteoritical.org/"
   st.markdown('''
Ten obszerny zestaw danych z [The Meteoritical Society](%s) zawiera informacje o wszystkich znanych lądowaniach meteorytów. Tabela zawiera aż 34 513 meteorytów!  
Dane pochodzą z NASA Open Data Portal, czyli portalu gdzie NASA udostępnia niektóre swoje dane. Zespół Programu Zarządzania Informacjami NASA wspiera wysiłki NASA w udostępnianiu dostępu do badań oraz otwartych zestawów danych w formacie,
który jest użyteczny dla użytkowników.   
W ten sposób mają nadzieję pobudzić kreatywne myśli i wyposażyć innych w narzędzia do innowacji na Ziemi
zarówno na poziomie lokalnym, globalnym, jak i międzygwiezdnym, wykorzystując zasoby cyfrowe.
Choć NASA nie jest w stanie obecnie oferować podróży kosmicznych, to zespół Programu Zarządzania Informacjami jest gotowy do współpracy z 
innymi w rozwiązywaniu wyzwań na naszej planecie, korzystając z danych, narzędzi i zasobów dostępnych w agencji.

''' % url, help= "Więcej informacji o DATA.NASA.GOV:  https://data.nasa.gov")
   
with col2:
   st.image("images/nasa-logo.png")


#opis kolumn
st.subheader("Opis kolumn", anchor=False)
st.divider()
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
   st.markdown("**name**", help="Więcej informacji: https://pl.wikipedia.org/wiki/Meteoryt#Nazewnictwo")
   st.write("Meteoryty otrzymują nazwy zgodnie z miejscem upadku lub znalezienia. Meteoryt po znalezieniu może otrzymać nazwę (w języku kraju, w którym spadł) najbliższego charakterystycznego punktu geograficznego, np. rzeki.")
   st.write("**id**")
   st.write("Numer porządkowy, nadany chronologicznie od najsterszego meteorytu.")

with col2:
   st.write("**nametype**")
   st.write("Wartość „valid” odnosi się do większości meteorytów, a „relikt” dotyczy obiektów, które kiedyś były meteorytami, ale obecnie na Ziemi uległy znacznym zmianom pod wpływem warunków.")
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
    st.subheader("Surowe dane", anchor=False)
    st.dataframe(df, 1600, 500)
except FileNotFoundError:
    st.error(f"Plik CSV o nazwie '{file_path}' nie został znaleziony.")

st.divider()
col1, col2, col3, col4, col5, col6 = st.columns(6)
with col1:
   st.info(":four::five::seven::one::five: uniklalnych meteorytów o niepowtarzalnych nazwach")
with col2:
   st.info("Z pośród wszystkich tylko wśród :one::one::one::zero: zostało zaobserwowane uderzenie")
with col3:
   st.info(f"**{round(df['mass (g)'].sum()/1000)}** kg - tyle wynosi łączna masa meteorytów które spadły na Ziemię. Jest to zaledwie 6% masy wieży Eiffla.")
with col4:
   st.info("**69.14%** wszystkich znalezisk odkyto na Antarktydzie")

   
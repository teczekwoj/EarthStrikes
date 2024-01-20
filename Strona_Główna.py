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
### SIDEBAR ##
##############

image = Image.open('images/asteroid.png')
st.sidebar.image(image, use_column_width="auto")

############
### BODY ###
############

t1 = '''
Witaj w zaawansowanym narzędziu do analizy danych dotyczących uderzeń meteorytów w naszą Planetę!  
Platforma oferuje fascynujący wgląd w niebiańskie zjawiska, które kształtują historię naszej planety.
'''
t2 = '''
Od czasów prehistorycznych, uderzenia meteorytów stanowiły nieodłączną część ewolucji Ziemi.
Te tajemnicze skarby kosmiczne przynoszą ze sobą nie tylko wyzwania,
ale także niesamowite możliwości naukowe. Aplikacja została stworzona,
aby pomóc w zgłębianiu tajemnic tych uderzeń i zrozumieniu ich wpływu na naszą planetę.
'''
t3 = '''
Aplikacja webowa dostarcza dane gromadzone przez NASA, narzędzia wizualizacji 
i zaawansowanych analiz, które pozwalają na zgłębienie wiedzy na temat uderzeń 
meteorytów w Ziemię. Dzięki temu narzędziu możesz:  
  
◾ **Odkrywać dane** - Przeglądaj ogromną ilość informacji na temat uderzeń meteorytów, włączając w to ich rozmiary, lokalizacje i daty znalezienia lub spadku.  
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
st.divider()

with st.expander("Czym są :green[meteoroidy]?"):
    st.write('''
Meteoroidy to odłamki skalne poruszające się po orbicie wokół Słońca. Mogą mieć średnicę między 0,1 mm a 10 m (według definicji Międzynarodowej Unii Astronomicznej). Większe od meteoroidów obiekty to planetoidy lub komety, mniejsze — pył międzyplanetarny. Większość meteoroidów to drobne okruchy, o masie nie przekraczającej 10−6 kg. Ocenia się, że w ciągu doby do atmosfery ziemskiej wpada kilkaset milionów meteoroidów. Oczywiście znaczna większość z nich to te najmniejsze.

Meteoroidy mogą powstawać na dwa sposoby:

-  wyniku zderzeń planetoid z pasu między Marsem, a Jowiszem (lub, rzadziej, z innych obszarów Układu Słonecznego)
- w wyniku rozpadu komety przelatującej blisko Słońca

Źródło: https://almukantarat.pl/wiedza/meteoroidy-meteory-meteoryty/  
(Klub astronomiczny Almukantrat)              
''')
with st.expander("Czym są :green[meteory]?"):
    st.write('''
Nazwa „meteor” pochodzi od greckiego słowa „meteoros”, co znaczy „wysoko na niebie”. Meteor to świecący ślad, jaki zostawia na niebie meteoroid, który wpadł w atmosferę ziemską. To właśnie to zjawisko jest często błędnie nazywane „spadającą gwiazdą”. Po wejściu w atmosferę meteoroid zaczyna się spalać w wyniku silnego oporu powietrza, a właściwie w wyniku adiabatycznego sprężania powietrza tuż przed jego czołem. Jego powierzchnia rozgrzewa się wtedy do temperatury kilku tysięcy st. Celsjusza, ale temperatura w środku skały może tylko nieznacznie wzrosnąć. w przypadku odłamków żelaznych cały meteoroid silnie się rozgrzewa, ponieważ żelazo jest dużo lepszym przewodnikiem cieplnym niż skała. w czasie przelotu meteoroidu przez atmosferę dochodzi do ablacji, czyli topnienia i zwiewania wierzchnich warstw skały. Meteoroid wpada w ziemską atmosferę z prędkością 11–76 km/s. Zaczyna świecić na wysokości 100–130 km, a gaśnie zwykle na wysokości 75–80 km, czasem niżej, nawet do 30 km. Meteor przestaje świecić, w momencie, kiedy początkowa prędkość meteoroidu zostaje wyhamowana i porusza się on tylko spadkiem swobodnym. Warto dodać, że to, co widzimy, nie jest świeceniem samego odłamku skalnego, lecz cząsteczek zjonizowanego powietrza wokół niego.

Meteor jaśniejszy od wszystkich planet, (o jasności większej niż −4 mag) nazywamy bolidem. Powyższa definicja została ustanowiona przez Międzynarodową Unię Astronomiczną.
Międzynarodowa Organizacja Meteorowa wprowadziła dokładniejszą definicję tego zjawiska: bolid to meteor, który widziany w zenicie miałby jasność −3 mag lub większą. Przelotowi bolidu towarzyszą zwykle efekty akustyczne określane jako grzmoty, odgłosy pisku opon czy wystrzałów z karabinu maszynowego. Wyjątkowo jasne bolidy (o jasności większej niż −15 mag) nazywane są superbolidami, a bolidy widziane w dzień to bolidy dzienne.

Większość meteoroidów wpadających do atmosfery ziemskiej ulega całkowitej ablacji w mezosferze. Niektóre docierają do powierzchni Ziemi jako meteoryty. Znane są również sporadyczne przypadki meteorów, które wleciały do atmosfery pod bardzo małym kątem i wyleciały z niej z powrotem w przestrzeń kosmiczną (np. bolid, który przeleciał 22.09.2008 r. nad Findlandią). To, jak się zakończy przelot meteoru zależy od masy meteoroidu, jego prędkości początkowej oraz kąta, pod którym wpadł do atmosfery.

Źródło: https://almukantarat.pl/wiedza/meteoroidy-meteory-meteoryty/  
(Klub astronomiczny Almukantrat)   
''')
with st.expander("Czym są :green[meteoryty]?"):
    st.write('''
Meteoryt to, najprościej mówiąc, meteoroid, który dotarł w postaci ciała stałego do powierzchni Ziemi. Szacuje się, że na Ziemię codziennie spada od 100 do nawet 1000 ton meteorytów. Oczywiście większość z nich to drobne okruchy.

Największe szanse na dotarcie do powierzchni Ziemi mają meteoroidy o dużej masie i małej prędkości początkowej. Większe meteoryty zwykle nie spadają na Ziemię w jednym kawałku, ale rozpadają się na wskutek oporu powietrza. Przy dużej ilości meteorytów pochodzących z jednego meteoru mówi się o deszczu meteorytów. Powierzchnię spadku takiego deszczu nazywa się elipsą rozsiania. Może ona osiągnąć długość kilku, kilkunastu, a nawet kilkudziesięciu kilometrów.

Podczas ablacji w atmosferze ziemskiej, meteor pozostawia za sobą smugi materii meteorytowej, która później powoli opada na powierzchnię Ziemi. Jest to tzw. pył meteorytowy. Jego warstwa leży na całej Ziemi, jednak w okolicach spadku dużych meteorytów wyraźnie się zagęszcza.

Obecnie znanych jest ok. 1050 meteorytów, które zostały odnalezione w wyniku obserwacji trajektorii lotu oraz ponad 31000 takich, które zostały odnalezione i rozpoznane jako meteoryty, mimo że nikt nie obserwował ich upadku. Regularne poszukiwania meteorytów prowadzone są na Antarktydzie i na Saharze, ponieważ wyróżniają się one w jednolitym krajobrazie tych miejsc. Nazwy meteorytów pochodzą od nazw miejsc, w których je znaleziono (zazwyczaj używa się nazwy geograficznej tego miejsca, jaka obowiązywała w czasach, gdy odnaleziono meteoryt i w języku, jaki obowiązywał wówczas na tym terenie).

Źródło: https://almukantarat.pl/wiedza/meteoroidy-meteory-meteoryty/  
(Klub astronomiczny Almukantrat)   
''')
with st.expander("Misja :green[DART]"):
    st.write('''
Bezzałogowa misja sondy kosmicznej, której celem był test technologii zapobiegających kolizji obiektów NEO z Ziemią. Zadaniem sondy DART była planowana kolizja impaktora z Dimorphosem – księżycem planetoidy Didymos, w celu sprawdzenia, czy celowe rozbicie sondy kosmicznej o asteroidę jest efektywnym sposobem na zmianę jej kursu. Sonda DART została wyniesiona na orbitę 24 listopada 2021 z Vandenberg Space Force Base w Kalifornii za pomocą rakiety nośnej Falcon 9 i zderzyła się z asteroidą docelową 27 września 2022 o 01:14  
Źródło: https://pl.wikipedia.org/wiki/Double_Asteroid_Redirection_Test             
''')







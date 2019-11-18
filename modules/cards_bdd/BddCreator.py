
# Sciypte that fill the database with all cards

from modules.cards_bdd.CardReader import Card, CardBdd

bdd = CardBdd('https://bipbipzizik.firebaseio.com/', 'cards')
bdd.delete()

# CARDS
# Command cards
bdd.write_card(user="axel",
               name="Play/Pause",
               comment="",
               ids="0013397903",
               mode="none",
               action="Command",
               data="playpause")

bdd.write_card(user="axel",
               name="Next",
               comment="",
               ids="0013403195",
               mode="none",
               action="Command",
               data="next")

bdd.write_card(user="axel",
               name="Volum +",
               comment="",
               ids="0005690629",
               mode="none",
               action="Command",
               data="volume/+5")

bdd.write_card(user="axel",
               name="Volum -",
               comment="",
               ids="0005690629",
               mode="none",
               action="Command",
               data="volume/-5")

# For Parents
bdd.write_card(user="axel",
               name="Mathieu Shedid",
               comment="M - Lettre Infinie",
               ids="0013365376",
               mode="none",
               action="spotify:album",
               data="4yYVqX2KierVI3nDV0M2UL")

bdd.write_card(user="axel",
               name="Adebert 2",
               comment="Adebert 2",
               ids="0003586576",
               mode="none",
               action="spotify:album",
               data="45Hm9e77uZVaRnEIYzzpzM")

bdd.write_card(user="axel",
               name="Caravan Palace",
               comment="",
               ids="0013381409",
               mode="none",
               action="spotify:album",
               data="3qU4wXm0Qngbtnr5PiLbFX")

bdd.write_card(user="axel",
               name="Shaka Ponk",
               comment="",
               ids="0013356493",
               mode="none",
               action="spotify:album",
               data="5lFcL4pj96ZRsoIiHpFl79")

bdd.write_card(user="axel",
               name="Gorillaz",
               comment="",
               ids="0005585628",
               mode="none",
               action="spotify:album",
               data="0bUTHlWbkSQysoM3VsWldT")

bdd.write_card(user="axel",
               name="Kavinsky",
               comment="",
               ids="0013343924",
               mode="none",
               action="spotify:album",
               data="3bRM4GQgoFjBRRzhp87Ugb")

# Radio
bdd.write_card(user="axel",
               name="Radio France Inter",
               comment="",
               ids="0005690638",
               mode="none",
               action="tunein",
               data="24875")

bdd.write_card(user="axel",
               name="Radio Nova",
               comment="",
               ids="0013385899",
               mode="none",
               action="tunein",
               data="17696")

bdd.write_card(user="axel",
               name="Radio RTL2",
               comment="",
               ids="0005589167",
               mode="none",
               action="tunein",
               data="50486")

bdd.write_card(user="axel",
               name="Radio Nostalgie",
               comment="",
               ids="0013336496",
               mode="none",
               action="tunein",
               data="2960")

# For hugo
bdd.write_card(user="axel",
               name="Aldebert Enfantillage 1",
               comment="",
               ids="0013200813",
               mode="ClearQueue",
               action="spotify:album",
               data="1xhy7WWxO28XoPKuFlnxSZ")

bdd.write_card(user="axel",
               name="Aldebert Enfantillage 2",
               comment="",
               ids="0013352322",
               mode="ClearQueue",
               action="spotify:album",
               data="45Hm9e77uZVaRnEIYzzpzM")

bdd.write_card(user="axel",
               name="Aldebert Enfantillage 3",
               comment="",
               ids="0013362342",
               mode="ClearQueue",
               action="spotify:album",
               data="77kv2o5PJeW3mim1yWPiMA")

bdd.write_card(user="axel",
               name="Caravan Palace",
               comment="",
               ids="0013177875",
               mode="ClearQueue",
               action="spotify:album",
               data="3qU4wXm0Qngbtnr5PiLbFX")

bdd.write_card(user="axel",
               name="Les petits poissons",
               comment="",
               ids="0013397291",
               mode="ClearQueue",
               action="spotify:track",
               data="35VKLRwEjuR5IuFyGqjMaf")

bdd.write_card(user="axel",
               name="Bateau sur l'eau",
               comment="",
               ids="0013199764",
               mode="ClearQueue",
               action="spotify:track",
               data="7zwcj8LYBpHfcPTgR5LkFg")

bdd.write_card(user="axel",
               name="Pirouette Cacahuete",
               comment="",
               ids="0013400272",
               mode="ClearQueue",
               action="spotify:track",
               data="3yCoWlqfp2wnOS4PeNsADE")

bdd.write_card(user="axel",
               name="Un grand Cerf",
               comment="",
               ids="0013337950",
               mode="ClearQueue",
               action="spotify:track",
               data="16nCFJAHubC7sj9LsTt3KF")

bdd.write_card(user="axel",
               name="Planter les choux",
               comment="",
               ids="0013385163",
               mode="ClearQueue",
               action="spotify:track",
               data="7IDzwsobKLjgaqg6keknrE")

bdd.write_card(user="axel",
               name="Coucou Hibou",
               comment="",
               ids="0013353316",
               mode="ClearQueue",
               action="spotify:track",
               data="2eu7C32YZKEyILfPHPwVa3")

# Playlist
bdd.write_card(user="axel",
               name="Légendes du Rock",
               comment="",
               ids="0013193487",
               mode="none",
               action="spotify:playlist",
               data="37i9dQZF1DWXTHBOfJ8aI7")

bdd.write_card(user="axel",
               name="Hugo Dance Hugo Go Go",
               comment="",
               ids="0013186464",
               mode="none",
               action="spotify:playlist",
               data="5p0Mw9D1i1EjkJyIafFsvH")

# To assign
bdd.write_card(user="axel",
               name="Medusa",
               comment="",
               ids="0005686687",
               mode="none",
               action="spotify:album",
               data="xxxxx")

bdd.write_card(user="axel",
               name="Pompier",
               comment="",
               ids="0013377637",
               mode="none",
               action="spotify:album",
               data="xxxxx")

bdd.write_card(user="axel",
               name="Plouf",
               comment="",
               ids="0013350280",
               mode="none",
               action="spotify:album",
               data="xxxxx")

bdd.write_card(user="axel",
               name="Shaka Ponk",
               comment="",
               ids="0013375526",
               mode="none",
               action="spotify:album",
               data="xxxxx")

bdd.write_card(user="axel",
               name="Elefunk",
               comment="",
               ids="0015141595",
               mode="none",
               action="spotify:album",
               data="xxxxx")

bdd.write_card(user="axel",
               name="Mystico",
               comment="",
               ids="0013381471",
               mode="none",
               action="spotify:album",
               data="xxxxx")

bdd.write_card(user="axel",
               name="Nez-licoptere",
               comment="",
               ids="0015141710",
               mode="none",
               action="spotify:album",
               data="xxxxx")

bdd.write_card(user="axel",
               name="Lion",
               comment="",
               ids="0013375443",
               mode="none",
               action="spotify:album",
               data="xxxxx")

bdd.write_card(user="axel",
               name="Mr Oizo",
               comment="",
               ids="0013379816",
               mode="none",
               action="spotify:album",
               data="xxxxx")

bdd.write_card(user="axel",
               name="Mice Mobile",
               comment="",
               ids="0013377441",
               mode="none",
               action="spotify:album",
               data="xxxxx")

bdd.write_card(user="axel",
               name="Spirale",
               comment="",
               ids="0015141564",
               mode="none",
               action="spotify:album",
               data="xxxxx")

bdd.write_card(user="axel",
               name="Clowny",
               comment="",
               ids="0013379825",
               mode="none",
               action="spotify:album",
               data="xxxxx")

bdd.write_card(user="axel",
               name="Enaf",
               comment="",
               ids="0013209651",
               mode="none",
               action="spotify:album",
               data="xxxxx")

bdd.write_card(user="axel",
               name="Croc odile",
               comment="",
               ids="0013338744",
               mode="none",
               action="spotify:album",
               data="xxxxx")

bdd.write_card(user="axel",
               name="Mr Bato",
               comment="",
               ids="0013249903",
               mode="none",
               action="spotify:album",
               data="xxxxx")

bdd.write_card(user="axel",
               name="Lapin",
               comment="",
               ids="0013247975",
               mode="none",
               action="spotify:album",
               data="xxxxx")







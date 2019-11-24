
# Script that fill the database with all configs

from modules.cards_bdd.DbManager import DbManager

data_base = DbManager('https://bipbipzizik.firebaseio.com/', 'cards', 'config', 'serviceAccountKey.json')
data_base.delete('config')

# CARDS
# Command cards
data_base.write_config(
    app_name="For test purpose",
    app_owner="axel",
    app_id="template",
    sonos_server_ip="HHH.UUU.GGG.OOO",
    sonos_server_port="2017",
    room_name="Ginette",
    multi_read_mode="none",
    card_timeout="42")


data_base.write_config(
    app_name="Main house sonos",
    app_owner="axel",
    app_id="000000008e3c2b91",
    sonos_server_ip="192.168.1.80",
    sonos_server_port="5005",
    room_name="Salle de jeux",
    multi_read_mode="cancel",
    card_timeout="30")


data_base.write_config(
    app_name="Hugo's sonos",
    app_owner="axel",
    app_id="TODO",
    sonos_server_ip="192.168.1.80",
    sonos_server_port="5005",
    room_name="Hugo",
    multi_read_mode="cancel",
    card_timeout="30")





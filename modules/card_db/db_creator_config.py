

"""
Script that fill the database with all config
"""

from modules.card_db.db_manager import DbManager

DATABASE = DbManager('https://bipbipzizik.firebaseio.com/', 'prod', 'WriteKey.json')
DATABASE.delete('config_prod')

# CARDS
# Command cards
DATABASE.write_config(
    app_name="For test purpose",
    app_owner="axel",
    app_id="template",
    sonos_server_ip="HHH.UUU.GGG.OOO",
    sonos_server_port="2017",
    room_name="Ginette",
    multi_read_mode="none",
    card_timeout="42")


DATABASE.write_config(
    app_name="Main house sonos (black72)",
    app_owner="axel",
    app_id="000000008e3c2b91",
    sonos_server_ip="192.168.1.80",
    sonos_server_port="5005",
    room_name="Salon",
    multi_read_mode="cancel",
    card_timeout="30")


DATABASE.write_config(
    app_name="Hugo's (orange71)",
    app_owner="axel",
    app_id="00000000deec2469",
    sonos_server_ip="192.168.1.80",
    sonos_server_port="5005",
    room_name="Hugo",
    multi_read_mode="cancel",
    card_timeout="30")


DATABASE.write_config(
    app_name="Debug (naked74)",
    app_owner="axel",
    app_id="00000000bad90242",
    sonos_server_ip="192.168.1.80",
    sonos_server_port="5005",
    room_name="Billard",
    multi_read_mode="cancel",
    card_timeout="5")

DATABASE.write_config(
    app_name="Bertrand (nano)",
    app_owner="bertrand",
    app_id="0000000036c8d22e",
    sonos_server_ip="192.168.1.80",
    sonos_server_port="5005",
    room_name="Salon 3",
    multi_read_mode="cancel",
    card_timeout="30")

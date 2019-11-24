#
# BIPBIPZIZIK
# Manage application config
#
#


class AppConfig:

    def __init__(self, app_name, app_owner, app_id, sonos_server_ip, sonos_server_port,
                 room_name, multi_read_mode, card_timeout):

        # Application owner info
        self.cfg_app_name = app_name
        self.cfg_app_owner = app_owner

        # Application unique id (raspberry hardware serial)
        self.cfg_application_id = app_id



        # Server info for node-sonos-http-api
        self.cfg_sonos_server_ip = sonos_server_ip
        self.cfg_sonos_server_port = sonos_server_port

        # Room name designation
        # If you want to play on all your speakers, set roomName = ""
        self.cfg_room_name = room_name

        # Multi read mode
        # Define the action to do on successive read of the same card
        # Available modes:
        #  - supported: "cancel"
        #  - future: "next", "randomAlbum", "nextAlbum"
        self.cfg_multi_read_mode = multi_read_mode

        # Previous card memory duration in second
        self.cfg_card_timeout = card_timeout

    def print(self):
        """
        Function that print the application config
        :return:
        """

        print("Application config:")
        print(self.cfg_application_id)
        print(self.cfg_sonos_server_ip)
        print(self.cfg_sonos_server_port)
        print(self.cfg_room_name)
        print(self.cfg_multi_read_mode)
        print(self.cfg_card_timeout)


# For test purpose
def main():

    app_config = AppConfig(
        app_name="app_name",
        app_owner="app_owner",
        app_id="app_id",
        sonos_server_ip="sonos_server_ip",
        sonos_server_port="sonos_server_port",
        room_name="room_name",
        multi_read_mode="multi_read_mode",
        card_timeout="card_timeout")

    app_config.print()


if __name__ == "__main__":
    main()

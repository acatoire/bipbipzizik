

"""
BIPBIPZIZIK
Manage application config
"""


class AppConfig:
    """
    Class that hold the application configuration
    """

    def __init__(self, app_name, app_owner, app_id, sonos_server_ip, sonos_server_port,
                 room_name, multi_read_mode, card_timeout):
        """
        Constructor
        :param app_name:
        :param app_owner:
        :param app_id:
        :param sonos_server_ip:
        :param sonos_server_port:
        :param room_name:
        :param multi_read_mode:
        :param card_timeout:
        """

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

    def __str__(self):

        return (
            "Application config:\n" +
            "    - " + self.cfg_app_name + "\n" +
            "    - " + self.cfg_app_owner + "\n" +
            "    - " + self.cfg_application_id + "\n" +
            "    - " + self.cfg_sonos_server_ip + "\n" +
            "    - " + self.cfg_sonos_server_port + "\n" +
            "    - " + self.cfg_room_name + "\n" +
            "    - " + self.cfg_multi_read_mode + "\n" +
            "    - " + str(self.cfg_card_timeout)
                )

    def get_sonos_cmd(self, card_command):
        """
        Get the sonos command from the card command
        :param card_command:
        :return:
        """

        # Create address path
        sonos_addr = "http://" + self.cfg_sonos_server_ip + ':' + self.cfg_sonos_server_port

        # Create command line
        if self.cfg_room_name == '':
            # Command for global playing
            addr_with_room = sonos_addr + '/'
        else:
            # Command for local playing
            addr_with_room = sonos_addr + '/' + self.cfg_room_name + '/'

        return addr_with_room + card_command

    def print(self):
        """
        Function that print the application config
        :return:
        """

        print("Application config:")
        print("    - " + self.cfg_app_name)
        print("    - " + self.cfg_app_owner)
        print("    - " + self.cfg_application_id)
        print("    - " + self.cfg_sonos_server_ip)
        print("    - " + self.cfg_sonos_server_port)
        print("    - " + self.cfg_room_name)
        print("    - " + self.cfg_multi_read_mode)
        print("    - " + str(self.cfg_card_timeout))

"""
Bip bip object class
Interacting with Sonos using SoCo library
"""

import logging
import time

import soco
from soco.plugins.sharelink import ShareLinkPlugin
from bipbip import BipBip

logger = logging.getLogger("bipbip.soco")


class SoCoMode:
    """
    The Mode Container class for a bipbip
    """

    def __init__(self, modes: str or list):
        """
        Modes constructor from a single string or list of string
        @param modes:
        """
        self.modes = modes or []

    @property
    def clear_queue(self):
        """
        clear_queue
        :return:
        """
        return "ClearQueue" in self.modes

    @property
    def multi_read_cancel(self):  # TODO
        """
        multi_read_cancel
        :return:
        """
        return "MultiReadCancel" in self.modes

    @property
    def multi_read_db_random(self):  # TODO
        """
        multi_read_db_random
        :return:
        """
        return "MultiReadDbRandom" in self.modes

    @property
    def multi_read_next(self):  # TODO
        """
        multi_read_next
        :return:
        """
        return "MultiReadNext" in self.modes

    @property
    def multi_read_random(self):  # TODO
        """
        multi_read_random
        :return:
        """
        return "MultiReadRandom" in self.modes


class BipBipSoCo(BipBip):
    """
    The SoCo bipbip class
    """

    def __init__(self, parameters: dict, multi_read_timeout: int or float = 3):
        """
        :param parameters: Parameter dict, each BipBip can implement its own parameters
                  Generic parameters are:
                        name: The BipBip (card) Name
                        ids: list of ids that will run this BipBip
                        comment: BipBip comment
                        mode:
                        action: type of action to be executed
                        data: extra data related to the action
                        user: allowed user for the card
        :param multi_read_timeout: (optional) Value to consider a multi read, default 3s
        """
        super().__init__(parameters, multi_read_timeout)

        self.soco_mode = SoCoMode(self.mode)

        # TODO create a sonos singleton
        player_name = "TV"
        self.player = soco.discovery.by_name(player_name)

        if self.player:
            logger.info("Player %s is available @ %s", player_name, self.player.ip_address)
        else:
            logger.critical("No player found with name: %s!", player_name)
            return

    def start(self):
        """
        Execute of the bipbip
        :return:
        """
        super().execute()

        ####################################################
        # ## Cancel conditions
        ####################################################
        if self.locked and not self.action == "sonos-cmd":
            logger.warning("Action canceled because of the %ds multi read protection.", self.multi_read_timeout)
            return

        if not self.player:
            logger.critical("No player valid player configured during init, execution aborted!")
            return

        ####################################################
        # ####### Action
        ####################################################
        if self.player.is_playing_radio:
            logger.debug("Stop radio before continue")
            # Todo manage the radio kill if actually playing

        if self.soco_mode.clear_queue:
            self.player.stop()
            self.player.clear_queue()
            logger.debug("Clear sonos queue before execution")

        if self.action == "sonos-cmd":
            # Command action execution
            logger.debug("System will execute the sonos command: %s", self.data)
            if self.data == "play":
                self.player.play()
            elif self.data == "pause":
                self.player.pause()
            elif self.data == "stop":
                self.player.stop()

        elif self.action in ["spotify:track", "spotify:album", "spotify:playlist"]:
            # Spotify action execution
            spotify_mode = self.action.split(':')[1]
            spotify_link = f"{self.action}:{self.data}"
            logger.debug("System will execute on sonos the spotify %s: %s", spotify_mode, self.data)

            sharelink = ShareLinkPlugin(self.player)
            sharelink.add_share_link_to_queue(spotify_link)

            self.player.play()
            # Start the queue play from beginning
            # self.player.play_from_queue(0)

        elif self.action == "radio":
            # radio action execution
            # TODO to be implemented

        else:
            logger.critical('Action "%s" is not supported by BipBipSoCo!', self.action)
            return

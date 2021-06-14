"""
Bip bip object class
Interacting with Sonos using SoCo library
"""

import logging
import time
import soco0226 as soco
from bipbip import BipBip

from soco0226.plugins.sharelink import ShareLinkPlugin  #need merge of https://github.com/SoCo/SoCo/pull/838

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
        return True if "ClearQueue" in self.modes else False

    @property
    def multi_read_cancel(self):  # TODO
        return True if "MultiReadCancel" in self.modes else False

    @property
    def multi_read_db_random(self):  # TODO
        return True if "MultiReadDbRandom" in self.modes else False

    @property
    def multi_read_next(self):  # TODO
        return True if "MultiReadNext" in self.modes else False

    @property
    def multi_read_random(self):  # TODO
        return True if "MultiReadRandom" in self.modes else False


class BipBipSoCo(BipBip):
    """
    The SoCo bipbip class
    """

    def __init__(self, parameters: dict):
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
        """
        super().__init__(parameters)

        self.soco_mode = SoCoMode(self.mode)

        # TODO create a sonos singleton
        player_name = "Hugo"
        self.player = soco.discovery.by_name(player_name)

        if self.player:
            logger.info("Player %s is available @ %s", player_name, self.player.ip_address)
        else:
            logger.critical("No player found with name: %s!", player_name)
            return

    def execute(self):
        """
        Execute of the bipbip
        :return:
        """

        super().execute()

        if not self.player:
            logger.critical("No player valid player configured during init, execution aborted!")
            return

        if self.soco_mode.clear_queue:
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

        else:
            logger.critical('Action "%s" is not supported by BipBipSoCo!', self.action)
            return

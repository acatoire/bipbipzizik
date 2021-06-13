"""
Bip bip object class
Interacting with Sonos using SoCo library
"""

import logging
import time
import soco
from bipbip import BipBip


logger = logging.getLogger("bipbip.soco")


class BipBipSoCo(BipBip):
    """
    The SoCo bipbip class
    """

    def execute(self):
        """
        Execute of the bipbip
        :return:
        """
        self._execution_log.append(time.time())
        logger.info("Execute the SoCo bipbip: %s", self.name)

        # TODO create a sonos singleton
        player_name = "Salon"
        player = soco.discovery.by_name(player_name)

        if not player:
            logger.critical("No player found with name: %s, execution aborted!", player_name)
            return

        logger.info("Player {player_name} is available @ %s", player.ip_address)

        if self.action == "sonos-cmd":
            logger.info("System will execute the sonos command: %s", self.data)
            if self.data == "play":
                player.play()
            elif self.data == "pause":
                player.pause()
            elif self.data == "stop":
                player.stop()

        if self.action == "spotify:track":
            logger.info("System will execute on sonos the spotify track: %s", self.data)

            # FIXME playing info are not printed on Sonos probably linked do https://github.com/SoCo/SoCo/issues/557
            spotify_uri = f"x-sonos-spotify:spotify%3atrack%3a{self.data}?sid=9&flags=8224&sn=1"
            player.play_uri(spotify_uri)

        if self.action == "spotify:album":
            logger.info("System will execute playe on sonos the spotify track: %s", self.data)

            # FIXME not working apparently only accept track linked to https://github.com/SoCo/SoCo/issues/762
            spotify_uri = f"x-sonos-spotify:spotify%3aalbum%3a{self.data}?sid=9&flags=8224&sn=1"
            player.play_uri(spotify_uri)

        if self.action == "spotify:playlist":
            logger.info("System will execute playe on sonos the spotify track: %s", self.data)

            # FIXME not working apparently only accept track linked to https://github.com/SoCo/SoCo/issues/762
            spotify_uri = f"x-sonos-spotify:spotify%3aplaylist%3a{self.data}?sid=9&flags=8224&sn=1"
            player.play_uri(spotify_uri)

        else:
            logger.critical('Action "%s" is not supported by BipBipSoCo!', self.action)
            return

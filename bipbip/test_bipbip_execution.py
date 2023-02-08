"""
Card execution tests
"""

import logging
from time import sleep
from unittest import TestCase
from unittest.mock import MagicMock
from bipbip_soco import BipBipSoCo

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("bipbip.soco")
logger.setLevel(level=logging.DEBUG)
# logging.config.fileConfig('logging_unittest.yaml')  TODO understand logging config

REAL = False


class TestBipBip(TestCase):
    """
    TestBipBip
    """

    @classmethod
    def setUpClass(cls):
        pass

    def test_execute_soco_play(self):
        """
        test_execute_soco_play
        :return:
        """
        param_dict = dict(
            name='play',
            action='sonos-cmd',
            data='play',
        )

        bip_bip = BipBipSoCo(param_dict, 'TV')

        if not REAL:
            bip_bip.player.play = MagicMock()

        bip_bip.execute()

        if not REAL:
            bip_bip.player.play.assert_called()

    def test_execute_soco_pause(self):
        """
        test_execute_soco_pause
        :return:
        """
        param_dict = dict(
            name='pause',
            action='sonos-cmd',
            data='pause',
        )

        bip_bip = BipBipSoCo(param_dict)
        bip_bip.execute()

    def test_execute_soco_stop(self):
        """
        test_execute_soco_stop
        :return:
        """
        param_dict = dict(
            name='stop',
            action='sonos-cmd',
            data='stop',
        )

        bip_bip = BipBipSoCo(param_dict)
        bip_bip.execute()

    def test_execute_soco_spotify_track(self):
        """
        test_execute_soco_spotify_track
        :return:
        """
        param_dict = dict(
            name='Les petits poissons',
            action='spotify:track',
            data='35VKLRwEjuR5IuFyGqjMaf',
            mode='ClearQueue',
        )

        bip_bip = BipBipSoCo(param_dict)
        bip_bip.execute()

    def test_execute_soco_spotify_album(self):
        """
        test_execute_soco_spotify_album
        :return:
        """
        param_dict = dict(
            name='Caravan Palace',
            action='spotify:album',
            data='3qU4wXm0Qngbtnr5PiLbFX',
            mode='ClearQueue',
        )

        bip_bip = BipBipSoCo(param_dict)
        bip_bip.execute()

    def test_execute_soco_spotify_playlist(self):
        """
        test_execute_soco_spotify_playlist
        :return:
        """
        param_dict = dict(
            name='Pirate',
            action='spotify:playlist',
            data='3YwpelPVPBfZLvltQPdTHY',
            mode='ClearQueue',
        )

        bip_bip = BipBipSoCo(param_dict)
        bip_bip.execute()

    def test_execute_soco_radio(self):
        """
        test_execute_soco_radio
        TODO not implemented
        :return:
        """
        param_dict = dict(
            name='France Inter',
            action='radio',
            data='france inter',
            mode='ClearQueue',
        )

        bip_bip = BipBipSoCo(param_dict)
        bip_bip.execute()

    def test_execute_soco_spotify_multi_read(self):
        param_dict = dict(
            name='Les petits poissons',
            action='spotify:track',
            data='35VKLRwEjuR5IuFyGqjMaf',
            mode='ClearQueue',
        )
        timeout = 1

        bip_bip = BipBipSoCo(param_dict, multi_read_timeout=timeout)
        if not REAL:
            bip_bip.player.clear_queue = MagicMock()
            bip_bip.sharelink.add_share_link_to_queue = MagicMock()
            bip_bip.player.play = MagicMock()

        bip_bip.execute()

        if not REAL:
            bip_bip.player.clear_queue.assert_called()
            bip_bip.sharelink.add_share_link_to_queue.assert_called_with("spotify:track:35VKLRwEjuR5IuFyGqjMaf")
            bip_bip.player.play.assert_called()

        sleep(0.1)

        if not REAL:
            bip_bip.player.clear_queue.reset_mock()
            bip_bip.sharelink.add_share_link_to_queue.reset_mock()
            bip_bip.player.play.reset_mock()

        bip_bip.execute()
        if not REAL:
            bip_bip.player.clear_queue.assert_not_called()
            bip_bip.sharelink.add_share_link_to_queue.assert_not_called()
            bip_bip.player.play.assert_not_called()

        sleep(0.1)

        if not REAL:
            bip_bip.player.clear_queue.reset_mock()
            bip_bip.sharelink.add_share_link_to_queue.reset_mock()
            bip_bip.player.play.reset_mock()

        bip_bip.execute()

        if not REAL:
            bip_bip.player.clear_queue.assert_not_called()
            bip_bip.sharelink.add_share_link_to_queue.assert_not_called()
            bip_bip.player.play.assert_not_called()

        sleep(timeout)

        if not REAL:
            bip_bip.player.clear_queue.reset_mock()
            bip_bip.sharelink.add_share_link_to_queue.reset_mock()
            bip_bip.player.play.reset_mock()

        bip_bip.execute()

        if not REAL:
            bip_bip.player.clear_queue.assert_called()
            bip_bip.sharelink.add_share_link_to_queue.assert_called_with("spotify:track:35VKLRwEjuR5IuFyGqjMaf")
            bip_bip.player.play.assert_called()

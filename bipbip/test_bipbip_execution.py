

import logging
from time import sleep
from unittest import TestCase
from unittest.mock import MagicMock
from bipbip_soco import BipBipSoCo

logging.basicConfig(level=logging.INFO)
# logging.config.fileConfig('logging_unittest.yaml')  TODO understand logging config

REAL = False


class TestBipBip(TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    def test_execute_soco_play(self):
        param_dict = dict(
            name='play',
            action='sonos-cmd',
            data='play',
        )

        bip_bip = BipBipSoCo(param_dict)

        if not REAL:
            bip_bip.player.play = MagicMock()

        bip_bip.execute()

        if not REAL:
            bip_bip.player.play.assert_called()

    def test_execute_soco_pause(self):
        param_dict = dict(
            name='pause',
            action='sonos-cmd',
            data='pause',
        )

        bip_bip = BipBipSoCo(param_dict)
        bip_bip.execute()

    def test_execute_soco_stop(self):
        param_dict = dict(
            name='stop',
            action='sonos-cmd',
            data='stop',
        )

        bip_bip = BipBipSoCo(param_dict)
        bip_bip.execute()

    def test_execute_soco_spotify_track(self):
        param_dict = dict(
            name='Les petits poissons',
            action='spotify:track',
            data='35VKLRwEjuR5IuFyGqjMaf',
            mode='ClearQueue',
        )

        bip_bip = BipBipSoCo(param_dict)
        bip_bip.execute()

    def test_execute_soco_spotify_album(self):
        param_dict = dict(
            name='Caravan Palace',
            action='spotify:album',
            data='3qU4wXm0Qngbtnr5PiLbFX',
        )

        bip_bip = BipBipSoCo(param_dict)
        bip_bip.execute()

    def test_execute_soco_spotify_playlist(self):
        param_dict = dict(
            name='Pirate',
            action='spotify:playlist',
            data='3YwpelPVPBfZLvltQPdTHY',
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

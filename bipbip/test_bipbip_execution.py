

import logging
from unittest import TestCase
from bipbip_soco import BipBipSoCo

logging.basicConfig(level=logging.INFO)
# logging.config.fileConfig('logging_unittest.yaml')  TODO understand logging config


class TestBipBip(TestCase):

    def test_execute_soco_play(self):
        param_dict = dict(
            name='play',
            action='sonos-cmd',
            data='play',
        )

        bip_bip = BipBipSoCo(param_dict)
        bip_bip.execute()

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

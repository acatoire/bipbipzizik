

import logging
from unittest import TestCase
from bipbip import BipBip

logging.basicConfig(level=logging.INFO)


class TestBipBip(TestCase):
    def test_parameters(self):
        param_dict = dict(
            name='name',
            ids='ids',
            comment='comment',
            mode='mode',
            action='action',
            data='data',
            user='user',
        )

        bip_bip = BipBip(param_dict)
        self.assertEqual("name", bip_bip.name)
        self.assertEqual("ids", bip_bip.ids)
        self.assertEqual("comment", bip_bip.comment)
        self.assertEqual("mode", bip_bip.mode)
        self.assertEqual("action", bip_bip.action)
        self.assertEqual("data", bip_bip.data)
        self.assertEqual("user", bip_bip.user)

    def test_parameters_failed(self):
        param_dict = dict(
            name='name',
        )

        bip_bip = BipBip(param_dict)
        self.assertEqual("name", bip_bip.name)
        self.assertEqual(None, bip_bip.ids)

    def test_execute(self):
        param_dict = dict(
            name='name',
        )

        bip_bip = BipBip(param_dict)
        bip_bip.execute()
        self.assertEqual(1, len(bip_bip.execution_log))
        bip_bip.execute()
        self.assertEqual(2, len(bip_bip.execution_log))

import unittest
import os
from tests.config.definitions import ROOT_DIR
from app.app import App
from sdk.moveapps_io import MoveAppsIo
import pandas as pd
import movingpandas as mpd


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        os.environ['APP_ARTIFACTS_DIR'] = os.path.join(ROOT_DIR, 'tests/resources/output')
        self.sut = App(moveapps_io=MoveAppsIo())

    def test_app_returns_input(self):
        # prepare
        expected: mpd.TrajectoryCollection = pd.read_pickle(os.path.join(ROOT_DIR, 'tests/resources/app/input2.pickle'))
        config: dict = {}

        # execute
        actual = self.sut.execute(data=expected, config=config)

        # verif
        self.assertEqual(expected, actual)

    def test_app_config_mapping(self):
        # prepare
        config = {
            "line_width": 10,
            "legend": True
        }

        # execute
        actual = self.sut.map_config(config=config)

        # verify
        self.assertEqual(10, actual.line_width)
        self.assertTrue(actual.with_legend)

    def test_app_config_mapping_defaults(self):
        # prepare
        config = {}

        # execute
        actual = self.sut.map_config(config=config)

        # verify
        self.assertEqual(5, actual.line_width)
        self.assertFalse(actual.with_legend)

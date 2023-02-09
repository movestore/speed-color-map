from sdk.moveapps_spec import hook_impl
from movingpandas import TrajectoryCollection
import logging
from dataclasses import dataclass


@dataclass
class AppConfig:
    line_width: int
    with_legend: bool


class App(object):

    def __init__(self, moveapps_io):
        self.moveapps_io = moveapps_io

    @staticmethod
    def map_config(config: dict):
        return AppConfig(
            line_width=config['line_width'] if 'line_width' in config else 5,
            with_legend=config['legend'] if 'legend' in config else False
        )

    @hook_impl
    def execute(self, data: TrajectoryCollection, config: dict) -> TrajectoryCollection:
        app_config = self.map_config(config=config)
        data.add_speed(overwrite=True)
        plot = data.plot(
            column="speed",
            linewidth=app_config.line_width,
            capstyle='round',
            legend=app_config.with_legend
        )
        plot.figure.savefig(self.moveapps_io.create_artifacts_file('plot.png'))
        return data

import src.config.configs.divisor as divisor_configs
import src.config.configs.gradient as gradient_configs

from src.track.waypoint_metrics import WaypointMetrics
from src.speed.speed_calculator import SpeedCalculator


class Track:
    def __init__(self, name, waypoints, config_name):
        self.name = name
        self.waypoints = waypoints
        self.config_name = config_name

        self.gradients_config = gradient_configs.configs[config_name]
        self.divisor_config = divisor_configs.configs[config_name]

        assert self.gradients_config is not None
        assert self.divisor_config is not None

        self.waypoint_metrics = WaypointMetrics(waypoints, self.gradients_config)
        self.speed_calculator = SpeedCalculator(self.waypoint_metrics, [1.33, 2.67, 4])
        # self.divisor = TrackDivisor(waypoints, self.waypoint_metrics, self.divisor_config)




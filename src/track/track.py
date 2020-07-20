import src.config.configs.gradient as gradient_configs
from src.angle_calculator import AngleCalculator

from src.track.waypoint_metrics import WaypointMetrics
from src.speed.speed_calculator import SpeedCalculator


class Track:
    def __init__(self, name, waypoints, config_name):
        self.name = name
        self.waypoints = waypoints
        self.config_name = config_name

        self.gradients_config = gradient_configs.configs[config_name]

        # Min and Max X and Y
        _x_coords = [x[0] for x in waypoints]
        _y_coords = [y[1] for y in waypoints]

        self.min_x = min(_x_coords)
        self.min_y = min(_y_coords)

        self.max_x = max(_x_coords)
        self.max_y = max(_y_coords)

        assert self.gradients_config is not None

        self.waypoint_metrics = WaypointMetrics(waypoints, self.gradients_config)
        self.speed_calculator = SpeedCalculator(self.waypoint_metrics, [1.33, 2.67, 4])

        self.angle_calculator = AngleCalculator(waypoints, self.waypoint_metrics)
        # self.divisor = TrackDivisor(waypoints, self.waypoint_metrics, self.divisor_config)



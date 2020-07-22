import math

import src.config.configs.gradient as gradient_configs
from src.track.waypoint import Waypoint


class Track:
    def __init__(self, name, waypoints, track_width, config_name):
        self.name = name
        self.raw_waypoint_data = waypoints
        self.config_name = config_name
        self.track_width = track_width

        self.gradients_config = gradient_configs.configs[config_name]

        self.waypoints = self.process_raw_waypoints_data(waypoints)

        # Min and Max X and Y
        _x_coords = [x[0] for x in waypoints]
        _y_coords = [y[1] for y in waypoints]

        self.min_x = min(_x_coords)
        self.min_y = min(_y_coords)

        self.max_x = max(_x_coords)
        self.max_y = max(_y_coords)

        self.smallest_radius = min([x.circle_radius for x in self.waypoints])

        self.update_estimated_speeds(self.smallest_radius, [1.33, 2.67, 4])
        assert self.gradients_config is not None

        # self.speed_calculator = SpeedCalculator(self.waypoint_metrics, [1.33, 2.67, 4])

        # self.angle_calculator = AngleCalculator(waypoints, self.waypoint_metrics)
        # self.divisor = TrackDivisor(waypoints, self.waypoint_metrics, self.divisor_config)

    def process_raw_waypoints_data(self, raw_waypoints):
        waypoints = []
        length = len(raw_waypoints)

        for i, wp in enumerate(raw_waypoints):
            wp = Waypoint(i, wp[0], wp[1])
            next_index, prev_index = i - self.gradients_config.waypoint_lookbehind, (
                        i + self.gradients_config.waypoint_lookahead) % length
            wp.update_circle_metrics(raw_waypoints[prev_index], raw_waypoints[next_index])
            waypoints.append(wp)

        return waypoints

    def update_estimated_speeds(self, smallest_radius, possible_speeds, constant=math.inf):
        if constant == math.inf:
            constant = min(possible_speeds) / smallest_radius ** 0.5
        for wp in self.waypoints:
            wp.update_speed(possible_speeds, constant)

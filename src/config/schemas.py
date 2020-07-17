class GradientConfig:
    def __init__(self, waypoint_lookahead=1, waypoint_lookbehind=1):
        self.waypoint_lookahead = waypoint_lookahead
        self.waypoint_lookbehind = waypoint_lookbehind


class SpeedConfig:
    def __init__(self, possible_speeds: list):
        self.possible_speeds = possible_speeds
        self.speed_action_space_size = len(possible_speeds)
        self.min_speed = min(possible_speeds)


class AngleConfig:
    def __init__(self):
        self.axle_distance = 0.165

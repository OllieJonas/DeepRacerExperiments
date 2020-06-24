from src.config_schema.divisor_config import DivisorConfig
from src.track_divider.divisor import TrackDivisor


class Track:
    def __init__(self, name, waypoints, divisor_config: DivisorConfig, debug=False):
        self.name = name
        self.waypoints = waypoints
        self.num_waypoints = len(waypoints)

        self.track_divisor = TrackDivisor(divisor_config, debug)

        self.narrow_gradients, self.wide_gradients = self.track_divisor.parse_track()

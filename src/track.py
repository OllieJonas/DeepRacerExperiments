from src.track_divider.divisor import TrackDivisor


class Track:
    def __init__(self, name, waypoints, track_divisor: TrackDivisor):
        self.name = name
        self.waypoints = waypoints
        self.track_divisor = track_divisor

        self.narrow_gradients, self.wide_gradients = track_divisor.parse_track()

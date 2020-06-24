from src.config.schemas import DivisorConfig
from src.waypoint_metrics import WaypointMetrics


class TrackDivisor:
    def __init__(self, waypoints, waypoint_metrics: WaypointMetrics, config: DivisorConfig, debug=False):
        """
        :param config: The config_schema to use
        :param debug: Toggles debugging
        """

        self.waypoints = waypoints
        self.num_waypoints = len(waypoints)

        self.waypoints_metrics = waypoint_metrics

        self.narrow_gradient_threshold = config.narrow_gradient_threshold
        self.wide_gradient_threshold = config.wide_gradient_threshold
        self.use_wide_gradient = config.use_wide_gradient

        self.distance_threshold = config.distance_threshold

        self.pre_corner_range = config.pre_corner_range
        self.post_corner_range = config.post_corner_range

        self.debug = debug

        self.straights = []
        self.corners = []
        self.pre_corners = []
        self.highlighted = [self.waypoints[x] for x in range(0, 0)]

        self.parse_track()

    def parse_track(self):
        # Gradients
        for i in range(0, self.num_waypoints):

            d_narrow_gradient = self.waypoints_metrics.d_narrow_gradients[i]
            d_wide_gradient = self.waypoints_metrics.d_wide_gradients[i]

            distance = self.waypoints_metrics.distances[i]

            # Super slow
            if (d_narrow_gradient > self.narrow_gradient_threshold or
                (d_wide_gradient > self.wide_gradient_threshold and self.use_wide_gradient)) \
                    and distance > self.distance_threshold:

                self.corners.append(i)

            # Medium speed
            elif (d_narrow_gradient > self.narrow_gradient_threshold * 2 or
                  (d_wide_gradient > self.wide_gradient_threshold * 2 and self.use_wide_gradient)) \
                    and distance > self.distance_threshold * 2:

                self.pre_corners.append(i)

            # Full speed ahead!
            else:
                self.straights.append(i)

        # Preparation for entering red zones (ie. corners)
        # Less slow leaving a corner
        for entry in self.corners:
            for i in range(0, self.post_corner_range):
                curr = entry - i

                if curr not in self.corners:
                    self.pre_corners.append(curr)
                    if curr in self.straights:  # This should always be true
                        self.straights.remove(curr)

        # Slow down upon entering a corner
        for entry in self.corners:
            for i in range(0, self.pre_corner_range):
                curr = entry - i

                if curr not in self.corners:
                    self.pre_corners.append(curr)
                    if curr in self.straights:  # This should always be true
                        self.straights.remove(curr)

    def debug_print(self, colour, i, narrow_gradient, prev_narrow_gradient, prev_waypoint, prev_wide_gradient, waypoint,
                    wide_gradient):
        if self.debug:
            print("{} - Index: {} Waypoint: {} Prev Waypoint: {} Narrow Gradient: {} Wide Gradient: {}"
                  .format(colour, i, waypoint, prev_waypoint, narrow_gradient - prev_narrow_gradient,
                          wide_gradient - prev_wide_gradient))

    def build_lines(self):
        """
        Takes the indexes created in the parse_track function and splits them into 3 lists, using data from the
        waypoints.

        :return: A tuple of lists, in the order straights, corners, pre_corners
        """
        straights = []
        corners = []
        pre_corners = []

        for i in self.straights:
            straights.append(self.waypoints[i])

        for i in self.corners:
            corners.append(self.waypoints[i])

        for i in self.pre_corners:
            pre_corners.append(self.waypoints[i])

        return straights, corners, pre_corners

    def print(self):
        """
        Debug printing, currently prints all the way-points.
        """
        [print(x) for x in self.waypoints]

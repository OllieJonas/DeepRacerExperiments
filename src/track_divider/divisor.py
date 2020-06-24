from src import util
from src.track_divider.divisor_config import DivisorConfig


class TrackDivisor:

    def __init__(self, config: DivisorConfig, debug=False):
        """
        :param config: The config to use
        :param debug: Toggles debugging
        """

        self.waypoints = config.waypoints
        self.num_waypoints = len(self.waypoints)

        self.narrow_gradient_threshold = config.narrow_gradient_threshold
        self.wide_gradient_threshold = config.wide_gradient_threshold
        self.use_wide_gradient = config.use_wide_gradient

        self.distance_threshold = config.distance_threshold

        self.pre_corner_range = config.pre_corner_range
        self.post_corner_range = config.post_corner_range

        self.waypoint_lookahead = config.waypoint_lookahead
        self.waypoint_lookbehind = config.waypoint_lookbehind

        self.debug = debug

        self.straights = []
        self.corners = []
        self.pre_corners = []
        self.highlighted = [self.waypoints[x] for x in range(0, 0)]

        self.parse_track()

    def parse_track(self):
        prev_narrow_gradient = 0
        prev_wide_gradient = 0

        # Gradients
        for i in range(0, self.num_waypoints):
            waypoint = self.waypoints[i]

            prev_waypoint = self.waypoints[max(0, i - self.waypoint_lookbehind)]
            next_waypoint = self.waypoints[min(self.num_waypoints - 1, i + self.waypoint_lookahead)]

            wide_gradient = util.calculate_gradient(next_waypoint, prev_waypoint)
            narrow_gradient = util.calculate_gradient(waypoint, next_waypoint)
            distance = util.distance_between(waypoint, next_waypoint)

            d_narrow_gradient = abs(narrow_gradient - prev_narrow_gradient)
            d_wide_gradient = abs(wide_gradient - prev_wide_gradient)

            # Super slow
            if (d_narrow_gradient > self.narrow_gradient_threshold or
                (d_wide_gradient > self.wide_gradient_threshold and self.use_wide_gradient)) \
                    and distance > self.distance_threshold:

                if self.debug:
                    self.debug_print("RED", i, narrow_gradient, prev_narrow_gradient, prev_waypoint,
                                     prev_wide_gradient,
                                     waypoint, wide_gradient)
                self.corners.append(i)

            # Medium speed
            elif (d_narrow_gradient > self.narrow_gradient_threshold * 2 or
                  (d_wide_gradient > self.wide_gradient_threshold * 2 and self.use_wide_gradient)) \
                    and distance > self.distance_threshold * 2:
                if self.debug:
                    self.debug_print("YELLOW", i, narrow_gradient, prev_narrow_gradient, prev_waypoint,
                                     prev_wide_gradient,
                                     waypoint, wide_gradient)
                self.pre_corners.append(i)

            # Full speed ahead!
            else:
                self.debug_print("GREEN", i, narrow_gradient, prev_narrow_gradient, prev_waypoint,
                                 prev_wide_gradient,
                                 waypoint, wide_gradient)
                self.straights.append(i)

            prev_narrow_gradient = narrow_gradient
            prev_wide_gradient = wide_gradient

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

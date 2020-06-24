from src.config.schemas import GradientConfig
import src.main.util as util


class WaypointMetrics:

    def __init__(self, waypoints, config: GradientConfig):
        self.waypoints = waypoints
        self.num_waypoints = len(waypoints)
        self.config = config

        self.wide_gradients = []
        self.narrow_gradients = []

        self.d_wide_gradients = []
        self.d_narrow_gradients = []

        self.distances = []

        self.calculate_metrics()

    def calculate_metrics(self):
        prev_narrow_gradient = 0
        prev_wide_gradient = 0

        for i in range(0, self.num_waypoints):
            curr = self.waypoints[i]

            prev_wide_waypoint = self.waypoints[(i - self.config.waypoint_lookbehind)]
            next_wide_waypoint = self.waypoints[(i + self.config.waypoint_lookahead) % self.num_waypoints]

            next_narrow_waypoint = self.waypoints[(i + 1) % self.num_waypoints]

            # Calculate distance between curr and next waypoint
            curr_distance = util.distance_between(curr, next_narrow_waypoint)

            # Calculate current gradients
            curr_wide_gradient = util.calculate_gradient(prev_wide_waypoint, next_wide_waypoint)
            curr_narrow_gradient = util.calculate_gradient(curr, next_narrow_waypoint)

            # Calculate difference between gradients
            d_curr_wide_gradient = abs(curr_wide_gradient - prev_wide_gradient)
            d_curr_narrow_gradient = abs(curr_narrow_gradient - prev_narrow_gradient)

            # Add to list
            self.distances.append(curr_distance)

            # Add them to a list of gradients
            self.wide_gradients.append((curr, curr_wide_gradient))
            self.narrow_gradients.append((curr, curr_narrow_gradient))

            # Add them to list
            self.d_wide_gradients.append(d_curr_wide_gradient)
            self.d_narrow_gradients.append(d_curr_narrow_gradient)

            # Assign prev wide gradients
            prev_wide_gradient = curr_wide_gradient
            prev_narrow_gradient = curr_narrow_gradient

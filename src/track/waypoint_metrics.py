from src.config.schemas import GradientConfig
import src.main.util as util


class WaypointMetrics:
    def __init__(self, waypoints, config: GradientConfig):
        self.waypoints = waypoints
        self.num_waypoints = len(waypoints)
        self.config = config

        self.distances = []

        self.circle_metrics = self.calculate_distances()
        self.gradients = self.calculate_gradients()

        self.smallest_radius = min(x['radius'] for x in self.circle_metrics)

    def calculate_distances(self):
        lookahead = self.config.waypoint_lookahead
        lookbehind = self.config.waypoint_lookbehind

        circle_metrics = []
        for i in range(0, self.num_waypoints):
            curr = self.waypoints[i % self.num_waypoints]
            prv = self.waypoints[(i - lookbehind) % self.num_waypoints]
            nxt = self.waypoints[(i + lookahead) % self.num_waypoints]

            circle_metric = util.circle_metrics(curr, prv, nxt)
            circle_metrics.append(circle_metric)
        return circle_metrics

    def calculate_gradients(self):
        lookahead = self.config.waypoint_lookahead
        lookbehind = self.config.waypoint_lookbehind

        gradient_metrics = []

        for i in range(0, self.num_waypoints):
            curr = self.waypoints[i % self.num_waypoints]
            prv = self.waypoints[(i - lookbehind) % self.num_waypoints]
            nxt = self.waypoints[(i + lookahead) % self.num_waypoints]

            wide_gradient_metric = util.calculate_gradient(nxt, prv)
            prev_gradient_metric = util.calculate_gradient(curr, prv)
            next_gradient_metric = util.calculate_gradient(nxt, curr)

            gradient_metric = {
                "wide": wide_gradient_metric,
                "prev": prev_gradient_metric,
                "next": next_gradient_metric
            }

            gradient_metrics.append(gradient_metric)
        return gradient_metrics

    def debug_print(self):
        for i in range(0, self.num_waypoints):
            print("WAYPOINT {}".format(i))
            print("Circle Metrics: \n {}".format(self.circle_metrics[i]))
            print("Gradients: \n {}".format(self.gradients[i]))
            print()

import numpy as np

from src.config.schemas import GradientConfig
import src.main.util as util


def _circle_metrics(coord1, coord2, coord3, debug=False):
    """
    Gives metrics about a circle (radius, equation, etc.) based on 3 given points.

    Calculated from here: http://ambrsoft.com/TrigoCalc/Circle3D.htm
    :param coord1:
    :param coord2:
    :param coord3:
    :param debug:
    :return:
    """
    x1, y1 = [a for a in coord1]
    x2, y2 = [a for a in coord2]
    x3, y3 = [a for a in coord3]

    x1_sqr, x2_sqr, x3_sqr = pow(x1, 2), pow(x2, 2), pow(x3, 2)
    y1_sqr, y2_sqr, y3_sqr = pow(y1, 2), pow(y2, 2), pow(y3, 2)

    det_a = x1 * (y2 - y3) - y1 * (x2 - x3) + x2 * y3 - x3 * y2
    det_b = (x1_sqr + y1_sqr) * (y3 - y2) + (x2_sqr + y2_sqr) * (y1 - y3) + (x3_sqr + y3_sqr) * (y2 - y1)
    det_c = (x1_sqr + y1_sqr) * (x2 - x3) + (x2_sqr + y2_sqr) * (x3 - x1) + (x3_sqr + y3_sqr) * (x1 - x2)
    det_d = (x1_sqr + y1_sqr) * ((x3 * y2) - (x2 * y3)) + (x2_sqr + y2_sqr) * ((x1 * y3) - (x3 * y1)) + (
                x3_sqr + y3_sqr) * ((x2 * y1) - (x1 * y2))

    if debug:
        print("A Det: {}. B Det: {}. C Det: {}. D Det: {}".format(det_a, det_b, det_c, det_d))

    if det_a == 0:
        centre_x, centre_y = None, None
        radius = np.Inf
    else:
        centre_x, centre_y = -1 * (det_b / (2 * det_a)), -1 * (det_c / (2 * det_a))
        radius = np.sqrt((det_b ** 2 + det_c ** 2 - 4 * det_a * det_d) / (4 * det_a ** 2))

    return {
        "coords": [coord1, coord2, coord3],
        "centre": (centre_x, centre_y),
        "radius": radius
    }


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

            circle_metric = _circle_metrics(curr, prv, nxt)
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

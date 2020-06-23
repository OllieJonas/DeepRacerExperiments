import matplotlib.pyplot as plt
import math

import waypoints_list as wp
import util

class TrackDivisor:

    def __init__(self, waypoints, narrow_gradient_threshold=0.3, wide_gradient_threshold=0.1, debug=False):
        self.waypoints = waypoints
        self.num_waypoints = len(waypoints)
        self.narrow_gradient_threshold = narrow_gradient_threshold
        self.wide_gradient_threshold = wide_gradient_threshold
        self.debug = debug

        self.straights = []
        self.corners = []
        self.pre_corners = []

        self.parse_track()

    def parse_track(self):
        gradients = []
        prev_narrow_gradient = 0
        prev_wide_gradient = 0

        for i in range(0, self.num_waypoints):
            waypoint = self.waypoints[i]
            prev_waypoint = self.waypoints[max(0, i - 2)]
            next_waypoint = self.waypoints[min(self.num_waypoints - 1, i + 2)]

            wide_gradient = util.calculate_gradient(next_waypoint, prev_waypoint)
            narrow_gradient = util.calculate_gradient(waypoint, next_waypoint)

            gradients.append(narrow_gradient)

            if abs((narrow_gradient - prev_narrow_gradient)) > self.narrow_gradient_threshold \
                    or abs(wide_gradient - prev_wide_gradient) > self.wide_gradient_threshold:
                print(waypoint, prev_waypoint, narrow_gradient, wide_gradient)
                self.corners.append(waypoint)
            else:
                self.straights.append(waypoint)

            prev_narrow_gradient = narrow_gradient
            prev_wide_gradient = wide_gradient
        pass

    def print(self):
        """
        Debug printing, currently prints all the way-points.
        """
        [print(x) for x in self.waypoints]

    def show_graph(self):
        """
        Displays a graph of the points.
        """
        straights, = plt.plot([x[0] for x in self.straights], [y[1] for y in self.straights], 'bo')
        corners, = plt.plot([x[0] for x in self.corners], [y[1] for y in self.corners], 'ro')
        pre_corners, = plt.plot([x[0] for x in self.pre_corners], [y[1] for y in self.pre_corners], 'go')

        # Graph Config
        straights.set_antialiased(False)
        corners.set_antialiased(False)
        pre_corners.set_antialiased(False)

        plt.xlabel('X Coordinates')
        plt.ylabel('Y Coordinates')

        plt.show()

        if self.debug:
            self.print()


if __name__ == "__main__":
    divisor = TrackDivisor(wp.REINVENT_2018, debug=False)
    divisor.show_graph()

import matplotlib.pyplot as plt
import math
import waypoints_list as wp
import util


class TrackDivisor:

    def __init__(self, waypoints, narrow_gradient_threshold=0.125, wide_gradient_threshold=0.3, pre_corner_range=3, debug=False):
        """

        :param waypoints:
        :param narrow_gradient_threshold:
        :param wide_gradient_threshold:
        :param pre_corner_range:
        :param debug:


        """
        self.waypoints = waypoints
        self.num_waypoints = len(waypoints)
        self.narrow_gradient_threshold = narrow_gradient_threshold
        self.wide_gradient_threshold = wide_gradient_threshold
        self.pre_corner_range = pre_corner_range
        self.debug = debug

        self.straights = []
        self.corners = []
        self.pre_corners = []

        self.parse_track()

    def parse_track(self):
        prev_narrow_gradient = 0
        prev_wide_gradient = 0

        for i in range(0, self.num_waypoints):
            waypoint = self.waypoints[i]
            prev_waypoint = self.waypoints[max(0, i - 1)]
            next_waypoint = self.waypoints[min(self.num_waypoints - 1, i + 1)]

            wide_gradient = util.calculate_gradient(next_waypoint, prev_waypoint)
            narrow_gradient = util.calculate_gradient(waypoint, next_waypoint)

            if abs((narrow_gradient - prev_narrow_gradient)) > self.narrow_gradient_threshold \
                    or abs(wide_gradient - prev_wide_gradient) > self.wide_gradient_threshold:
                self.corners.append(i)
            else:
                self.straights.append(i)

            print("Waypoint: {} Prev Waypoint: {} Narrow Gradient: {} Wide Gradient: {}"
                  .format(waypoint, prev_waypoint, narrow_gradient, wide_gradient))

            prev_narrow_gradient = narrow_gradient
            prev_wide_gradient = wide_gradient

        for entry in self.corners:
            for i in range(0, self.pre_corner_range):
                curr = entry - i

                if curr not in self.corners:
                    self.pre_corners.append(curr)
                    if curr in self.straights:  # This should always be true
                        self.straights.remove(curr)

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

    def show_graph(self):
        """
        Displays a graph of the points.
        """

        straights, corners, pre_corners = self.build_lines()

        straights_line, = plt.plot([x[0] for x in straights], [y[1] for y in straights], 'o', color='lime')
        corners_line, = plt.plot([x[0] for x in corners], [y[1] for y in corners], 'o', color='red')
        pre_corners_line, = plt.plot([x[0] for x in pre_corners], [y[1] for y in pre_corners], 'o', color='gold')

        # Graph Config
        straights_line.set_antialiased(False)
        corners_line.set_antialiased(False)
        pre_corners_line.set_antialiased(False)

        plt.xlabel('X Coordinates')
        plt.ylabel('Y Coordinates')

        plt.show()

        if self.debug:
            self.print()


if __name__ == "__main__":
    divisor = TrackDivisor(wp.FUMIAKI_LOOP_2020, debug=False)
    divisor.show_graph()

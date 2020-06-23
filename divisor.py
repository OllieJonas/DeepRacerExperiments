import waypoints_list as wp
import matplotlib.pyplot as plt


class TrackDivisor:
    def __init__(self, waypoints, x_sensitivity=0.5, y_sensitivity=0.5, debug=False):
        self.waypoints = waypoints
        self.x_sensitivity = x_sensitivity
        self.y_sensitivity = y_sensitivity
        self.debug = debug

        self.corners = []
        self.before_corners = []
        self.straights = []

    def parse_track(self):
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
        line, = plt.plot([x[0] for x in self.waypoints], [y[1] for y in self.waypoints], 'bo')
        line.set_antialiased(False)
        plt.xlabel('X Coordinates')
        plt.ylabel('Y Coordinates')
        plt.show()

        if self.debug:
            self.print()


if __name__ == "__main__":
    divisor = TrackDivisor(wp.REINVENT_2018, debug=True)
    divisor.show_graph()

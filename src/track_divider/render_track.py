from src.track_divider.divisor import TrackDivisor
import matplotlib.pyplot as plt


class TrackRenderer:
    def __init__(self, divisor: TrackDivisor):
        self.divisor = divisor

    def render(self):
        """
        Displays a graph of the points.
        """

        straights, corners, pre_corners = self.divisor.build_lines()

        straights_line, = plt.plot([x[0] for x in straights], [y[1] for y in straights], 'o', color='lime')
        corners_line, = plt.plot([x[0] for x in corners], [y[1] for y in corners], 'o', color='red')
        pre_corners_line, = plt.plot([x[0] for x in pre_corners], [y[1] for y in pre_corners], 'o', color='gold')
        # highlight, = plt.plot([x[0] for x in self.highlighted], [y[1] for y in self.highlighted], 'o', color='blue')

        # Graph Config
        straights_line.set_antialiased(False)
        corners_line.set_antialiased(False)
        pre_corners_line.set_antialiased(False)

        plt.xlabel('X Coordinates')
        plt.ylabel('Y Coordinates')

        plt.show()

        # if self.divisor.debug:
        #     self.divisor.print()

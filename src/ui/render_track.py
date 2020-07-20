from tkinter import Canvas

from src.track.track import Track
import matplotlib.pyplot as plt


def get_speed_colour(speed):
    if speed == 4:
        return 'lime'
    elif speed == 2.67:
        return 'gold'
    elif speed == 1.33:
        return 'red'
    else:
        return 'black'


class TrackRenderer:
    def __init__(self, track: Track, canvas: Canvas):
        self.track = track
        self.canvas = canvas

    def render_matplot(self):
        """
        Displays a graph of the points.
        """

        waypoints = self.track.waypoints
        speeds = self.track.speed_calculator.rounded_speeds

        X = [x[0] for x in waypoints]
        Y = [y[1] for y in waypoints]

        for i, j in enumerate(X):
            plt.scatter(X[i], Y[i], color=get_speed_colour(speeds[i]))
        plt.show()

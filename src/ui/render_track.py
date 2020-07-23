from tkinter import Canvas

from colour import Color

from src.track.track_model import TrackModel
import src.util.maths as maths


class TrackRenderer:
    def __init__(self, track_model: TrackModel, canvas: Canvas):
        self.track = track_model
        self.canvas = canvas
        self.scale = self.calculate_scale()

        self.draw()

    def redraw(self):
        pass

    def draw(self):
        self.draw_waypoints()

    def draw_waypoints(self):
        granularity = 20
        colour_range = list(Color("red").range_to(Color("lime"), granularity + 1))
        for w in self.track.waypoints:
            self.draw_dot(w.x, w.y, 5, self.colour_from_speed(w.estimated_speed, 1.33, 4, colour_range=colour_range))

    def draw_dot(self, x, y, r, colour):
        x = (x - self.track.min_x) * self.scale
        y = (self.track.max_y - y) * self.scale

        self.canvas.create_oval(x - r, y - r, x + r, y + r, fill=colour, width=0)

    def draw_line(self, x, y):
        x *= self.scale
        y *= self.scale

        self.canvas.create_line()

    # There is 100% a better way of doing this...
    def colour_from_speed(self, speed, min_speed, max_speed, granularity=-1, colour_range=None):
        if colour_range is None:
            colour_range = list(Color("red").range_to(Color("lime"), granularity + 1))

        if granularity == -1:
            granularity = len(colour_range) - 1

        divider = (max_speed - min_speed) / granularity

        curr = min_speed
        lst = []
        for i in range(granularity + 1):
            lst.append(curr)
            curr += divider

        rounded_speed = maths.take_closest(lst, speed)
        index = lst.index(rounded_speed)
        return colour_range[index]

    def calculate_scale(self):
        return 100


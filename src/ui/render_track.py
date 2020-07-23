from tkinter import Canvas

from colour import Color

from src.track.track_model import TrackModel
import src.util.maths as maths


def colour_from_speed(speed, min_speed, max_speed, granularity=-1, colour_range=None):
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


class TrackRenderer:
    def __init__(self, track_model: TrackModel, canvas: Canvas):
        self.track = track_model
        self.canvas = canvas
        self.scale = 100

        # borders to prevent overflowing off UI
        self.x_border = 0
        self.y_border = 0

        self.draw()

    def clear(self):
        self.canvas.delete("all")

    def redraw(self, new_width, new_height):
        self.clear()
        self.adjust_scale(new_width, new_height)
        self.draw()

    def adjust_scale(self, new_width, new_height):
        x_scale = new_width / self.track.x_size
        y_scale = new_height / self.track.y_size

        self.scale = min(x_scale, y_scale)

        self.x_border = (1 - self.scale / x_scale) / 2 * self.track.x_size
        self.y_border = (1 - self.scale / y_scale) / 2 * self.track.y_size

        print(self.x_border, self.y_border)

    def draw(self, waypoint_size=3):
        self.draw_waypoints(granularity=20, size=waypoint_size)
        self.draw_borders()

    def draw_waypoints(self, granularity, size=2):
        assert granularity > 0

        colour_range = list(Color("red").range_to(Color("lime"), granularity + 1))
        for w in self.track.waypoints:
            self.draw_dot(w.x, w.y, size, colour_from_speed(w.estimated_speed, 1.33, 4, colour_range=colour_range))

    def draw_borders(self):
        self.draw_inside_border()
        self.draw_outside_border()

    def draw_inside_border(self):
        pass

    def draw_outside_border(self):
        pass

    def draw_dot(self, x, y, r, colour):
        x = (x - self.track.min_x - self.x_border) * self.scale
        y = (self.track.max_y - y + self.y_border) * self.scale

        self.canvas.create_oval(x - r, y - r, x + r, y + r, fill=colour, width=0)

    def draw_line(self, x, y):
        x *= self.scale
        y *= self.scale

        self.canvas.create_line()




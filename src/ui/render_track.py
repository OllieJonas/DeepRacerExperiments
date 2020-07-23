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
            self.draw_dot(w.x, w.y, size, colour_from_speed(w.estimated_speed, min_speed=1.33, max_speed=4, colour_range=colour_range))

    def draw_borders(self):
        length = len(self.track.outer_borders)
        # colour_range = self.generate_rainbow(spacing=3)

        prev_out = self.track.outer_borders[-1]
        prev_in = self.track.inner_borders[-1]

        for i in range(0, length):
            curr_out = self.track.outer_borders[i]
            curr_in = self.track.inner_borders[i]



            # c = colour_range[i % len(colour_range) - 1]
            # colour = Color(rgb=(c[0] / 255, c[1] / 255, c[2] / 255))

            if curr_out is not prev_out and curr_out is not prev_out:
                self.plot_line(prev_in[0], prev_in[1], curr_in[0], curr_in[1], 2, Color("blue"))
                self.plot_line(prev_out[0], prev_out[1], curr_out[0], curr_out[1], 2, Color("blue"))

            prev_out = curr_out
            prev_in = curr_in

    def draw_dot(self, x, y, r, colour):
        x = (x - self.track.min_x - self.x_border) * self.scale
        y = (self.track.max_y - y + self.y_border) * self.scale

        self.canvas.create_oval(x - r, y - r, x + r, y + r, fill=colour, width=0)

    def plot_line(self, x1, y1, x2, y2, width, fill_colour):

        x_line = (x1 - self.track.min_x - self.x_border) * self.scale
        y_line = (self.track.max_y - y1 + self.y_border) * self.scale

        x2_line = (x2 - self.track.min_x - self.x_border) * self.scale
        y2_line = (self.track.max_y - y2 + self.y_border) * self.scale

        self.canvas.create_line(x_line, y_line, x2_line, y2_line, fill=fill_colour, width=width)

    # # Jesus this is crude
    # def generate_rainbow(self, spacing=1):
    #     red = [255] * int(255 / spacing) * 3 + list(range(255, 0, -1 * spacing)) + [0] * (int(255 / spacing) * 2) + list(range(0, 143, 1 * spacing))
    #     green = list(range(0, 255, max(int(0.5 * spacing), 1))) + [255] * int(255 / spacing) * 2 + list(range(255, 0, -1 * spacing))
    #     blue = [0] * (int(255 / spacing) * 4) + list(range(0, 255, 1 * spacing)) + list(range(255, 130, -1 * spacing)) + list(range(130, 255, 1 * spacing))
    #     return list(zip(red, green, blue))




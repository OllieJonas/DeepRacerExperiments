import tkinter as tk

from src.track.track import Track


class TrackModel:
    def __init__(self, track: Track):
        self.track = track
        self.canvas = tk.Canvas(bg='black')
        self.waypoints = track.waypoints
        self.scale = 100

        self.draw_waypoints()
        self.canvas.update()

    def update_boundaries(self):
        x_size = self.track.max_x - self.track.min_x
        y_size = self.track.max_y - self.track.min_y

        self.scale = min(x_size, y_size)

    def draw_inside_border(self):
        pass

    def draw_outside_border(self):
        for w in self.waypoints:
            pass

    def draw_waypoints(self):
        for w in self.waypoints:
            self.draw_dot(w[0], w[1], 5, 'red')
        pass

    def draw_dot(self, x, y, r, colour):
        x = (x - self.track.min_x) * self.scale
        y = (self.track.max_y - y) * self.scale

        self.canvas.create_oval(x - r, y - r, x + r, y + r, fill=colour, width=0)

    def draw_line(self, x, y):
        x *= self.scale
        y *= self.scale

        self.canvas.create_line()



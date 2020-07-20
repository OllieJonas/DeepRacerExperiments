import tkinter as tk

from src.track.track import Track
from src.track.track_model import TrackModel
from src.ui.menu_bar import MenuBar

CANVAS_WIDTH, CANVAS_HEIGHT = 800, 500


class MainView(tk.Frame):
    def __init__(self, app, track: Track):

        # Init basic stuff
        self.root = tk.Tk()
        self.app = app
        self.track = track

        super().__init__(self.root)

        # Track Canvas
        self.track_canvas = TrackModel(track).canvas
        self.pack_track_canvas()

        # More basic stuff
        self.master.title("DR Optimum Racing Tool")
        self.menu_bar = MenuBar(self.root, app)

        self.update()

    def pack_track_canvas(self):
        self.track_canvas.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
        self.pack(fill=tk.BOTH, expand=True)

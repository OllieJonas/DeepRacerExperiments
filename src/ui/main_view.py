import tkinter as tk

from src.track.track import Track
from src.track.track_model import TrackModel
from src.ui.menu_bar import MenuBar
from src.ui.render_track import TrackRenderer

CANVAS_WIDTH, CANVAS_HEIGHT = 800, 500


class MainView(tk.Frame):
    def __init__(self, app, track: TrackModel):
        # Init basic stuff
        self.root = tk.Tk()
        self.app = app
        self.track = track

        super().__init__(self.root)

        # Track Canvas
        canvas = tk.Canvas(self, bg="black", width=1000, height=800)
        canvas.bind("<Configure>", self.print_scale)
        canvas.bind("<Button-1>", self.print_scale)
        canvas.bind("<Key>", self.print_scale)

        self.renderer = TrackRenderer(track, canvas)

        self.pack_track_canvas()
        self.pack(fill=tk.BOTH, expand=True)

        # More basic stuff
        self.master.title("DR Optimum Racing Tool")
        self.menu_bar = MenuBar(self.root, app)

    def pack_track_canvas(self):
        self.renderer.canvas.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

    def print_scale(self, event):

        print("Width: {} Height: {}".format(self.winfo_width(), self.winfo_height()))
        pass

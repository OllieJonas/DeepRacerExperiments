import src.config.waypoints as wp
from src.track.track import Track
from src.ui.main_view import MainView


class App:
    def __init__(self, headless_mode=False):

        self.headless_mode = headless_mode

        # Init tracks
        self.reinvent_2018 = Track(name="Reinvent 2018", waypoints=wp.REINVENT_2018, config_name="REINVENT_2018")
        self.fumiaki_loop_2020 = Track(name="Fumiaki Loop 2020", waypoints=wp.FUMIAKI_LOOP_2020,
                                  config_name="FUMIAKI_LOOP_2020")

        self.default_track = self.reinvent_2018  # Default track

        # Init UI
        if not headless_mode:
            self.view = MainView(self, self.reinvent_2018)
            self.view.mainloop()

        # renderer = TrackRenderer(reinvent_2018)
        # renderer.render()


if __name__ == "__main__":
    app = App()

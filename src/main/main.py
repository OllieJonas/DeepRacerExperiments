import src.config.waypoints as wp

from src.ui.render_track import TrackRenderer
from src.track.track import Track

reinvent_2018 = Track(name="Reinvent 2018", waypoints=wp.REINVENT_2018, config_name="REINVENT_2018")
fumiaki_loop_2020 = Track(name="Fumiaki Loop 2020", waypoints=wp.FUMIAKI_LOOP_2020, config_name="FUMIAKI_LOOP_2020")


if __name__ == "__main__":

    renderer = TrackRenderer(reinvent_2018)
    renderer.render()


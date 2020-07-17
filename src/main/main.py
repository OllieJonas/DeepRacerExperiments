import src.config.waypoints as wp
from src.track.track import Track
from src.ui.render_track import TrackRenderer

reinvent_2018 = Track(name="Reinvent 2018", waypoints=wp.REINVENT_2018, config_name="REINVENT_2018")
fumiaki_loop_2020 = Track(name="Fumiaki Loop 2020", waypoints=wp.FUMIAKI_LOOP_2020, config_name="FUMIAKI_LOOP_2020")


def test():
    circle_metrics = reinvent_2018.waypoint_metrics.circle_metrics
    smallest_radius = min([x['radius'] for x in circle_metrics])

    print(smallest_radius)


if __name__ == "__main__":
    test()
    # reinvent_2018.waypoint_metrics.debug_print()
    #
    # renderer = TrackRenderer(reinvent_2018)
    # renderer.render()

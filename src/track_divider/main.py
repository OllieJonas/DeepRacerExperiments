from src.track_divider.divisor import TrackDivisor
from src.track_divider.render_track import TrackRenderer
from src.track_divider import configs

if __name__ == "__main__":
    divisor = TrackDivisor(configs.REINVENT_2018, debug=True)
    renderer = TrackRenderer(divisor)
    renderer.render()

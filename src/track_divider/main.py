from src.track_divider.divisor import TrackDivisor
from src.track_divider.render_track import TrackRenderer
from src.track_divider import configs

if __name__ == "__main__":
    divisor = TrackDivisor(configs.FUMIAKI_LOOP_2020, debug=False)
    renderer = TrackRenderer(divisor)
    renderer.render()

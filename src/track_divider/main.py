from src.track_divider.divisor import TrackDivisor
from src.track_divider.render_track import TrackRenderer
from src.waypoint_metrics import WaypointMetrics

import src.config.divisor as divisor_configs
import src.config.gradient as gradients_configs
import src.config.waypoints as wp

if __name__ == "__main__":
    gradient_calculator = WaypointMetrics(wp.REINVENT_2018, gradients_configs.REINVENT_2018)
    divisor = TrackDivisor(wp.REINVENT_2018, gradient_calculator, divisor_configs.REINVENT_2018, debug=True)
    renderer = TrackRenderer(divisor)
    renderer.render()

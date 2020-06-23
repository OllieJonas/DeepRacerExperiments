from divisor_config import DivisorConfig
import waypoints_list as wp

REINVENT_2018 = DivisorConfig(
    wp.REINVENT_2018,
    narrow_gradient_threshold=0.125,
    wide_gradient_threshold=1.0,
    use_wide_gradient=True,
    distance_threshold=0.08,
    pre_corner_range=2,
    post_corner_range=1,
    waypoint_lookahead=1,
    waypoint_lookbehind=1
)

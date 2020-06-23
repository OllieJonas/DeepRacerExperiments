class DivisorConfig:
    def __init__(self, waypoints,
                 narrow_gradient_threshold=0.125,
                 wide_gradient_threshold=1.0,
                 use_wide_gradient=True,
                 distance_threshold=0.08,
                 pre_corner_range=2,
                 post_corner_range=1,
                 waypoint_lookahead=1,
                 waypoint_lookbehind=1):

        self.waypoints = waypoints

        self.narrow_gradient_threshold = narrow_gradient_threshold
        self.wide_gradient_threshold = wide_gradient_threshold
        self.use_wide_gradient = use_wide_gradient

        self.distance_threshold = distance_threshold

        self.pre_corner_range = pre_corner_range
        self.post_corner_range = post_corner_range

        self.waypoint_lookahead = waypoint_lookahead
        self.waypoint_lookbehind = waypoint_lookbehind

class DivisorConfig:
    def __init__(self,
                 narrow_gradient_threshold=0.125,
                 wide_gradient_threshold=0.125,
                 use_wide_gradient=True,
                 distance_threshold=0.09,
                 pre_corner_range=2,
                 post_corner_range=1
                 ):
        """
        Configuration file for the track divider.

        Gradient Threshold: If the gradient at this point is above the threshold,
                            then it will signal the car to change to the red setting.
                            If the gradient at this point is two times above the threshold,
                            then it will signal the car to change to the yellow setting

        :param narrow_gradient_threshold: Takes into account the current and the next waypoints
        :param wide_gradient_threshold: Takes into account the prev / next waypoints based on waypoint lookahead/behind
        :param use_wide_gradient: Whether to actually use the wide gradient
        :param distance_threshold: If two adjacent points are above this distance, it will assume green
        :param pre_corner_range: How many waypoints to indicate as yellow BEFORE reaching a corner
        :param post_corner_range: How many waypoints to indicate as yellow AFTER reaching a corner
        """

        self.narrow_gradient_threshold = narrow_gradient_threshold
        self.wide_gradient_threshold = wide_gradient_threshold
        self.use_wide_gradient = use_wide_gradient

        self.distance_threshold = distance_threshold

        self.pre_corner_range = pre_corner_range
        self.post_corner_range = post_corner_range


class GradientConfig:
    def __init__(self, waypoint_lookahead=1, waypoint_lookbehind=1):
        self.waypoint_lookahead = waypoint_lookahead
        self.waypoint_lookbehind = waypoint_lookbehind

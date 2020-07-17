from src.config.schemas import GradientConfig

configs = {
    "REINVENT_2018": GradientConfig(
        waypoint_lookahead=2,
        waypoint_lookbehind=2
    ),

    "FUMIAKI_LOOP_2020": GradientConfig(
        waypoint_lookahead=4,
        waypoint_lookbehind=4
    )
}

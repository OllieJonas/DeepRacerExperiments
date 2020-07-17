from src.config.schemas import GradientConfig

configs = {
    "REINVENT_2018": GradientConfig(
        waypoint_lookahead=1,
        waypoint_lookbehind=1
    ),

    "FUMIAKI_LOOP_2020": GradientConfig(
        waypoint_lookahead=5,
        waypoint_lookbehind=5
    )
}

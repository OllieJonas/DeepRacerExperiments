from src.config.schemas import GradientConfig

configs = {
    "REINVENT_2018": GradientConfig(
        waypoint_lookahead=1,
        waypoint_lookbehind=1
    )
}

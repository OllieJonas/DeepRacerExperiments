from src.config.schemas import SpeedConfig

configs = {
    "REINVENT_2018": SpeedConfig(
        waypoint_lookahead=1,
        waypoint_lookbehind=1
    ),

    "FUMIAKI_LOOP_2020": SpeedConfig(
        waypoint_lookahead=5,
        waypoint_lookbehind=5
    )
}

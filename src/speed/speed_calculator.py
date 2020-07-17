from src.track.waypoint_metrics import WaypointMetrics
from src.config.schemas import SpeedConfig
from enum import Enum


class Speed(Enum):
    low = 1
    mid = 2
    high = 3


class SpeedCalculator:
    def __init__(self, metrics: WaypointMetrics, speed_config: SpeedConfig):
        self.metrics = metrics
        self.speed_config = speed_config

        self.constant = speed_config.min_corner_speed / (metrics.smallest_radius ** 0.5)


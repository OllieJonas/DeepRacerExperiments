import math

from src.track.waypoint_metrics import WaypointMetrics

_axle_distance = 0.165


class AngleCalculator:
    def __init__(self, waypoints, waypoint_metrics: WaypointMetrics):
        self.waypoints = waypoints
        self.waypoint_metrics = waypoint_metrics

        self.angles = self.calculate_angles()

    def calculate_angles(self):
        radii = [x['radius'] for x in self.waypoint_metrics.circle_metrics]

        def angle_equation(axle_distance, radius):
            return math.asin(axle_distance / radius) * (180 / 3.14)

        return [angle_equation(_axle_distance, r) for r in radii]

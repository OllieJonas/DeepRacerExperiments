import math

from src.path.optimal_path import OptimalPathStrategy

axle_distance = 0.165


class AngleCalculator(OptimalPathStrategy):
    def __init__(self, waypoints):
        super().__init__()

        self.waypoints = waypoints

        self.angles = self.calculate_angles()

    def calculate_angles(self):
        radii = [x.circle_radius for x in self.waypoints]

        def angle_equation(axle_distance, radius):
            return math.asin(axle_distance / radius)

        return [angle_equation(axle_distance, r) for r in radii]

    def angles_in_degrees(self):
        return [x * (180 / 3.14) for x in self.angles]

    def waypoint_to_angle(self, wp1, wp2):
        pass

    def angle_to_waypoint(self, angle):
        pass

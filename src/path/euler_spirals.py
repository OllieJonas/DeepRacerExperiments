from src.path.optimal_path import OptimalPathStrategy


class EulerSpirals(OptimalPathStrategy):
    def __init__(self, waypoints):
        super().__init__()

        self.waypoints = waypoints

        self.length_from_init_position = self.calculate_length_from_init_position()

        self.spiral_length = self.calculate_spiral_length()

    def calculate_length_from_init_position(self):
        return 0

    def calculate_spiral_length(self):
        return 0

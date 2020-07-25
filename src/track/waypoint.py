import math

from src.util import maths as maths_util


class Waypoint:
    def __init__(self, pos, x, y, interpolated=False):

        # Defined fields
        self.pos = pos
        self.x = x
        self.y = y

        self.interpolated = interpolated

        # Calculated fields
        self.prev_raw = (0, 0)
        self.curr_raw = (x, y)
        self.next_raw = (0, 0)

        self.circle_radius = 0
        self.circle_centre = (0, 0)

        self.estimated_speed = 0
        self.estimated_rounded_speed = 0
        self.estimated_angle_of_approach = 0

    def update_circle_metrics(self, prev_raw, next_raw):
        self.prev_raw = tuple(prev_raw)
        self.next_raw = tuple(next_raw)

        circle_metrics = maths_util.calculate_circle_metrics(prev_raw, self.curr_raw, next_raw)
        self.circle_centre = circle_metrics['centre']
        self.circle_radius = circle_metrics['radius']

    def update_speed(self, possible_speeds, constant):
        def speed_equation(c, r):
            return min(c * (r ** 0.5), max(possible_speeds))

        self.estimated_speed = speed_equation(constant, self.circle_radius)
        self.estimated_rounded_speed = maths_util.take_closest(possible_speeds, self.estimated_speed)


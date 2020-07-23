import math


class TrackModel:
    def __init__(self, track):
        self.track = track
        self.waypoints = track.waypoints
        self.track_width = track.track_width

        # Min and Max X and Y
        x_coords = [x[0] for x in track.raw_waypoint_data]
        y_coords = [y[1] for y in track.raw_waypoint_data]

        self.min_x = min(x_coords)
        self.min_y = min(y_coords)

        self.max_x = max(x_coords)
        self.max_y = max(y_coords)

        self.x_size = self.max_x - self.min_x
        self.y_size = self.max_y - self.min_y

        self.inner_borders = []
        self.outer_borders = []

        self.populate_borders()

    def populate_borders(self):
        for i, wp in enumerate(self.waypoints):
            prev = self.waypoints[i - 1]
            left = self.get_target_point(prev.x, prev.y, wp.x, wp.y, 90, self.track_width / 2)
            right = self.get_target_point(prev.x, prev.y, wp.x, wp.y, -90, self.track_width / 2)

            self.inner_borders.append(left)
            self.outer_borders.append(right)
            pass

    def get_target_point(self, x1, y1, x2, y2, direction_offset, distance):
        direction = math.radians(math.degrees(math.atan2(y2 - y1, x2 - x1)) + direction_offset)
        return x2 + math.cos(direction) * distance, y2 + math.sin(direction) * distance

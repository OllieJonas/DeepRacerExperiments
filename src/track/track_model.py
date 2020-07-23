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

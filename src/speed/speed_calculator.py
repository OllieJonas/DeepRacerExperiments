from src.track.waypoint_metrics import WaypointMetrics


class SpeedCalculator:
    def __init__(self, metrics: WaypointMetrics, possible_speeds):

        _constant = min(possible_speeds) / (metrics.smallest_radius ** 0.5)

        def speed_equation(c, r):
            return min(c * (r ** 0.5), max(possible_speeds))

        from bisect import bisect_left

        def take_closest(entries, n):
            """
            Assumes entries is sorted. Returns closest value to myNumber.

            If two numbers are equally close, return the smallest number.
            """
            pos = bisect_left(entries, n)
            if pos == 0:
                return entries[0]
            if pos == len(entries):
                return entries[-1]
            before = entries[pos - 1]
            after = entries[pos]
            if after - n < n - before:
                return after
            else:
                return before

        self.speeds = [speed_equation(_constant, m['radius']) for m in metrics.circle_metrics]
        self.rounded_speeds = [take_closest(possible_speeds, x) for x in self.speeds]
        print(self.speeds)

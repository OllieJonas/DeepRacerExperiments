from src.track.waypoint_metrics import WaypointMetrics


class SpeedCalculator:
    def __init__(self, metrics: WaypointMetrics, possible_speeds):

        _constant = min(possible_speeds) / (metrics.smallest_radius ** 0.5)

        def speed_equation(c, r):
            return min(c * (r ** 0.5), max(possible_speeds))

        from bisect import bisect_left

        def take_closest(myList, myNumber):
            """
            Assumes myList is sorted. Returns closest value to myNumber.

            If two numbers are equally close, return the smallest number.
            """
            pos = bisect_left(myList, myNumber)
            if pos == 0:
                return myList[0]
            if pos == len(myList):
                return myList[-1]
            before = myList[pos - 1]
            after = myList[pos]
            if after - myNumber < myNumber - before:
                return after
            else:
                return before

        self.speeds = [take_closest(possible_speeds, speed_equation(_constant, m['radius'])) for m in metrics.circle_metrics]
        print(self.speeds)

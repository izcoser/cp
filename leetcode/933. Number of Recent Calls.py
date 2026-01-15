# easy, queue (super lazy and poorly performant solution)
class RecentCounter:

    def __init__(self):
        self.reqs = []

    def ping(self, t: int) -> int:
        self.reqs.append(t)
        self.reqs = [r for r in self.reqs if r >= t - 3000]
        return len(self.reqs)

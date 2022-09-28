G: float = 9.8


class MotionEqual:
    def __init__(self, start: float, speed: float, velocity: float):
        self.start = start
        self.speed = speed
        self.velocity = velocity

    def calculate(self, time: float) -> float:
        return self.start + self.speed * time + self.velocity * time ** 2 / 2

    def distance(self, point: float) -> float:
        return point - self.start

    def eval_time(self, point: float) -> float:
        if self.velocity == 0:
            return self.distance(point) / self.speed

        if self.speed == 0:
            return abs(self.distance(point) * 2 / G) ** .5

        raise ValueError('Unavailable eval time')


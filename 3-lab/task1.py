import random


def pi_circle_calc(radius: float, iters: int) -> float:
    counts = 0
    for i in range(0, iters):
        if sum([
            random.uniform(-radius, radius) ** 2,
            random.uniform(-radius, radius) ** 2,
        ]) <= radius ** 2:
            counts += 1

    return 4 * counts / iters


def pi_quarter_circle_calc(radius: float, iters: int) -> float:
    counts = 0
    for i in range(0, iters):
        if sum([
            random.uniform(0, radius) ** 2,
            random.uniform(0, radius) ** 2,
        ]) <= radius ** 2:
            counts += 1

    return 4 * counts / iters


if __name__ == '__main__':
    print(pi_circle_calc(radius=1, iters=10000000))
    print(pi_quarter_circle_calc(radius=1, iters=10000000))

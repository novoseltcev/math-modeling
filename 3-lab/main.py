import random

import matplotlib as mpl
import numpy as np

mpl.use("TkAgg")
import matplotlib.pyplot as plt  # noqa


def pi_circle_calc(radius: float, iters: int) -> tuple[float, list, list]:
    counts = 0
    xs = []
    ys = []
    for i in range(0, iters):
        if sum([
            (x := random.uniform(-radius, radius)) ** 2,
            (y := random.uniform(-radius, radius)) ** 2,
        ]) <= radius ** 2:
            counts += 1
        xs.append(x)
        ys.append(y)
    return 4 * counts / iters, xs, ys


def pi_quarter_circle_calc(radius: float, iters: int) -> tuple[float, list, list]:
    counts = 0
    xs = []
    ys = []
    for i in range(0, iters):
        if sum([
            (x := random.uniform(0, radius)) ** 2,
            (y := random.uniform(0, radius)) ** 2,
        ]) <= radius ** 2:
            counts += 1
        xs.append(x)
        ys.append(y)
    return 4 * counts / iters, xs, ys


def main(iters: int, radius: float, axs):
    ax = axs[0]
    ax.axis('equal')
    ax.set(xlim=(-1, 1), ylim=(-1, 1))
    pi1, xs, ys = pi_quarter_circle_calc(radius=radius, iters=iters)
    ax.plot(xs, ys, 'ob')
    X = np.linspace(0, radius, 100)
    Y = (radius ** 2 - X **2) ** .5
    ax.plot(X, Y, 'r-')
    ax.plot(X, Y * 0, 'r-')
    ax.plot(X * 0, Y, 'r-')

    ax = axs[1]
    ax.axis('equal')
    ax.set(xlim=(-1, 1), ylim=(-1, 1))
    pi1, xs, ys = pi_circle_calc(radius=radius, iters=iters)
    ax.plot(xs, ys, 'ob')
    X = np.linspace(-radius, radius, 100)
    Y = (radius ** 2 - X ** 2) ** .5
    ax.plot(X, Y, 'r-')
    ax.plot(X, -Y, 'r-')

    plt.show()


if __name__ == '__main__':
    fig, axs = plt.subplots(1, 2)
    main(iters=10000, radius=1, axs=axs)
    plt.show()

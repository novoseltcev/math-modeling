import matplotlib.pyplot as plt
import numpy as np


def calc(T1: float, T2: float, r: float, omega: float) -> None:
    y0 = 0
    phi0 = 0
    g = 9.8
    t = np.linspace(0, T1, 1000)

    spring_y = (y0 + g / omega ** 2) * np.cos(omega * t) - g / omega ** 2
    rx = r * np.cos(phi0 + 2 * np.pi * t / T1)
    ry = r * np.sin(phi0 + 2 * np.pi * t / T1) + spring_y

    plt.figure()
    plt.plot(rx, ry)
    plt.title(f"Соотношение = {T1 / T2}")
    plt.ylabel("Проекция радиус вектора ry")
    plt.xlabel("Проекция радиус вектора rx")


def main() -> None:
    k = 0.9
    m = 1
    omega = np.sqrt(k / m)
    T2 = 2 * np.pi / omega

    for koef in np.arange(0.5, 2., 0.5):
        calc(T1=T2 * koef, T2=T2, r=5, omega=omega)
    plt.show()


if __name__ == '__main__':
    main()

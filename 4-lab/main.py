import matplotlib.pyplot as plt
import numpy as np


def calc(T1: float, T2: float, r: float, omega: float) -> None:

    t = np.linspace(0, T1, 1000)

    spring_y = -10 * np.cos(omega * t)

    rx = r * np.cos(((2 * np.pi) / (T1)) * t)
    ry = r * np.sin(((2 * np.pi) / (T1)) * t) + spring_y

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
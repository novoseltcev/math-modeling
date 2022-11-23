import numpy as np
from scipy.integrate import odeint
import matplotlib as mpl

mpl.use("TkAgg")
import matplotlib.pyplot as plt # noqa


def balance(𝛼1, 𝛼2, 𝛽1, 𝛽2, 𝛾1, 𝛾2):  # noqa
    return [
        (𝛼1*𝛾2 + 𝛽2*𝛾1) / (𝛽1*𝛽2 - 𝛼1*𝛼2),
        (𝛼2*𝛾1 + 𝛽1*𝛾2) / (𝛽1*𝛽2 - 𝛼1*𝛼2),
    ]


def f(M, t, 𝛼1, 𝛼2, 𝛽1, 𝛽2, 𝛾1, 𝛾2):  # noqa
    return [
        𝛼1 * M[1] - 𝛽1 * M[0] + 𝛾1,
        𝛼2 * M[0] - 𝛽2 * M[1] + 𝛾2
    ]


def plot_M1_1(𝛽1, 𝛽2, 𝛾1, 𝛾2, t, M0, k):  # noqa
    for k1 in k:
        m = odeint(f, M0, t, args=(k1 * 𝛽1, 𝛽2, 𝛽1, 𝛽2, 𝛾1, 𝛾2))
        plt.plot(t, m[:, 0], '-', label=f'a1/b2={k1:.2f}')

    plt.xlabel('time')
    plt.ylabel('M')
    plt.legend()

def plot_M1_2(𝛽1, 𝛽2, 𝛾1, 𝛾2, t, M0, k):  # noqa
    for k2 in k:
        m = odeint(f, M0, t, args=(𝛽1, k2 * 𝛽2, 𝛽1, 𝛽2, 𝛾1, 𝛾2))
        plt.plot(t, m[:, 0], '-', label=f'a2/b1={k2:.2f}')
    plt.xlabel('time')
    plt.ylabel('M')
    plt.legend()

def plot_M2(𝛼1, 𝛼2, 𝛽1, 𝛽2, 𝛾2, t, M0, k):  # noqa
    for x in k:
        m = odeint(f, M0, t, args=(𝛼1, 𝛼2, 𝛽1, 𝛽2, x * 𝛾2, 𝛾2))
        plt.plot(t, m[:, 1], '-', label=f'g1/g2={x:.2f}')
    plt.xlabel('time')
    plt.ylabel('M')
    plt.legend()


if __name__ == '__main__':
    # 𝛼1, 𝛽2 = 4, 1  # noqa
    # 𝛼2, 𝛽1 = 1, 2  # noqa
    # # assert 𝛽1 * 𝛽2 > 𝛼1 * 𝛼2
    # M0 = balance(𝛼1, 𝛼2, 𝛽1, 𝛽2, 𝛾1, 𝛾2)
    𝛽1, 𝛽2 = 1, 1  # noqa
    𝛾1=𝛾2 = 1  # noqa
    t = np.linspace(0, 1, 10)
    k = (1/5, 1/3, 1, 3, 5)
    M0 = [10, 10]
    plt.figure()
    plot_M1_1(𝛽1, 𝛽2, 𝛾1, 𝛾2, t, M0, k)
    plt.figure()
    plot_M1_2(𝛽1, 𝛽2, 𝛾1, 𝛾2, t, M0, k)
    𝛼1, 𝛼2 = 1, 1  # noqa
    plt.figure()
    plot_M2(𝛼1, 𝛼2, 𝛽1, 𝛽2, 𝛾2, t, M0, k)
    plt.show()



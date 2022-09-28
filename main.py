from math import cos, sin, radians

import matplotlib as mpl
mpl.use("TkAgg")
import matplotlib.pyplot as plt

from utils_3d import MotionEqual

width, length = 9, 18
height_net = 2.43
y = 1.7


def main():
    # speed = float(input('Введите скорость бросания ( > 0 ): ').strip())
    # alpha = float(input('Введите угол бросания (90 > α > 0): ').strip())
    speed = 13
    alpha = 60
    step = 100
    result = []
    for x0 in ((x / step) * (length / 2) for x in range(step + 1)):
        for z0 in ((z / step) * width for z in range(step + 1)):
            if is_match_to_enemy_box(x0, z0, y, speed, alpha):
                result.append((x0, z0))
    xs = list(x[0] for x in result)
    zs = list(x[1] for x in result)
    plt.plot(xs, zs, 'go')
    plt.xlim([0, 9])
    plt.ylim([0, 9])
    plt.show()
    return result


def is_match_to_enemy_box(x0: float, z0: float, y0: float, speed: float, alpha: float) -> bool:
    phi = -90
    while phi <= 90:
        if predict(x0, z0, y0, speed, alpha, phi):
            return True
        phi += 1
    return False


def predict(x0: float, z0: float, y0: float, speed: float, alpha: float, phi: float) -> bool:
    x = MotionEqual(start=x0, speed=speed * cos(radians(alpha)) * cos(radians(phi)), velocity=0)
    z = MotionEqual(start=z0, speed=speed * cos(radians(alpha)) * sin(radians(phi)), velocity=0)
    y = MotionEqual(start=y0, speed=speed * sin(radians(alpha)), velocity=-9.8)
    t_net = x.eval_time(length / 2)
    t_x = x.eval_time(length)
    return (
            y.calculate(t_net) > height_net
            and y.calculate(t_x) < 0
            and (z.speed == 0 or y.calculate(max(z.eval_time(width), z.eval_time(0))) < 0)
    )


if __name__ == '__main__':
    print(main())
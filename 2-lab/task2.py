import matplotlib as mpl
import numpy as np

from matplotlib import cm
from matplotlib.colors import LightSource
from mpl_toolkits import mplot3d  # noqa

from rocket import Rocket

mpl.use("TkAgg")
import matplotlib.pyplot as plt  # noqa

fuel_in_last_stage = int(input('Enter percent of fuel in last stage: ')) / 100

rocket = Rocket(
    payload=7000,  # кг
    total_fuel=274000,  # кг
    total_structure=308000 - 274000,  # кг
    fuel_distribution=[.5-fuel_in_last_stage/2, .5-fuel_in_last_stage/2, fuel_in_last_stage],
    fuel_leaking=3,  # кг / с
)

print(f'weight={rocket.total_weight} | speed={rocket.get_speed(rocket.get_time_shooting_stage(rocket.stages - 1))}')

time_end_fuel = rocket.get_time_shooting_stage(rocket.stages - 1)
times = range(int(time_end_fuel))

t = np.linspace(0, int(time_end_fuel), 100)
d = np.linspace(0, 1 - fuel_in_last_stage, 10)
T, D = np.meshgrid(t, d)

SPEED = []
for dim in d:
    rocket.fuel_distribution = [1. - dim, dim, fuel_in_last_stage]
    x = []
    for time in t:
        x.append(rocket.get_speed(time))
    SPEED.append(x)
SPEED = np.matrix(SPEED)

fig = plt.figure()
ax = plt.axes(projection='3d')
surf = ax.plot_surface(T, D, SPEED, linewidth=1)
ax.set_xlabel('time, s')
ax.set_ylabel('distribution')
ax.set_zlabel('speed, km/h')
plt.show()

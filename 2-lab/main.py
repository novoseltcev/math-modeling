import matplotlib as mpl

from utils import Rocket

mpl.use("TkAgg")
import matplotlib.pyplot as plt  # noqa

rocket = Rocket(
    payload=22800,  # кг
    total_fuel=443850,  # кг
    total_structure=82350,  # кг
    fuel_distribution=[.33, .33, .34],
    fuel_leaking=4.24,  # кг / с
)

time_end_fuel = rocket.get_time_shooting_stage(rocket.stages - 1)
# for time in range(int(time_end_fuel)):
#     print(f't={time} | speed={rocket.get_speed(time)}')
print(rocket.get_weight_in_time(time_end_fuel))
print(f'Скорость в наивысшей точке: {rocket.get_speed(time_end_fuel)} км/c')


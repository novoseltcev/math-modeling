import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

pray_birth = 1.
predator_death = 1.5
pray_death_due_to_predators = 0.1
predator_growth = 0.75


def calc_populate(population: np.array, t: np.linspace = 0) -> np.array:
    return np.array([
        (
            pray_birth
            - pray_death_due_to_predators * population[1]
        ) * population[0],
        (

            pray_death_due_to_predators * predator_growth * population[0]
            - predator_death
        ) * population[1]
    ])


def main() -> None:
    N0 = pray_birth / pray_death_due_to_predators
    M0 = predator_death / predator_growth
    print("N0", N0)
    print("M0", M0)
    t = np.linspace(0, 17, 1000)
    population = odeint(
        func=calc_populate,
        y0=np.array([N0, M0]),
        t=t,
    )

    prays, predators = population.T
    plt.figure()
    plt.plot(prays, predators)
    plt.xlabel('Жертвы')
    plt.ylabel('Хищники')
    plt.title('Завимость поуляций друг от друга')

    plt.figure()
    plt.plot(t, predators, '-r', label='Хищники')
    plt.plot(t, prays, '-b', label='Жертвы')
    plt.legend(loc='upper right')
    plt.xlabel('Время')
    plt.ylabel('Популяция')
    plt.title('Эволюция популяций хищников и жертв')
    plt.show()


if __name__ == '__main__':
    main()

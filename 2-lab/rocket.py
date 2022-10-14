from math import log


class Rocket:
    def __init__(
            self,
            payload: float,
            total_structure: float,
            total_fuel: float,
            fuel_distribution: list[float],
            fuel_leaking: float
    ) -> None:
        self.payload = payload
        self.total_structure = total_structure
        self.total_fuel = total_fuel
        self.fuel_distribution = fuel_distribution
        self.fuel_leaking = fuel_leaking
        assert round(sum(self.fuel_distribution), 2) == 1.

    @property
    def total_weight(self):
        return sum([
            self.payload,
            self.total_fuel,
            self.total_structure
        ])

    @property
    def stages(self) -> int:
        return len(self.fuel_distribution)

    def get_fuel_in_stage(self, num: int) -> float:
        return self.fuel_distribution[num] * self.total_fuel

    def get_structure_in_stage(self, num: int) -> float:
        return self.total_structure / (self.stages + 1)

    def get_stage_weight(self, num: int) -> float:
        return sum([
            self.get_structure_in_stage(num),
            self.get_fuel_in_stage(num),
        ])

    def get_time_shooting_stage(self, num: int) -> float:
        if num == -1:
            return 0.

        return (self.get_fuel_in_stage(num) / self.fuel_leaking) + self.get_time_shooting_stage(num - 1)

    def get_weight_after_shooting_stage(self, num: int) -> float:
        if num == -1:
            return self.total_weight

        return self.get_weight_after_shooting_stage(num - 1) - self.get_stage_weight(num)

    def get_last_shooted_stage(self, time: float) -> int:
        stage = 0
        while time > self.get_time_shooting_stage(stage):
            stage += 1

        return stage - 1

    def get_weight_in_time(self, time: float) -> float:
        last_shooted_stage = self.get_last_shooted_stage(time)
        dt = time - self.get_time_shooting_stage(last_shooted_stage)
        return self.get_weight_after_shooting_stage(last_shooted_stage) - self.fuel_leaking * dt

    def get_speed(self, time: float) -> float:
        last_shooted_stage = self.get_last_shooted_stage(time)
        m_i = self.get_weight_after_shooting_stage(last_shooted_stage)
        t_i = self.get_time_shooting_stage(last_shooted_stage)
        if time == t_i:
            return self.fuel_leaking * log(m_i / self.get_weight_in_time(time))
        return self.get_speed(t_i) + self.fuel_leaking * log(m_i / self.get_weight_in_time(time))

    def debug_stage(self, num: int) -> str:
        return ' | '.join([
            f'stage={num}',
            f'time={round(self.get_time_shooting_stage(num), 2)}',
            f'weight={self.get_weight_after_shooting_stage(num)}',
            f'fuel={self.get_fuel_in_stage(num)}',
            f'structure={self.get_structure_in_stage(num)}'
        ])

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
        assert sum(self.fuel_distribution) == 1.

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
        return self.total_structure / (num + 1)

    def get_time_shooting_stage(self, num: int) -> float:
        if num == -1:
            return 0.

        return (self.get_fuel_in_stage(num) / self.fuel_leaking) + self.get_time_shooting_stage(num - 1)

    def get_weight_after_shooting_stage(self, num: int) -> float:
        if num == -1:
            return self.total_weight

        return self.get_weight_after_shooting_stage(num - 1) - (
                self.get_fuel_in_stage(num) + self.get_structure_in_stage(num)
        )

    def get_weight_in_time(self, time: float) -> float:
        stage = 0
        while time > self.get_time_shooting_stage(stage):
            stage += 1

        last_shooted_stage = stage - 1
        print(time, self.get_time_shooting_stage(stage), self.get_time_shooting_stage(last_shooted_stage))
        print(f'{self.get_weight_after_shooting_stage(last_shooted_stage)=}')
        print(f'{self.fuel_leaking * (time - self.get_time_shooting_stage(last_shooted_stage))=}')
        # print(self.get_weight_after_shooting_stage(last_shooted_stage))
        return self.get_weight_after_shooting_stage(last_shooted_stage) - self.fuel_leaking * (
                time - self.get_time_shooting_stage(last_shooted_stage)
        )

    def get_speed(self, time: float) -> float:
        return self.fuel_leaking * log(self.total_weight / self.get_weight_in_time(time))

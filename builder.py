from abc import ABC, abstractmethod


class Builder(ABC):
    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def add_case(self) -> None:
        pass

    @abstractmethod
    def add_motherboard(self) -> None:
        pass

    @abstractmethod
    def add_CPU(self) -> None:
        pass

    @abstractmethod
    def add_RAM(self) -> None:
        pass

    @abstractmethod
    def add_power_supply(self) -> None:
        pass

    @abstractmethod
    def add_GPU(self) -> None:
        pass

    @abstractmethod
    def add_cooling_system(self) -> None:
        pass
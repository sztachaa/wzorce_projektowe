from builder import Builder
from computer import Computer


class ComputerBuilder(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self):
        self._product = Computer()

    @property
    def product(self) -> Computer:
        product = self._product
        self.reset()
        return product

    def add_case(self) -> None:
        self._product.add("Obudowę")

    def add_motherboard(self) -> None:
        self._product.add("Płytę główną")

    def add_CPU(self) -> None:
        self._product.add("Procesor")

    def add_RAM(self) -> None:
        self._product.add("RAM")

    def add_power_supply(self) -> None:
        self._product.add("Zasilacz")

    def add_GPU(self) -> None:
        self._product.add("Kartę graficzną")

    def add_cooling_system(self) -> None:
        self._product.add("System chłodzenia")
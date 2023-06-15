from builder import Builder


class Director:

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_basic_computer(self) -> None:
        self.builder.add_case()
        self.builder.add_motherboard()
        self.builder.add_CPU()
        self.builder.add_RAM()
        self.builder.add_power_supply()

    def build_gaming_computer(self) -> None:
        self.builder.add_case()
        self.builder.add_motherboard()
        self.builder.add_CPU()
        self.builder.add_RAM()
        self.builder.add_power_supply()
        self.builder.add_GPU()
        self.builder.add_cooling_system()
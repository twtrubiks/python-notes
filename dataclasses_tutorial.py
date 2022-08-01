# ref. https://docs.python.org/3/library/dataclasses.html

from dataclasses import dataclass, field


class InventoryItemOLD:
    def __init__(self, name: str, unit_price: float, quantity_on_hand: int = 0):
        self.name = name
        self.unit_price = unit_price
        self.quantity_on_hand = quantity_on_hand
        self.total = self.unit_price * self.quantity_on_hand

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}', unit_price={self.unit_price}, quantity_on_hand={self.quantity_on_hand}, total={self.total})"


@dataclass(frozen=False)
class InventoryItem:
    """Class for keeping track of an item in inventory."""

    name: str
    unit_price: float
    quantity_on_hand: int = 0
    total: float = field(init=False)

    def __post_init__(self):
        self.total = self.unit_price * self.quantity_on_hand


if __name__ == "__main__":
    print(InventoryItemOLD("twtrubiks", 100, 2))
    print(InventoryItem("twtrubiks", 100, 2))

# ref. https://docs.python.org/3/library/dataclasses.html

from dataclasses import dataclass, field, asdict
from datetime import datetime

class InventoryItemOLD:
    def __init__(self, name: str, unit_price: float, quantity_on_hand: int = 0):
        self.name = name
        self.unit_price = unit_price
        self.quantity_on_hand = quantity_on_hand
        self.total = self.unit_price * self.quantity_on_hand

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}', unit_price={self.unit_price}, quantity_on_hand={self.quantity_on_hand}, total={self.total})"

def default_data():
    return [1, 2, 3]

@dataclass(frozen=False)
class InventoryItem:
    """Class for keeping track of an item in inventory."""

    name: str
    unit_price: float
    quantity_on_hand: int = 0
    total: float = field(init=False)
    data: list[int] = field(default_factory=default_data)

    def __post_init__(self):
        self.total = self.unit_price * self.quantity_on_hand

@dataclass
class BInventoryItem:
    secret: str = field(repr=False)
    id: int = 0
    item: InventoryItem = field(default_factory=InventoryItem)
    create_time: datetime = \
        field(init=False, default_factory=datetime.now)


if __name__ == "__main__":
    print(InventoryItemOLD("twtrubiks", 100, 2))
    print(InventoryItem("twtrubiks", 100, 2))
    item = InventoryItem(
        name="twtrubiks", unit_price=100, \
        quantity_on_hand=3, data=[0, 0, 0])
    print(item)
    b_item = BInventoryItem(item=item, secret="My Secret")
    print(b_item) # 不會顯示 secret
    print(asdict(b_item)) # to_dict

# ref
# https://docs.python.org/3/library/typing.html#typing.KeysView

from typing import KeysView


class Data:

    products = {
        "milk": {"price": 1.50, "quantity": 10},
        "eggs": {"price": 0.20, "quantity": 100},
        "cheese": {"price": 2.00, "quantity": 10},
    }

    def product_list(self) -> KeysView[str]:
        return self.products.keys()


products = {
    "milk": {"price": 1.50, "quantity": 10},
    "eggs": {"price": 0.20, "quantity": 100},
    "cheese": {"price": 2.00, "quantity": 10},
}

print(products.keys())

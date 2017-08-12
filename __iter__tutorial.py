class Product(object):
    def __init__(self):
        self.products = [
            {
                'id': 1,
                'count': 1,
                'price': 10
            },
            {
                'id': 2,
                'count': 2,
                'price': 20
            },
            {
                'id': 3,
                'count': 3,
                'price': 30
            },
            {
                'id': 4,
                'count': 4,
                'price': 40
            }
        ]

    def __iter__(self):
        for product in self.products:
            product['total'] = product['count'] * product['price']
            yield product


if __name__ == "__main__":
    p = Product()
    for result in p:
        print(result)

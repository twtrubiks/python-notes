class Product(object):
    def __init__(self):
        self.items = [
            {
                'id': 1,
                'value': 10
            },
            {
                'id': 2,
                'value': 20
            },
            {
                'id': 3,
                'value': 30
            },
            {
                'id': 4,
                'value': 40
            }
        ]

    def __len__(self):
        return sum(item['value'] for item in self.items)


if __name__ == "__main__":
    data = 'test'
    print('data.__str__(): {}'.format(data.__len__()))
    print('len(data): {}'.format(len(data)))
    product = Product()
    print('len(product): {}'.format(len(product)))

import json


class Stock:
    def __init__(self, num, date):
        self.num = num
        self.date = date
        self.push_date = ["5/3"]


# create object
stock = Stock("2222", "2/3")

# convert to JSON string
json_str = json.dumps(stock.__dict__)

print(json_str)

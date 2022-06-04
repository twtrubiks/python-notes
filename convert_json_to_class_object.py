import json


class User:
    def __init__(self, name):
        self.name = name


class Stock:
    def __init__(self, num, date, user):
        self.num = num
        self.date = date
        self.user = user


# create object
user = User("twtrubiks")
stock = Stock("2222", "2/3", user)

# convert to JSON string
json_str = json.dumps(stock, default=lambda o: o.__dict__)
print(json_str)

json_data = json.loads(json_str)
stock_obj = Stock(**json_data)
print(stock_obj)

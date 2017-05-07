# ref. https://www.programiz.com/python-programming/methods/built-in/staticmethod

# Static method
# However, when you need a utility function that doesn't access any properties of
# a class but makes sense that it belongs to the class, we use static functions.


# Static method vs Class method
# Static method knows nothing about the class and just deals with the parameters.
# Class method works with the class since its parameter is always the class itself.

#  Create utility function as a static method
class Dates:
    def __init__(self, date):
        self._date = date

    def get_date(self):
        return self._date

    @staticmethod
    def to_dash_date(date):
        return date.replace("/", "-")


# How inheritance works with static method?
class DatesWithSlashes(Dates):
    def get_date(self):
        return Dates.to_dash_date(self._date)


def main():
    # tutorial 1
    date = Dates("15-12-2016")
    date_from_birthday = "15/12/2016"
    date_with_dash = Dates.to_dash_date(date_from_birthday)

    if date.get_date() == date_with_dash:
        print("Equal")
    else:
        print("Unequal")

    # tutorial 2
    date2 = Dates("15-12-2016")
    date_with_slash = DatesWithSlashes("15/12/2016")

    if date2.get_date() == date_with_slash.get_date():
        print("Equal")
    else:
        print("Unequal")


if __name__ == "__main__":
    main()

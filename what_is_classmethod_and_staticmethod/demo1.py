class Dates:
    def __init__(self, date):
        self._date = date

    def get_date(self):
        return self._date

    @staticmethod
    def to_dash_date(date):
        return date.replace("/", "-")


def main():
    date = Dates("2018-10-10")  # <1>
    print('date.get_date():', date.get_date())  # <2>
    date_from_birthday = "2018/12/12"
    date_with_dash = Dates.to_dash_date(date_from_birthday)  # <3>
    print('date_with_dash:', date_with_dash)


if __name__ == "__main__":
    main()

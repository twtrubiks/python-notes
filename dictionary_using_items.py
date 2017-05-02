if __name__ == "__main__":

    # common way
    # dictory = {"first_name": "Alfred", "last_name": "Hitchcock"}
    #
    # for key in dictory:
    #     print("{} = {}".format(key, dictory[key]))

    # preferred way using items()
    dictionary = {"first_name": "twt", "last_name": "rubiks"}

    for key, val in dictionary.items():
        print("{} = {}".format(key, val))

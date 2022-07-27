def base_example_1():
    try:
        print("run_1")
    except Exception:
        print("Exception")
    finally:
        print("other code")


def example_1():
    try:
        print("run_1")
    except Exception:
        print("Exception")
        return "re Exception"
    finally:
        print("other code")


def example_1_except():
    try:
        1 / 0
    except Exception:
        print("Exception")
        return "re Exception"
    finally:
        print("other code")


def example_2_diff():
    try:
        print("run_1")
    except Exception:
        print("Exception")
        return "re Exception"

    print("other code")


def example_2_diff_except():
    try:
        1 / 0
    except Exception:
        print("Exception")
        return "re Exception"

    print("other code")


def example_file():
    # better with as statement
    myfile = open("test.txt", "w")

    try:
        # 1/0
        myfile.write("data")  # raises Exception
    except Exception:
        print("Exception")
    finally:
        print("close file")
        myfile.close()  # has run


if __name__ == "__main__":
    print(base_example_1())

    # print(example_1())
    # print(example_1_except()) # -> has print("other code") ## important

    # print(example_2_diff())
    # print(example_2_diff_except()) # -> no print("other code")

    # example_file()

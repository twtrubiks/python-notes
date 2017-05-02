from distutils.util import strtobool

if __name__ == "__main__":
    # Convert String to Boolean
    """
        Convert a string representation of truth to true (1) or false (0).
        True values are 'y', 'yes', 't', 'true', 'on', and '1';
        false valuesare 'n', 'no', 'f', 'false', 'off', and '0'.
        Raises ValueError if 'val' is anything else.
    """
    # print(bool('true'))  # -->error
    # print(bool('True'))  # -->error
    # print(bool('false'))  # -->error
    # print(bool('False'))  # -->error
    # print(bool('0'))  # -->error

    print(strtobool('true'))
    print(strtobool('True'))
    print(strtobool('False'))
    print(strtobool('on'))
    print(strtobool('n'))
    print(strtobool('y'))
    print(strtobool('0'))
    print(strtobool('1'))

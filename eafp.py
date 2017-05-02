# LBYL: Look Before You Leap
# EAFP: Easier to Ask for Forgiveness than Permission -> python

import os

if __name__ == "__main__":

    # violates EAFP coding style
    if os.path.exists("file.txt"):
        os.unlink("file.txt")

    # correspond EAFP coding style
    try:
        os.unlink("file.txt")
    # raised when file does not exist
    except OSError:
        pass

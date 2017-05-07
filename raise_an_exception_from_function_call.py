# If a function that is supposed to return a given type (e.g. list, tuple, dict)
# suddenly returns something else (e.g. None) the caller of that function will always
# need to check the type of the return value before proceeding. This makes for confusing
# and complex code. If the function is unable to produce the supposed return value
# it is better to raise an exception that can be caught by the caller instead.

# exceptions.Exception  REF. https://docs.python.org/3.4/library/exceptions.html#exceptions.Exception


# Anti-pattern
def get_secret_code_anti_pattern(password):
    if password != "bicycle":
        return None
    else:
        return "42"


# Raise an exception when an error is encountered or a precondition is unsatisfied
def get_secret_code(password):
    if password != "bicycle":
        raise ValueError
    else:
        return "42"


if __name__ == "__main__":
    # Anti-pattern
    secret_code_anti_pattern = get_secret_code_anti_pattern("unicycle")

    if secret_code_anti_pattern is None:
        print("Wrong password. (Anti-pattern) ")
    else:
        print("The secret code is {}".format(secret_code_anti_pattern))

    # Raise an exception when an error is encountered or a precondition is unsatisfied
    try:
        secret_code = get_secret_code("unicycle")
        print("The secret code is {}".format(secret_code))
    except ValueError as e:
        print("Wrong password.")
        print(isinstance(e, ValueError))  # e belong ValueError
        print(isinstance(e, Warning))  # e does not belong Warning

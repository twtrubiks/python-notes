# Return the dictionary containing the current scope's global variables.

print(globals())

class A:
    pass

x = 1

print(globals())
print(globals()["x"])
print(globals()["A"])

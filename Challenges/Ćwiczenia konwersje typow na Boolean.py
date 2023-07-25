# falsy values
print(bool())  # false
print(bool(0))  # false
print(bool(0.0))  # false
print(bool(()))  # false
print(bool([]))  # false
print(bool({}))  # false
print(bool(""))  # false
print(bool(None))  # false
print(bool(False))  # false

# true value
print(bool(True))  # true
print(bool(1))  # true
print(bool(0.1))  # true
print(bool(-10))  # true
print(bool((0,)))  # true - pamietac o przecinku
print(bool([0]))  # true
print(bool({0}))  # true
print(bool("7"))  # true

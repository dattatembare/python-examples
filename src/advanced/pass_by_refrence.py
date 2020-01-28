def f(value, key, hash={}):
    hash[value] = key
    return hash


print(f('a', 1))
print(f('b', 2))

# Expected
# {'a': 1}
# {'b': 2}

# Actual
# {'a': 1}
# {'a': 1, 'b': 2}

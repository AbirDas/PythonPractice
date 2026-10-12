
assert True, "this is true!"

value = 7

try:
    assert value > 8, "Now this is False!"
except AssertionError as a:
    print(a)
    print(type(a))
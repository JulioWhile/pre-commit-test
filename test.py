def foo(a, b):
    _c = 1
    _d = 2
    _unused_var = 123
    print("The result is: ", a + b)


def bar():
    _temp = 42  # allowed, underscore-prefixed
    print("something")  # bad spacing, single->double quote


foo(1, 2)

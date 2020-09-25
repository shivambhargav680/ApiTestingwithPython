'''def outer_func():
    def inner_func():
        print("Hello Inner function")
    return inner_func

var = outer_func()
print(var())
'''


def outer_func(msg):
    def inner_func():
        print(f"Hello outer function {msg}")
    return inner_func

var = outer_func("Hi there")
print(var())
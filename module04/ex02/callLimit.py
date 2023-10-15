def callLimit(limit: int):
    count = [0]
    def callLimiter(function):
        def limit_function(*args: any, **kwds: any):
            if (count[0] >= limit):
                print(f"Error: <function {function.__name__} at {hex(id(function))}> called too many times")
            else:
                function()
                count[0] += 1
        return limit_function
    return callLimiter

@callLimit(3)
def f():
    print ("f()")

@callLimit(1)
def g():
    print ("g()")

for i in range(3):
    f()
    g()

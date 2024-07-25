
def log_factorial_calls(func):
    def wrapper(n):
        print(f"Calling {func.__name__}({n})")
        result = func(n)
        print(f"Result: {result}")
        return result
    return wrapper

@log_factorial_calls
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_generator(n):
    for i in range(n + 1):
        yield factorial(i)

for fact in factorial_generator(5):
    pass
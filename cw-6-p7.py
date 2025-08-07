
def limit_time(maxcalls):

    count = 0

    def decorator(func):

        def wrapper(*args, **kwargs):
            nonlocal count
            count += 1
            if count < maxcalls:
                result = func(*args, **kwargs)
                return result
            else:
                return ("you exceed the limit")

        return wrapper
    return decorator


def execution_limit1(func):
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        if count < 3:
            result = func(*args, **kwargs)
            count += 1
            return result
        else:
            return ("you exceed the limit")

    return wrapper


# @execution_limit1
# def print_string(string):
#     return (string)

@limit_time(3)
def print_string(string):
    return (string)


print(print_string("Hello world"))
print(print_string("Hello world"))
print(print_string("Hello world"))
print(print_string("Hello world"))
print(print_string("Hello world"))
# print(print_string("Hello world"))


# @time(3)
# ​def limit(calls=3):
#     def decorator(func):

#         def wrapper(*args, **kwargs):

#         return wrapper
#     return decorator


def execution_limit(func):
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


@execution_limit
def print_string(string):
    return (string)


print(print_string("Hello world"))
print(print_string("Hello world"))
print(print_string("Hello world"))
print(print_string("Hello world"))
print(print_string("Hello world"))
# print(print_string("Hello world"))

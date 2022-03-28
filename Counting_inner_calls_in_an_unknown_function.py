"""
The aim of this kata is to determine the number of sub-function calls made by an unknown function.

You have to write a function named count_calls which:

takes as parameter a function and its arguments (args, kwargs)

calls the function

returns a tuple containing:

the number of function calls made inside it and inside all the sub-called functions recursively

the function return value.

NB: The call to the function itself is not counted.

HINT: The sys module may come in handy.
"""
import inspect
COUNT = 0


def decorator(func):
    def wrapper(*args, **kwargs):
        global COUNT
        COUNT += 1
        return func(*args, **kwargs)
    return wrapper


def count_calls(func, *args, **kwargs):
    global COUNT
    functions_in_file = {key: val for key, val in inspect.getmodule(func).__dict__.items()
                         if (callable(val) and key not in ["count_calls", "decorator"])}
    lambda_func = {str(val): key for key, val in functions_in_file.items() if val.__name__ == '<lambda>'}
    for f, val in functions_in_file.items():
        inspect.getmodule(func).__dict__[f] = decorator(val)
    if func.__name__ != '<lambda>':
        res = inspect.getmodule(func).__dict__[func.__name__](*args, **kwargs)
    else:
        try:
            res = inspect.getmodule(func).__dict__[lambda_func[str(func)]](*args, **kwargs)
        except KeyError:
            res = decorator(func)
    count, COUNT = COUNT - 1, 0
    for key, val in functions_in_file.items():
        inspect.getmodule(func).__dict__[key] = val
    return count, res

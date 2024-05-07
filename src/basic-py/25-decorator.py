def positiveIntCheck(func):
    # get function as parameter
    def wrapper(*args, **kwargs) :
        # get arguments from the function
        
        # get value from argument
        value = None
        if len(args) > 0 : value = args[0]
        elif len(kwargs) > 0 : value = kwargs["num"]
        
        if isinstance(value, int) and value >= 0 :
            # return the result of the fuction
            return func(*args, **kwargs)
        else :
            raise ValueError(f"value given in {func.__name__} is not a positive integer")

    # return the function wrapper
    return wrapper

# use a decoration fuction, can be use more than 1 func
@positiveIntCheck
def factorial(num: int) -> int:
    fact = 1
    for i in range(2, num + 1) :
        fact *= i
    
    return fact

print(factorial(5))
print(factorial())
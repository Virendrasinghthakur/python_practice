# create a decorator function to print function name and the values of its arguments evry time the function is called
import functools
def dec(fxn):
    @functools.wraps(fxn)
    def wrapper(n,m):
        # all_params=",".join(filter(None,[n,m]))
        print(f"executing function {fxn.__name__}(m={m},n={n})")
        fxn(n,m)
        print("hii")
    return wrapper
    

@dec
def sum(n,m):
    # print(f"parameter values are {n,m} and their output is {n*m}")
    return

sum(4,5)

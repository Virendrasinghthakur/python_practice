# impelement a decorator that caches the return values of a function , so that when it's called with the same arguments, the cached value is returned insted of re-executing the function


def cache_decorator(fxn):
    cache={}
    def wrapper(*args):
        if args in cache:
            print("from cache")
            return cache[args]
        
        print("executing...")
        result=fxn(*args)
        cache[args]=result
        return result
    return wrapper

@cache_decorator
def square(n):
    return n*n

print(square(5))
print(square(7))
print(square(9))
print(square(7))

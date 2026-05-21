from datetime import datetime

def time(fxn):

    def wrapper():
        start = datetime.now()
        fxn()
        end = datetime.now()
        print("Execution time:", end - start)
    return wrapper


@time
def multiplication():
    num = 5

    for i in range(1, 11):
        print(f"{num} X {i} = {num*i}")


multiplication()      
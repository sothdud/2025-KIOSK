def oneToNKoop(n):
    """
    O(n)
    """
    result = 0
    for i in range(1, n+1):
        result += i
    return result
def oneToNKoop2(n):
    """
    O(1)
    """
    return n*(n+1)//2

def timedecorator(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Time taken: ", end-start)
        return result
    return wrapper

timed_oneToNKoop = timedecorator(oneToNKoop)
timed_oneToNKoop2 = timedecorator(oneToNKoop2)

print(timed_oneToNKoop(1000000))
print(timed_oneToNKoop2(1000000))

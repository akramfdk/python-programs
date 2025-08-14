from time import time

def performance(func):
    def wrapper(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        end = time()
        print(f"It took {end - start} seconds to complete")

    return wrapper


if __name__ == "__main__":
    @performance
    def function(a, b, n):
        for _ in range(n):
            a*b
    
    function(5, 7, 25000000)
import functools
from Clockdeco import clock

# functools.lru_cache(maxsize=128, typed=False)
# lru cache uses a dict to store the results, and the keys are made from the 
# positional and keyword arguments used in the calls
@functools.lru_cache()
@clock
def fibonacci(n):
    if n<2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

@clock 
def fibonacci_memoized(n, memo):
    if n<2:
        return n
    else:
        memo[n] = fibonacci_memoized(n-2,memo) + fibonacci_memoized(n-1,memo)
        return memo[n]

@clock 
def fibonacci_memoized1(n):
    if n<len(memo1):
        return memo1[n]
    else:
        temp = fibonacci_memoized1(n-2) + fibonacci_memoized1(n-1)
        memo1.append(temp)
        return temp
       

if __name__ == '__main__':
    #print(fibonacci(6))

    # memo = [None] * 10
    # print(fibonacci_memoized(8, memo))

    # memo1 = [0,1]
    # print(fibonacci_memoized1(8))
"""
    Functions in Python are first-class objects. Programming language
    theorists define a "first-class object" as a program entity that can be
    1. Created at runtime
    2. Assigned to a variable or elements in a data structure
    3  Passed as an argument to a function
    4. Returned as the result of a function   
"""

def factorial(n):
    """return n!"""
    return 1 if n < 2 else n*factorial(n-1)

def memoize_factorial(n, memo):
    if(n < 2):
        memo[n] = n
    if memo[n] == None:
        memo[n] = memoize_factorial(n-1, memo) + memoize_factorial(n-2, memo) 
    return memo[n]

def bottomup_factorial(n):
    f = [0]*[n+1]
    f[0] = f[1] = 1

    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    
    return f[n]
import time
from Clockdeco import clock

@clock
def snnoze(seconds):
    time.sleep(seconds)

@clock
def factorial(n):
    return 1 if n<2 else n*factorial(n-1)

if __name__ == '__main__':
    print('*' * 40, 'Calling snooze(.123)')
    snnoze(.123)
    print('*' * 40, 'Calling factorial(6)')
    print('6! =', factorial(6))

# Records the initial time t0
# Calls the original factorial, saving the result
# Computes the elapsed time
# Formats and prints the collected data
# Returns the result saved in step 2.


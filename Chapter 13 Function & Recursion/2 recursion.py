# Recursion: here function calls itself again and again
def factorial(n):
    # NOTE: If you don't write base condition than function calls itself infinite times

    if n == 0 or n == 1: # base condition which doesn’t call the function any further
        return 1
    else:
        return n * factorial(n-1) # function calling itself
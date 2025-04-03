def factorial(n):
    '''This is factorial'''
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(5))
factorial(5)
print(factorial.__doc__)
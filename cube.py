def cube(n):
    return n*n*n

def bythree(n):
    if n%3==0:
        return cube(n)

    else:
        return False
    
print(bythree(5))
print(bythree(9))
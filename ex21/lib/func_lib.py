def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)
def A(n,k):
    return factorial(n)/factorial(n-k) #tu app cthuc
def C(n,k):
    return factorial(n)/(factorial(n-k)*factorial(k))
def factorial(solon):
    if solon==0:
        return 1
    return solon*factorial(solon-1)
def C(solon,sonho):
    if solon <= sonho:
        return 0
    return factorial(solon)/(factorial(solon-sonho)*factorial(sonho))
def P(n,m,d):
    if n<m or n<d:
        return 0
    return (C(d,1)*C(n-d, m-1))/C(n,m)
import math
def factorial(n):
    """
    Factorial function for quick calculation
    """
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

def combination(i, N):
    """
    Combination function for quick calculation
    """
    return factorial(N)/(factorial(i)*factorial(N - i))

def prob(n, p, N, r):
    return combination(n - r + 1, n)*(p ** n)*(1 - p)**r

def infoMeasure(n, p, N, r):
    return -math.log(prob(n, p, N, r), 2)

def sumProb(N, p, r):
    """
    Return the sum of probabilty of negbinomial sources
    """
    sum = 0 
    for i in range(1, N + 1):
        sum += prob(i, p, N, r)

    return sum

def approxEntropy(N, p, r):
    """
    Return the entropy of negbinomial sources
    """
    sum = 0
    for i in range(1, N + 1):
        sum += prob(i, p, N, r)*infoMeasure(i, p, N, r)
    return sum

print(approxEntropy(5, 0.5, 2))


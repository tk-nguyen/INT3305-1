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

def prob(n, p, N):
    return combination(n, N)*(p ** n)*(1 - p)**(N - n)

def infoMeasure(n, p, N):
    return -math.log(prob(n, p, N), 2)

def sumProb(N, p):
    """
    Return the sum of probabilty of binomial sources
    """
    sum = 0 
    for i in range(1, N + 1):
        sum += prob(i, p, N)

    return sum

def approxEntropy(N, p):
    """
    Return the entropy of binomial sources
    """
    sum = 0
    for i in range(1, N + 1):
        sum += prob(i, p, N)*infoMeasure(i, p, N)
    return sum

print(approxEntropy(3, 0.5))

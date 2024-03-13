import numpy as np

def primes(n):
    x = np.ones((n+1,), dtype=np.bool_)
    x[0] = False
    x[1] = False
    for i in range(2, int(n**0.5)+1):
        if x[i]:
            x[2*i::i] = False

    primes = np.where(x == True)[0]
    return primes

# print(len(primes(100_000_000)))

primes=primes(100_000_000)

for i in primes:
    print(i)

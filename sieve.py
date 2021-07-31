import math

def simple_sieve(n):
    if n < 2:
        return []
    size = n + 1
    sieve = [ True ] * size
    sieve[:2] = [ False, False ]
    for i in range(2, int(math.sqrt(size)) + 1):
        for j in range(i * i, size, i):
            sieve[j] = False
    return [ i for i in range(size) if sieve[i] ]


def segmented_sieve(n):
    if n < 2:
        return []
    m = int(math.sqrt(n)) + 1
    primes = simple_sieve(m)
    siz = len(primes)
    sieve = [ None ] * m
    for i in range(m, n + 1, m):
        sieve = [ True for val in sieve ]
        for p in primes[:siz]:
            lo = i - i % p
            if lo < i:
                lo += p
            for j in range(lo, i + m, p):
                sieve[j - i] = False
        hi = min(i + m, n + 1)
        primes.extend( [ j for j in range(i, hi) if sieve[j - i] ] )

    return primes

def n_primes(n):
    if n < 1:
        return []

    if n >= 6:
        m = int( math.sqrt(n*math.log(n) + n*math.log(math.log(n))) ) + 1
    else:
        m = 12

    # compute base sieve
    primes = simple_sieve(m)
    siz = len(primes)
    if siz >= n:
        return primes[:n]

    i = m
    while True:
        sieve = [ True ] * m
        for p in primes[:siz]:
            lo = i // p * p
            if lo < i:
                lo += p
            for j in range(lo, i + m, p):
                sieve[j - i] = False

        for j in range(m):
            if sieve[j]:
                primes.append(i + j)
                if len(primes) == n:
                    return primes
        i += m

def count_primes(n):
    if n < 2:
        return 0
    m = int(math.sqrt(n)) + 1
    primes = simple_sieve(m)
    count = 0
    for p in primes:
        if p > n:
            return count
        count += 1
        
    for i in range(m, n + 1, m):
        sieve = [ True ] * m
        for p in primes:
            lo = i // p * p
            if lo < i:
                lo += p
            for j in range(lo, i + m, p):
                sieve[j - i] = False

        for j in range(m):
            if sieve[j]:
                count += 1
            if i + j == n:
                return count

def nth_prime(n):
    if n < 1:
        return None

    if n >= 6:
        siz = int( n * math.log(n) + n * math.log(math.log(n)) )
    else:
        siz = 12

    m = int(math.sqrt(siz)) + 1
    # compute base primes
    primes = simple_sieve(m)
    if len(primes) > n:
        return primes[n - 1]
    count = len(primes)
    i = m
    while True:
        sieve = [ True ] * m
        for p in primes:
            lo = i // p * p
            if lo < i:
                lo += p
            for j in range(lo, i + m, p):
                sieve[j - i] = False
        
        for j in range(m):
            if sieve[j]:
                count += 1
                if count == n:
                    return i + j
        i += m

def print_list(p):
    n = len(p)
    if n > 100:
        return
    for i in range(0, n-n%6, 6):
        print('%12d'*6 % tuple(p[i:i+6]))
    print('%12d'*(n%6) % tuple(p[n-n%6:]))

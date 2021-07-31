#!/usr/bin/env python

import sys
import time
import sieve

def main(n):
    print('simple sieve')
    t1 = time.time()
    primes = sieve.simple_sieve(n)
    t2 = time.time()
    sieve.print_list(primes)
    print('elapsed time =', t2 - t1, 'seconds')
    print()

    print('segmented sieve')
    t1 = time.time()
    primes = sieve.segmented_sieve(n)
    t2 = time.time()
    sieve.print_list(primes)
    print('elapsed time =', t2 - t1, 'seconds')
    print()

    print('prime counting function')
    t1 = time.time()
    count = sieve.count_primes(n)
    t2 = time.time()
    print('\u03c0(%d) = %d' % (n, count))
    print('elapsed time =', t2 - t1, 'seconds')
    print()

    print('first', n, 'prime nos.')
    t1 = time.time()
    primes = sieve.n_primes(n)
    t2 = time.time()
    sieve.print_list(primes)
    print('elapsed time =', t2 - t1, 'seconds')
    print()

    print('nth prime no.')
    t1 = time.time()
    nth_prime = sieve.nth_prime(n)
    t2 = time.time()
    print('prime no.', n, '=', nth_prime)
    print('elapsed time =', t2 - t1, 'seconds')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.stderr.write('Usage: %s n\n' % sys.argv[0])
        sys.exit(1)
    try:
        n = int(sys.argv[1])
        main(n)
    except Exception as error:
        sys.stderr.write('%s\n' % error)
        sys.exit(1)

import mathtools

def test_isPrime():
    fails = 0
    print "Testing isPrime"
    primes = [2, 3, 5, 7, 983, 991, 997]
    not_primes = [4, 6, 8, 9, 993, 994, 995, 999]
    for prime in primes:
        if mathtools.isPrime(prime):
            print '+ ',  # Pass the test
        else:
            fails += 1
            print '- ',
    for not_prime in not_primes:
        if mathtools.isPrime(not_prime):
            fails += 1
            print '- ',
        else:
            print '+ ',  # Pass the test

    if not fails:
        print "TEST OK"
    else:
        print ("FOUND ", fails, " ERRORS")


def test_factorial():
    print "Testing factorial "
    fails = 0
    factorials = [(5, 120), (10, 3628800), (7, 5040), (12, 479001600)]
    for f in factorials:
        if mathtools.factorial(f[0]) == f[1]:
            print '+ ',  # Pass the test
        else:
            fails += 1
            print '- ',
    if not fails:
        print "TEST OK"
    else:
        print "FOUND ", fails, " ERRORS"

def test_fib():
    print "Testing fib "
    fails = 0
    fib = [(1, 1), (0, 0), (3, 2), (4, 3), (6, 8), (7, 13), (20, 6765)]
    for f in fib:
        if mathtools.fib(f[0]) == f[1]:
            print '+ ',  # Pass the test
        else:
            fails += 1
            print '- ',
    if not fails:
        print "TEST OK"
    else:
        print "FOUND ", fails, " ERRORS"

functions = ('isPrime', 'factorial', 'fib')
for f in functions:
    if hasattr(mathtools, f):
        globals()['test_'+f]()
    else:
        print "*", f, "IS NOT DEFINED"
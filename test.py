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

functions = ('isPrime')
for f in functions:
    if hasattr(mathtools, f):
        globals()['test_'+f]()
    else:
        print "*", f, "IS NOT DEFINED"
'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
def prime():
    primes = []
    primes.append(2)
    n = 3
    count = 1
    found = False
    while found == False:
        for x in primes:
            if n%x == 0:
                found = False
                break
                
            else:
                if x == primes[-1]:
                    primes.append(n)
                    count += 1
        n += 1
        if count == 10001:
            found = True
    print(primes[-1]) 

        
                
   

        
                
   

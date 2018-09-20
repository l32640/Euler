'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
import math
def sum_primes():
    som = []
    som.append(2)
    for n in range(3, math.sqrt(2000000)):
        prime = True
        for x in range(2, n):
            if math.sqrt(n)%x == 0:
                prime = False
                break
        if prime == True:
            som.append(n)
    
    print (sum(soma))

   

        
                
   

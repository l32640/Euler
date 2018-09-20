# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10
# without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
def smallest_number():
    i= 2520
    primes = [2,3,5,7,11,13,17,19] 
    max_num = 20
    while True:
        i += 1
        # testa todos os numeros 11 a 20 divisiveis por i com resto de 0 e imprime resultado
        divisible = True
        
        for x in primes:
            divisible = (i % x == 0)
            if not divisible:
                break
        if divisible:
            print("Found: %d"%i)
            break
        else:
            pass
            # print("%d not div by %d"%(i,x))

smallest_number()

'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''


def long():
    bigger = 0
    bigger_sequency = 0
    x = dict()
    for n in range(2, 1000001):
        num = n
        count = 0
        while num> 1:
            try:
                count += x[num] - 1
                break
            except KeyError:
                pass
             
            if num % 2 == 0:
                num = num / 2
            else:
                num = num * 3 + 1
            count += 1
 
        count += 1
        x[n] = count
 
        if count > bigger_sequency:
            bigger_sequency = count
            bigger = n
 
    print (bigger)
    print (bigger_sequency)
print(long())
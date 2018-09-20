'''
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10) ^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers
and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers
and the square of the sum.
'''
def diff_s_s():
    i=0
    sum1=[]
    sum2=[]
    for i in range(101):
        x=i**2
        sum1.append(x)
        i++1
    for i in range(101):
        sum2.append(i)
        i++1
    sum_squares=sum(sum1)
    square_sums=sum(sum2)
    square_sums=square_sums**2
    return square_sums-sum_squares

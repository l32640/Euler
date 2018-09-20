# A palindromic number reads the same both ways. The largest palindrome
# made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
# formula
#  numero n > 0 na base b ≥ 2, que é escrito em notação standart k+1 digits a(i) como:

def palindromo():
    numero=0
    for k in range(100, 999):
        for i in range(k+1, 999):
            inicio = k * i
            if inicio > numero:
                s = str(k * i)
                if s == s[::-1]:  #
                    numero = k * i
    print (numero)

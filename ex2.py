from math import factorial
n=int(input('Dati primul numar n='))
m=int(input('Dati al doilea numar m='))
if n<m:
    print('Nu este respectata conditia')
    exit()
def f(x):
    s=0
    d=1
    for i in range(1, x+1):
        d*=1
    return d
num=factorial(m) * (factorial(n-m))
c=factorial(n)/num
print('C=', c)
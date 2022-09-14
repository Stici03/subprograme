from re import I


def putere(x, y): return x**y
print("S=", putere(1, 0)+putere(0.5, 2)+putere(0.5, 4)+putere(0.6, 6))

def factorial(x):
    c=1
    for i in range(1, x+1):
        c=c*i
    return c

n=int(input("introdu valoarea lui n: "))
m=int(input("introdu valoarea lui m: "))
if n<m:
    print("eroare")
else:
    print("c=", factorial(n)/(factorial(m)*factorial(n-m)))
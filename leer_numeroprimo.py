from time import*

num = int(input("ingrese el valor  a evaluar: "))
cont = 0

print()
print("{0} es divisible por".format(num), end=": ")
for n in range(1, num+1):
    if num % n == 0:
        print(n, end=" - ")
        cont += 1
        print("fin")

if cont == 2:
    print("el numero ingresado si es primo, tiene {0} divisores".format(cont))
else:
    print("el numero ingresado no es primo, tiene {0} divisores".format(cont))
sleep(20)

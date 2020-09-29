from time import*

n = int(input("cuantas temperaturas quieres?: "))
c = 1
suma = 0
while c <= n:
    num = float(input("introduce el numeros de dias: "))
    suma += num
    c += 1
print("el promedio de temperaturas es ", suma / n)

sleep(20)

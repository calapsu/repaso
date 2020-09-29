from time import*


def esPrimo(l):
    primos = []
    for i in l:
        p = 0
        if i == 1:
            primos.append(i)
        else:
            for j in range(1, i+1):
                if i % j == 0:
                    p += 1
            if p == 2:
                primos.append(i)
    return primos


num = range(0, 100)
lista = num
print("numeros primos: %s " % esPrimo(lista))

# sumatoria de los valores
print('La suma de los valores de la lista es %d' % (sum(lista)))

# promedio de valores
print('El promedio es %.2f' % (sum(lista) / len(lista)))

sleep(20)

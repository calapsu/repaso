from time import*


def funcion_multiplos():
    multiplos = num / 5
    print("numeros de multiplos es %s" % round(multiplos))


num = int(input("ingresa un numero: "))


if num % 5 == 0:
    print("es multiplo de 5")
    funcion_multiplos()

else:
    print("no es multiplo de 5")

sleep(20)


#estemodulo genera valores aleatorios por defecto con los siguientes parametros
import random

#excluye los extremos
a = random.randrange(0,100)
print(a)


#incluye los  extremos

b = random.randint(0,100)
print(b)

#


c = random.choice([1,100,'berga']) #selecciona un elemento aleatorio de una lista
print(c)

#

d = random.random()
print(d)


e = random.uniform(0,10)
print(e)

#f = []
lista = ['marcos','papa',2,5,True]
random.shuffle(lista)
print(lista)

random.seed(100)
print(random.random())

random.seed(10)
print(random.random())





a = random.randrange(1,100) #otorga de manera random 1 numero entre 2 y 99 sin contar 1 y 100
print(a)
print("----------------------------------------")

b = random.randint(1,100) #otorga de manera random 1 numero entre 1 y 100 incluyendo ambos
print(b)
print("----------------------------------------")

c = random.choice([1,100,"blanco","negro"]) #selecciona un elemento aleatorio de una lista
print(c)
print("----------------------------------------")

d = random.random() #me da un numero flotante random entre 0 y 1
print(d)
print("----------------------------------------")

e = random.uniform(1,100) #me da un numero flotante random en este caso entre 1 y 100
print(e)
print("----------------------------------------")

f = [0, 25, 50, 75, 100] 
random.shuffle(f) #me devuelve la lista desordenada aleatoriamente
print(f)
print("----------------------------------------")

g = [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0,
     1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1]
random.shuffle(g) #LOS POLLITOS DE MYSTAKE
print(g)
print("----------------------------------------")

h = random.seed(3)
a1 = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
random.shuffle(a1)
i = random.seed(9)
a2 = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
random.shuffle(a2)
j = random.seed(3)
a3 = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
random.shuffle(a3)
k = random.seed(3)
a4 = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
random.shuffle(a1)
l = random.seed(9)
a5 = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
random.shuffle(a2)
m = random.seed(3)
a6 = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
random.shuffle(a3)
print("{}\n{}\n{}".format(a1, a2, a3))

cartas = [a1, a2, a3, a4, a5, a6]
aux = 0

for aux in range(len(cartas)):
    print(cartas[aux][0])
    aux = aux+1
    input("presione tecla para continuar")

# 
# #ejemplo sencillo 
# 
# 
# print()
# print('-------------------------------------------------------------------------')
# print()
# 
# numero = random.randint(-50,9)
# print(('numero : ').center(50),numero)
# print()
# print('-------------------------------------------------------------------------')
# print()
# 
# 
# #sea la siguiente lista
# regalos = ['sartén', 'jamón', 'mp4', 'muñeca', 'tv',
#            'patín', 'balón', 'reloj', 'bicicleta', 'anillo']
#            
# 
# for sorteo in range(5):
#     regalo = regalos[random.randint(0, 9)]
#     print('Sorteo', sorteo + 1, ':', regalo)
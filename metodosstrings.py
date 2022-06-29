#metodos strings
#count

texto = 'soy un cara de berga'

print('el articulo "un" aparece :',texto.count('un'))

# diferentes formas de formateo de strings

print('-----------------------------------------------------------')
a = texto.count('a')


print(f'la letra "a" aparece :{a} veces ')
print('la letra "a" aparece {} veces'.format(texto.count('a')))
print('la letra "a" aparece {} veces'.format(a))



print('-----------------------------------------------------------')

print('la palabra world aparece',texto.find("world"))

print('-----------------------------------------------------------')
print('-----------------------------------------------------------')
print('el texto seleccionado comienza con la palabra "soy :',texto.startswith('soy'))
print('el texto seleccionado comienza con la palabra "gil :',texto.startswith("gil"))


print('el texto seleccionado termina con la palabra "berga :',texto.endswith('berga'))
print('el texto seleccionado termina con la palabra "gil :',texto.endswith("gil"))

print('-----------------------------------------------------------')
print('-----------------------------------------------------------')
# isnumeric() es más amplia, pues incluye también caracteres de connotación
# numérica que no necesariamente son dígitos (por ejemplo, una fracción).
a = '1234'
b = '1234a'
c = '00.5'
print("la cadena de texto '{}' es numerica ?{}".format(a,a.isnumeric()))
print("la cadena de texto '{}' es numerica ?{}".format(b,b.isnumeric()))
print("la cadena de texto '{}' es numerica ?{}".format(c,c.isnumeric()))
print('-----------------------------------------------------------')
print('-----------------------------------------------------------')

# iisdecimal(), es la más restrictiva al tener en cuenta
# únicamente números decimales; esto es, formados por dígitos del 0 al 9.
a = '1234'
b = '1234a'
c = '1.5'
print("la cadena de texto '{}' es decimal ?{}".format(a,a.isdecimal()))
print("la cadena de texto '{}' es decimal ?{}".format(b,b.isdecimal()))
print("la cadena de texto '{}' es decimal ?{}".format(c,c.isdecimal()))
print('-----------------------------------------------------------')
print('-----------------------------------------------------------')

# isdigit(), considera caracteres que pueden formar números,
# incluidos aquellos correspondientes a lenguas orientales.
a = '1234'
b = '1234a'
c = '0,5+123'
print("la cadena de texto '{}' es un digito ?{}".format(a,a.isdigit()))
print("la cadena de texto '{}' es un digito ?{}".format(b,b.isdigit()))
print("la cadena de texto '{}' es un digito ?{}".format(c,c.isdigit()))
print('-----------------------------------------------------------')
print('-----------------------------------------------------------')

a = 'abc123'
b = 'abc'
c = '123'
d = 'ABC'
e = 'abc'
f = 'aBc'
g = '123/*\n'
h = ' '
# Determina si todos los caracteres son alfanuméricos.
print("la cadena de texto '{}' es un alfanumerico ?{}".format(a,a.isalnum()))
print("la cadena de texto '{}' es un alfanumerico ?{}".format(b,b.isalnum()))
print("la cadena de texto '{}' es un alfanumerico ?{}".format(c,c.isalnum()))
print("la cadena de texto '{}' es un alfanumerico ?{}".format(g,g.isalnum()))

print('-----------------------------------------------------------')
print('-----------------------------------------------------------')

# Determina si todos los caracteres son alfabéticos.
print("la cadena de texto '{}' es alfabetico ?{}".format(a,a.isalpha()))
print("la cadena de texto '{}' es alfabetico ?{}".format(b,b.isalpha()))
print("la cadena de texto '{}' es alfabetico ?{}".format(c,c.isalpha()))
print("la cadena de texto '{}' es alfabetico ?{}".format(g,g.isalpha()))


print('-----------------------------------------------------------')
print('-----------------------------------------------------------')
# # Determina si todas las letras son minúsculas.

print("la cadena de texto '{}' esta en minusculas ?{}".format(a,a.islower()))
print("la cadena de texto '{}' esta en minusculas ?{}".format(b,b.islower()))
print("la cadena de texto '{}' esta en minusculas ?{}".format(c,c.islower()))
print("la cadena de texto '{}' esta en minusculas ?{}".format(f,f.islower()))


print('-----------------------------------------------------------')
print('-----------------------------------------------------------')

# # Mayúsculas.

print("la cadena de texto '{}' esta en mayusculas ?{}".format(a,a.isupper()))
print("la cadena de texto '{}' esta en mayusculas ?{}".format(b,b.isupper()))
print("la cadena de texto '{}' esta en mayusculas ?{}".format(c,c.isupper()))
print("la cadena de texto '{}' esta en mayusculas ?{}".format(d,d.isupper()))

print('-----------------------------------------------------------')
print('-----------------------------------------------------------')

print("la cadena de texto '{}' es imprimible ?{}".format(a,a.isprintable()))
print("la cadena de texto '{}' es imprimible ?{}".format(b,b.isprintable()))
print("la cadena de texto '{}' es imprimible ?{}".format(c,c.isprintable()))
print("la cadena de texto '{}' es imprimible ?{}".format(g,g.isprintable()))

print('-----------------------------------------------------------')
print('-----------------------------------------------------------')

print("la cadena de texto '{}' tiene solo espacios ?{}".format(a,a.isspace()))
print("la cadena de texto '{}' tiene solo espacios ?{}".format(b,b.isspace()))
print("la cadena de texto '{}' tiene solo espacios ?{}".format(c,c.isspace()))
print("la cadena de texto '{}' tiene solo espacios ?{}".format(h,h.isspace()))

print('-----------------------------------------------------------')
print('-----------------------------------------------------------')


#Métodos de transformación
print('metodos de transformacion\n')
texto = 'soy un cara de poronga'
print('sea el siguiente texto :',texto)
print('ahora lo transformo {} '.format(texto.capitalize()))
print('\nformateo con una cadena de caracteres especifica en este caso utf-8')
print(texto.encode("utf-8"))

print('\n')
print('-----------------------------------------------------------')
print('-----------------------------------------------------------')
print('Los métodos center(), ljust() y rjust() alinean una cadena')

print("Hola".center(50))
print()
print("Hola".ljust(50))
print()
print("Hola".rjust(50))
print('-----------------------------------------------------------')
print('-----------------------------------------------------------')

print("Hola".center(50,'*'))
print()
print("Hola".ljust(50,'@'))
print()
print("Hola".rjust(50,'·'))

print('-----------------------------------------------------------')
print('-----------------------------------------------------------')

print('metodos de separacion y union')
print()
print('sea la siguiente cadena :',texto)

print(texto.split())

print()
print('el separador,como argumento en el siguiente ejemplo sera un espacio y el texto es :Hola mundo!\nHello world!')
print()
print("Hola mundo!\nHello world!".split(" "))
print()
print('Hola mundo!\nHello world! soy un cara de pija'.splitlines()) #separo lineas en los saltos unicamente
print()
print("Hola mundo hello world".split(" ", 1)) #con unseguundo argumento indico la cantidad de listas que voy armar
print("Hola mundo hello world".split(" ", 2))
print()
print(" ".join(["Hola", "mundo"]))    #concatenacion con el argumento espacio
                                    # o podemos decir un conversor de listas a str
                                    
print()
print(", ".join(["C", "C++", "Python", "Java"]))
print('-----------------------------------------------------------')
print('-----------------------------------------------------------')

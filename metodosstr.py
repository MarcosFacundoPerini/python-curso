a=("programando sin cigarrillos y sin yerba")
print(a)
print(a.count("sin"))  #Metodo Count
print(a.count("o"))
print(a.index("sin"))  #Buscar donde esta el inicio de la palabra
print(len(a))
print(a[13:40].index("sin"))
print("------------------------------------------")
c=a.index("sin")+1
b=a[13:40].index("sin")
print(a.index("sin"), end = ' ')
print(b+c)
print(a[30])
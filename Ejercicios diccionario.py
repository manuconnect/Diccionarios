#Ejercicio 1

d = {1:17,2:23, 3:19,4:18, 6:16}
lista = list(d.values())
lista.sort()
print(lista)


#Ejercicio 2

dic1 = {"pedro":17,2:23, 3:19,4:18, "jeje":16}
dic2 = {"juan":300,"pedro":230,"pepa":188, "Folo":167, "yuyo":119}


d = {1:17,2:23, 3:19,4:18, 5:16}
e = {1:17,2:23,4:18, 5:16, 3:19}

puerta = True
for i in d:

    if e[i] == d[i]:
        pass
    else:
        puerta = False

print(puerta)

#Ejercicio 3
def mezcla(d,e):

    t = {}
    
    for i in d:
        t[i] = d[i]

    for i in e:

        if i in t:
            pass
        else:
            t[i] = e[i]
    
    return t

print(mezcla(dic1,dic2))


#Ejercicio 4

persona1 = {"nombre":"Manuel" , "apellido":"Velasco", "edad":23}
persona2 = {"nombre":"Luci" , "apellido":"Buitrago", "edad":19}
persona3 = {"nombre":"Sara" , "apellido":"Vargas", "edad":82}
persona4 = {"nombre":"Juan" , "apellido":"Perez", "edad":63}

lista =[persona1, persona2, persona3, persona4]

for i in lista:
    
    if i["edad"] >18 and i["edad"]<30:
        print(i["nombre"], i["apellido"])



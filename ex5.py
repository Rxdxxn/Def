def creareListaFloat(n):
    lista = []
    for i in range(n):
        element = input('Dati un element de tip float: ')
        try:
            lista.append(float(element))
        except:
            while not element.isdecimal():
                element = input('Mai incercati: ')
            lista.append(float(element))
    return lista

print(creareListaFloat(5))
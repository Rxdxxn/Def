def creareListaInt(n):
    lista = []
    for i in range(n):
        element = input('Dati un element de tip integer: ')
        try:
            lista.append(int(element))
        except:
            while not element.isnumeric():
                element = input('Mai incercati: ')
            lista.append(int(element))
    return lista

print(creareListaInt(5))


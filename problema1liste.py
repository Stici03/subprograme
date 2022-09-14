def creare_lista():
    n=int(input("introdu nr de elemnte: "))
    lista_noua=[]
    for i in range(n):
        element=int(input("introdu elementul cu nr: "))
        lista_noua.append(element)
    return lista_noua

lista1=creare_lista()
print(lista1)
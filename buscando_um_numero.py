
def buscabinaria(lista,alvo,inicio,fim):
    if inicio>fim:
        return -1
    meio=(inicio+fim)//2
    if lista[meio]==alvo:
        return True
    elif alvo not in lista:
        return False
    elif lista[meio]>alvo:
        return buscabinaria(lista,alvo,inicio,meio-1)
    else:
        return buscabinaria(lista,alvo,meio+1,fim)
#programa principal
lista=[987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]
lista.sort()
print(buscabinaria(lista,1,0,19))
      
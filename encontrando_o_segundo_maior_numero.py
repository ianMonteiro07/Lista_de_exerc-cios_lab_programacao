def segundo_maior(lista):
    lista.remove(max(lista))
    print(max(lista))

lista=[987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]
print(lista)
print(f'o segundo maior elemento da lista é {segundo_maior(lista)}')
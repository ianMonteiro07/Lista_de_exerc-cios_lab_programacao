
lista=[987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]
def soma(lista):
    if len(lista)==0:
        return 0
    else:
        return lista[0]+soma(lista[1:])
print(f'A lista é -> {lista} e a soma é -> {soma(lista)}')

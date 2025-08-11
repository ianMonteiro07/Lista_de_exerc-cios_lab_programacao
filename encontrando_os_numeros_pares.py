def pares(lista):
    nova=lista[0:]
    for i in nova:
        if i%2!=0:
            nova.remove(i)
    print(f'lista par -> {nova}' )
lista=[987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]
print(f'lista original -> {lista}')
pares(lista)
def ocorrencias(lista,n):
    soma=0
    for i in range(len(lista)):
        if lista[i]==n:
            soma+=1
    print(f' O número escolhido apareceu {soma} vezes')

lista=[987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]
ocorrencias(lista,2)
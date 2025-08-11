def media(lista):
    s=0
    m=0
    for i in range(len(lista)):
        s+=lista[i]
    m=s//len(lista)
    print(f'{s}/{len(lista)}=media ->{m}')
lista= [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]
media(lista)
    

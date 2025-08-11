def extrair_nomes(lista):
    nomes=[]
    for objeto in lista:
        nomes.append(objeto.nome)
    return nomes
class Pessoa:
     def __init__(self,nome,idade):
         self.nome=nome 
         self.idade=idade

pessoas=[
    Pessoa('Alice',30),
    Pessoa('Alberto',39),
    Pessoa('Albiran',60)
    ]
nomes_extraidos = extrair_nomes(pessoas)
print(nomes_extraidos) 

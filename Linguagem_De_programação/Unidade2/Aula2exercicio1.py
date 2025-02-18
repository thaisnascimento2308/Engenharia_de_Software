#SET
#add(), in e remove()

#Criando um conjunto vazio
meu_conjunto = set()

#Adicionando elementos ao conjunto
meu_conjunto.add(10)
meu_conjunto.add(20)
meu_conjunto.add(30)

#Imprimindo o conjunto
print("Conjunto apos adicionar elementos: ", meu_conjunto)

#Verificando se um elemento está no conjunto
elemento = 20
if elemento in meu_conjunto:
    print(f"{elemento} está no conjunto")
else:
    print(f"{elemento} não está no conjunto")

#Removendo um elemento do conjunto
meu_conjunto.remove(20)

#Imprimindo o conjunto atualizado
print("Conjunto após remover o elemento 20:", meu_conjunto)

#DICT 
#Criação de dicionario vazio, seguido de atribuição de chaves e valores
dici_1 = {}
dici_1['nome'] = "Maria"
dici_1['idade'] = 25

#Criação de um dicionario com pares chave:valor
dici_2 = {'nome': 'Maria', 'idade': 25}

#Criação de um dicionario com uma lista de tuplas representando pares chave: valor
dici_3 = dict([('nome', "Maria"), ('idade', 25)])

#Criação de um dicionario usando a função built-in zip() e duas listas, uma para as chaves e outra para valores
dici_4 = dict(zip(['nome', 'idade'], ["Maria", 25]))

#Teste se todas as construções resultam em objetos iguais
print(dici_1 == dici_2 == dici_3 == dici_4) #deve imprimir true
print(dici_1)

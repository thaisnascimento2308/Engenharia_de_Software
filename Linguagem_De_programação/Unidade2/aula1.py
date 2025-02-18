texto = "Explorando a diversidade de linguagens de programação com Python."

print(f"Tamanho do texto = {len(texto)}")
print(f"Python intexto = {'Python' in texto}")
print(f"Quantidade de e no texto = {texto.count('e')}")
print(f"As cinco primeiras letras do texto são: {texto[:5]}")


cores = ['vermelho', 'azul', 'verde', 'amarelo', 'roxo']
for cor in cores:
    print(f'Posição = {cores.index(cor)}, cor = {cor}')
    
#listcomp
linguagens = ["Python", "Java", "JavaScript", "C", "C#", "C++", "Swift", "Go", "Kotlin"] #lista
print("Antes da listcomp = ", linguagens) #Imprime a lista como está

linguagens = [item.lower() for item in linguagens] #lower coloca todos os caracteres em minúsculos.
print("\nDepois da listcomp = ", linguagens) #\n para quebra de linhas.

#Função MAP
#Aplica a uma função em toda a sequencia
#map(função, sequencia)
precos_em_dolares = [100, 50, 75, 120]
taxa_de_cambio = 5.25
precos_em_reais = list(map(lambda x: x * taxa_de_cambio, precos_em_dolares))
#precos_em_reais = [x * taxa_de_cambio for x in precos_em_dolares]
print(precos_em_reais)

#Função FILTER
#Filtra os elementos de uma sequencia com base em uma função de teste (retorna true or false)
#Filter(funcao_teste, sequencia)
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
#numeros_pares = [x for x in numeros if x % 2 == 0]
print(numeros_pares)

#Tupla, a ordem importa
vogais = ('a', 'e', 'i', 'o', 'u')
print(f"Tipo do objeto vogais = {type(vogais)}")
for p, x in enumerate(vogais):
    print(f"Posição = {p}, valor = {x}")
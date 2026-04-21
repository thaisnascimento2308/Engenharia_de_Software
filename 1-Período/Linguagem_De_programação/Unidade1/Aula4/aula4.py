# Cria uma lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11, '12', True]
# Usa a função len() para calcular o comprimento da lista
comprimento = len(numeros)
# Imprime o comprimento da lista
print("O comprimento da lista é:", comprimento)

#Definindo uma função chamada 'soma'
def soma (a ,b):
    resultado = a + b
    return resultado

result = soma(5, 9)
print(f"A soma de 5 e 9 é:", result)

#Definindo uma função chamada "e_par"
def e_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    
numero = 1235488791

if e_par(numero):
    print(f"{numero} é um número par.")
else:
    print(f"{numero} é um número ímpar.")

#Função anonima ou lambda
soma = lambda a, b: a + b #lambda para funçoes usadas apenas 1 vez
resultado = soma(3, 4)
print(resultado)
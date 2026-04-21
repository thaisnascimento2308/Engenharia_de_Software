#For
numeros = [1, 2, 3, 4, 5]
for num in numeros:
    print(num)
    
#While
numero = int(input("Digite um número (ou 0 para sair): "))

while numero != 0:
  if numero % 2 == 0:
   print("O número é par.")
  else:
   print("O número é ímpar.")
  numero = int(input("Digite outro número (ou 0 para sair): "))
  
#range
#Repetição por Quantidade:
for x in range(5): #Range começa em 0
 print(x)

#Limites Inicial e Superior:
for y in range(2, 7): #o 7 não entra no looping
 print(y)

#Com Incremento:
for z in range(1, 11, 2): #o 11 não entra no looping
 print(z)

#Break
for numero in range(1, 11):
 if numero % 2 == 0:
  print("O primeiro número par encontrado é:", numero)
 break

#Continue
for numero in range(1, 11):
  if numero == 5: #vai pular o 5
   continue
  print(numero)
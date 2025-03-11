Nota_1 = int(input('Digite uma nota: '))
Nota_2 = int(input('Digite uma nota: '))
Nota_3 = int(input('Digite uma nota: '))
Nota_4 = int(input('Digite uma nota: '))

media = (Nota_1+Nota_2+Nota_3+Nota_4)/4

if media >= 6:
    situacao = print ("Aprovado")
else:
    situacao = print ("Reprovado")

print(f'{media}')
print(f'{situacao}')
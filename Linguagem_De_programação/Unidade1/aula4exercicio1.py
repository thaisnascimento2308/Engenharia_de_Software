#Lista de notas
notas = [7.5, 8.0, 6.5, 9.0, 7.0]
#notas = [1.5, 8.0, 6.5, 9.0, 7.0]

#Função regular para calcular média
def calcular_media(notas):
    total = sum(notas) #soma as notas
    media = total / len(notas) #media é = total dividido pelo numero de notas
    return media

#Função lambda para arredondar a media para duas casas decimais
arredondar_media = lambda media: round(media, 2)

#def arredondar_media(media):  (mesma coisa da linha de cima)
#    return round(media, 2)

#Calcular a média
media = calcular_media(notas)
media_arredondada = arredondar_media(media)

#Verificar se os estudantes foram aprovados
#situacao = "Aprovado" if media_arredondada >= 7 else "Reprovado"
if media_arredondada >= 7:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

#Resultados
print("Notas dos estudantes:", notas)
print("Media das notas:", media_arredondada)
print("Situação do estudante:", situacao)
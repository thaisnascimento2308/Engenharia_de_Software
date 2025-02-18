#Suponha que temos 3 filmes por semana, cada filme tem uma faixa etária, o primeiro é para menores que 12 anos, o segundo é para maiores ou iguais a 12 anos e menores que 18, por fim, o terceiro filme é para maiores de ou igual a 18 anos. Outro ponto solicitado é a respeito da disponibilidade de ingressos.

#Solicita a idade do cliente
idade = int(input('Digite sua idade: '))

#Verifica a idade para sugestçao de filmes
if idade < 12:
    print('Recomendamos o filme infantil N1')
elif idade >= 12 and idade < 18:
    print('Recomendamos o filme adolescente N2')
else:
    print('Recomendamos o filme emocionane N3')

#Verifica a disponibilidade de ingressos
ingressos = 3
if ingressos > 0:
    print('Ingressos disponiveis. Divirta-se.')
else:
    print('Ingressos indisponiveis. Sinto muito.')

#1.Como as estruturas condicionais em Python podem ser usadas para tomar decisões em programas?

#São usadas para tomar decisões em programas verificando se certas condições são verdadeiras ou falsas. A principal estrutura condicional é o if, que pode ser complementada com elif (senão se) e else (senão). Elas permitem que o programa execute diferentes blocos de código dependendo do resultado da condição.

#2.Qual é a importância da reutilização de código por meio de funções na programação em Python?

#Funções permitem que você escreva blocos de código reutilizáveis, promovendo a modularidade e a manutenção eficiente. Quando um pedaço de código precisa ser usado repetidamente, ele pode ser encapsulado em uma função. Isso evita duplicação de código, facilita a leitura e o entendimento do programa, e torna o processo de correção ou modificação mais simples. 

#3.Como você pode aplicar o pensamento lógico para resolver problemas complexos usando Python em sua trajetória acadêmica e profissional?

#Para resolver problemas complexos com Python, você pode decompor o problema em partes menores e abordá-las de forma sequencial. Isso envolve entender o problema, planejar uma solução, aplicar condicionais, laços e funções, e, finalmente, testar o código para garantir que ele funcione conforme o esperado. Na sua trajetória acadêmica e profissional, o pensamento lógico permite que você aborde desafios de forma estruturada, resolvendo problemas passo a passo com algoritmos, refinando soluções e automatizando processos.

#Questões norteadoras!
#1. Como você pode aplicar seus conhecimentos em programação em Python para criar uma calculadora de desconto?

#Você pode usar funções e operações matemáticas para calcular o valor do desconto e aplicar ao preço original. A calculadora pode receber o valor do produto, a porcentagem de desconto e, então, calcular o preço final.

#2.Quais estruturas condicionais em Python você pode usar para verificar se o desconto está dentro de limites aceitáveis?

#Para garantir que o desconto seja razoável, você pode usar as estruturas condicionais if, elif e else para verificar se o valor do desconto está dentro de um intervalo aceitável, como entre 0% e 100%. 

#Imagine que você trabalha em uma loja de eletrodomésticos e precisa criar uma calculadora de desconto em Python para ajudar os vendedores a calcular o valor final de uma compra com base no valor do produto e em um desconto percentual oferecido.

#Solicita ao usuario que insira o valor do produto e o percentual de desconto
valor_produto = float(input("Digite o valor do produto: R$ "))
desconto = float(input("Digite o percentual de desconto: "))

#Verifica se o percentual de desconto está dentro dos limites aceitavéis (0 a 100%)
if desconto < 0 or desconto > 100:
    print("Erro: O percentual de desconto deve estar entre 0% e 100%.")
else:
    #Calcula o valor do desconto
    valor_desconto = valor_produto * (desconto / 100)

#Calcula o valor final da compra
valor_final = valor_produto - valor_desconto

#Exibe o vcalor final da compra
print(f"Valor com desconto: R$ {valor_final:.2f}") #Valor exibido com 2 casas decimais
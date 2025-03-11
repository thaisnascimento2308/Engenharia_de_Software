#Você está gerenciando uma lista de convidados para uma festa e uma lista de pessoas que confirmaram sua presença. Você deseja identificar as pessoas que ainda não confirmaram e convidá-las novamente.

#Tupla de convidados
convidados = ("Alice", "Bob", "Carol", "Julio", "Eve")

#Lista de confirmações
confirmados = ["Bob", "Julio"]

#Identificar quem ainda não confirmou
nao_confirmados = [convidado for convidado in convidados if convidado not in confirmados]

#Exibir os convidados que ainda não confirmaram
print("Convidados que ainda não confirmaram:")
for pessoa in nao_confirmados:
    print(pessoa)

#Enviar lembretes aos não confirmados
print("\nEnviando lembretes para os convidados que ainda não confirmaram.")
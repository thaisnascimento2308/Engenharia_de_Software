#Lista de filmes para classificação
filmes = ['Filme 1', 'Filme 2', 'Filme 3', 'Filme 4', 'Filme 5']

#Mensagens de boas vindas
print("Bem-vindo(a) a classificação de filmes!")
print("Você tem cinco filmes para classificar.")
print("Digite '0' a qualquer momento para parar.\n")

for filme in filmes:
    while True:
        classificacao = input(f"Qual nota você daria para o '{filme}' de 1 a 5? (ou 0 para sair): ")
        if classificacao == '0':
            print('Que pena! Você não irá classificar os filmes.')
            break  # Encerra o loop interno com "break"
        
        classificacao = int(classificacao)
        if classificacao < 1 or classificacao > 5:
            print('Por favor, digite uma classificação válida de 1 a 5.')
        else:
            print(f"Você classificou '{filme}' com {classificacao} estrelas.\n")
            break  # Sai do loop interno
print("Obrigada pela participação!")

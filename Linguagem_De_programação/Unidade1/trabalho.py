#Função para cadastrar notas
def cadastrar_notas():
    notas = [] #Lista vazia para adicionar as notas
    while True:
        nota = float(input("Insira a nota do aluno(ou -0 para Sair): ")) #Solicita a nota do aluno
        if nota == -0: #Sistema para sair
            break
        elif 0 <= nota <= 10: #Aceita notas entre 0 e 10
            notas.append(nota) #Adiciona notas a lista
        else:
            print("Nota inválida! Insira um valor entre 0 e 10.") #Erro para nota inválida
    return notas
            
#Função para calcular a média das notas
def calcular_media(notas):
    return sum(notas) / len(notas) if notas else 0

#Função para determinar a situação do aluno
def determinar_situacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

#Função principal para exibir o relatório final
def sistema_notas():
    print("Sistema de Gestão de Notas de Alunos")
    
    notas = cadastrar_notas()
    media = calcular_media(notas)
    
    if notas:  # Verifica se há notas para gerar o relatório
        situacao = determinar_situacao(media)
        print("\nRelatório Final:")
        print(f"Notas inseridas: {notas}")
        print(f"Média: {media:.2f}")
        print(f"Situação: {situacao}")
    else:
        print("Nenhuma nota foi inserida.")

# Executando o sistema
sistema_notas()

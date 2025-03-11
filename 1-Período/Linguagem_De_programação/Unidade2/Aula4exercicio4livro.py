import matplotlib.pyplot as plt

#Classe para representar um livro
class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
    
    def __str__(self):
        return f"{self.titulo} por {self.autor}, Publicado em {self.ano_publicacao}"

#Criar uma lista de livros
biblioteca = []

#Lista para armazenar anos de publicação
anos = []

#Função para adicionar um livro á biblioteca
def adicionar_livro(titulo, autor, ano_publicacao):
    novo_livro = Livro(titulo, autor, ano_publicacao)
    biblioteca.append(novo_livro)
    anos.append(ano_publicacao) #Adiciona o ano á lista anos
    print(f"O livro '{titulo}' foi adicionado a biblioteca.")

#Função para listar todos os livros na biblioteca
def listar_livros():
    print("Livros na biblioteca:")
    for livro in biblioteca:
        print(livro)

#Adicionar alguns livros á biblioteca
adicionar_livro("Dom Quixote", "Miguel de Cervantes", 1605)
adicionar_livro("Orgulho e preconceito", "Jane Austen", 1813)
adicionar_livro("1984", "George Orwell", 1949)
adicionar_livro("Cem anos de solidão", "Gabriel Garcia Marquez", 1967)
adicionar_livro("Apanhador no Campo de Centeio", "J.D. Salinger", 1951)


#Listar todos os livros na biblioteca
listar_livros()

#Criar um gráfico de livros por ano
anos = list(set(anos)) #Remove duplicatas dos anos
anos.sort() #ele ordena a lista anos em ordem crescente, diretamente na lista original (ou seja, ele modifica a própria lista e não retorna uma nova).

#Contagem de livros por ano
contagem_por_ano = [anos.count(ano) for ano in anos]

#Criar um gráfico de linha
plt.plot(anos, contagem_por_ano, marker='o', linestyle='-')
plt.xlabel('Ano de publicação')
plt.ylabel('Numero de livros')
plt.title('Distribuição de Livros na Biblioteca por Ano de Publicção')

#Adicionar rótulos aos pontos de dados
for i, valor in enumerate(contagem_por_ano):
    plt.text(anos[i], valor, str(valor), ha='center', va='bottom')

plt.grid(True)
plt.show()

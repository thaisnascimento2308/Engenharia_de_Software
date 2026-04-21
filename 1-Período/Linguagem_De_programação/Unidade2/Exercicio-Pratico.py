import matplotlib.pyplot as plt

#Classe para representar um livro
class Livro:
    def __init__(self, titulo, autor, genero, quantidade_disponivel):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade_disponivel = quantidade_disponivel
    
    def __str__(self):
        return f"{self.titulo} por {self.autor}, Gênero {self.genero}, quantidade disponivel {self.quantidade_disponivel}."

#Criar uma lista de livros
biblioteca = []

#Função para cadastrar um novo livro á biblioteca
def adicionar_livro(titulo, autor, genero, quantidade_disponivel):
    novo_livro = Livro(titulo, autor, genero, quantidade_disponivel)
    biblioteca.append(novo_livro)

#Função para listar todos os livros na biblioteca
def listar_livros():
    print("Livros na biblioteca:")
    for livro in biblioteca:
        print(livro)

#Função para buscar um livro pelo título
def buscar_livro(titulo):
    for livro in biblioteca:
        if livro.titulo.lower() == titulo.lower():
            return livro
    return None

#Função para gerar gráfico de quantidade de livros por gênero
def gerar_grafico_genero():
    generos = {}
    
    for livro in biblioteca:
        if livro.genero in generos:
            generos[livro.genero] += livro.quantidade_disponivel
        else:
            generos[livro.genero] = livro.quantidade_disponivel
    
    #Gerar o gráfico
    plt.bar(generos.keys(), generos.values())
    plt.xlabel('Gênero')
    plt.ylabel('Quantidade de livros')
    plt.title('Quantidade de Livros por Gênero')
    plt.show()

#Testando o sistema
adicionar_livro("O Senhor dos Anéis", "J.R.R. Tolkien", "Fantasia", 3)
adicionar_livro("1984", "George Orwell", "Distopia", 2)
adicionar_livro("Dom Quixote", "Miguel de Cervantes", "Clássico", 1)
adicionar_livro("Harry Potter", "J.K. Rowling", "Fantasia", 4)
adicionar_livro("Orgulho e preconceito", "Jane Austen", "Romance", 5)

listar_livros()

livro_encontrado = buscar_livro("1984")
if livro_encontrado:
    print(f"\nLivro encontrado: {livro_encontrado}")
else:
    print("\nLivro não encontrado.")

#Gerar gráfico de quantidade de livros por gênero
gerar_grafico_genero()
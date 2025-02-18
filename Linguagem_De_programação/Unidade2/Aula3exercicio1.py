#Define uma classe chamada pessoa.
class Pessoa:
    #o metodo __init__ é um construtor, chamado quando um objeto da classe é criado.
    #Ele inicializa os atributos da classe.
    def __init__(self, nome, idade, genero):
        #Self é uma convenção em Python que se refere á propria instância da classe
        #Os parâmetros nome, idade, genero sao passados durante a criação do objeto.
        #Eles sao usados para inicializar os atributos da instância
        self.nome = nome #Atribui o valor de nome ao atruibuto nome da instância
        self.idade = idade #Atribui o valor de idade ao atruibuto idade da instância
        self.genero = genero #Atribui o valor de genero ao atruibuto genero da instância
    #O metodo cumprimentar retorna uma saudação com o nome da pessoa
    def cumprimentar(self):
        return f"Olá, meu nome é {self.nome}."
    #O metodo aniversario aumenta a idade da pessoa em 1
    def aniversario(self):
        self.idade += 1 #Incrementa
#Cria uma instância da classe "Pessoa" com os valores "João", 30 e "Masculino" para nome, idade e genero, respectivamente.
pessoa1 = Pessoa("João", 30, "Masculino")
#Chama o método "cumprimentar" na instância pessoa1 e imprime a saudação.
print(pessoa1.cumprimentar()) #Saída: Olá, meu nome é João.
#Acessa o atributo idade da instância pessoa1 e imprime sua idade.
print(f"Idade: {pessoa1.idade}") #Saída: Idade:30
#Chama o método "aniversario" na instância pessoa1 para aumentar sua idade em 1.
pessoa1.aniversario()
#Acessa o atributo idade atualizado da instância pessoa1 e imprime a nova idade.
print(f"Nova idade: {pessoa1.idade}") #Saída: Nova idade: 31.
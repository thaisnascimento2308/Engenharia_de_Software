from flask import Flask

#Criação da aplicação Flask
app = Flask(__name__)

#Rota para a página inicial
@app.route('/')
def hello():
    return 'Bem-vindo ao back-end simples com Flask!'

#Executa a aplicação no host e na porta especificados
if __name__ == '__main__':
    app.run(host='localhost', port=5000)
import sqlite3

#1. Conectar ao banco de dados (ou criar umnovo)
#usando a função connect do módulo sqlite3 para se conectar a um banco de dados SQLite
#chamado 'exemplo.db'. Se o banco de dados não existir, ele será criado automaticamente.
conn = sqlite3.connect('exemplo.db')

#2. Criar um objeto cursor
#O cursor é usado para executar comando SQL no banco de dados.
#Ele atua como uma especie de ponteiro que percorre os resultados de consultas.
cursos = conn.cursor()

#3. Definir o comando SQL para criar a tabela
#define uma string create_table que contém um comando SQL para criar uma tabela chamada 'Produtos'.
#Esta tabela terá quatro colunas: id (chave primaria), nome (texto), preco (número real) e estoque (numero inteiro).
#O IF NOT EXISTS garante que a tabela só será criada se ainda não existir
create_table = """
CREATE TABLE IF NOT EXISTS Produtos (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    estoque INTEGER
);
"""

#Usa o método execute do objeto cursos para executar o comando SQL definido anteriormente e criar a tabela no banco de dados.
#4. Executar o comando SQL para cria a tabela
cursos.execute(create_table)

#5. Confirmar as alterações (commit)
#Após a execução bem-sucedida do comando SQL, usa o método commit no objeto de conexão (conn) para confirmar as alterações no banco de dados.
#Isso garante que as alterações sejam efetrivamente aplicadas.
conn.commit()

#6. Fechar a conexão com o banco de dados
#Finalmente, vc usa o método close no objeto de conexão com o banco de dados.
#é uma prática recomendada fechar a conexão após a conclusão das operações, para liberar recursos e evitar possiveis problemas de concorrência.
conn.close()
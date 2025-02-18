#Adicionar produto
import sqlite3

#Conectando ao banco de dados
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()

#Dados do novo produto
novo_produto = ('Camiseta', 19.99, 50) #nome, preco, estoque

#Comando SQL para inserir o novo produto na tabela
inserir_produto = "INSERT INTO Produtos (nome, preco, estoque) VALUES (?, ?, ?)"

#Executando o comando SQL para inserção
cursor.execute(inserir_produto, novo_produto)

#Confirmando as alterações
conn.commit()

#Fechando a conexão
conn.close()

#############################################################3

#Visualizar produto
#Conectando ao banco de dados
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()

#Comando SQL para selecionar todos os produtos
selecionar_produtos = "SELECT * FROM Produtos"

#Executando o comando SQL
cursor.execute(selecionar_produtos)

#Obtendo todos os registros e exebindo-os
produtos = cursor.fetchall()
for produto in produtos:
    print(produto)

#Fechando a conexão
conn.close()

#Saida1
#(1, 'Camiseta', 19.99, 50)

#Saida2
#(1, 'Camiseta', 19.99, 50)
#(2, 'Camiseta', 28.99, 50) #apenas alterando o valor

###################################################3
#Atualizar produto
import sqlite3

#Conectando ao banco de dados
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()

#Novo preço e ID do produto a ser atualizado
novo_preco = 24.99

produto_id = 1 #Suponhamos que queremos atualizar o produto com id 1

#Comando SQL para atualizar o preço do produto
atualizar_preco = "UPDATE Produtos SET preco = ? WHERE id = ?"

#Executando o comando SQL de atualização
cursor.execute(atualizar_preco, (novo_preco, produto_id))

#Confirmando as alterações
conn.commit()

#Fechando a conexão
conn.close()

#################################################################3
#Excluirproduto
import sqlite3

#Conectando ao banco de dados
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()

#ID do produto a ser excluido
produto_id = 1 #Suponhamos que queremos excluir o produto com ID 2

#Comando SQL para excluir o produto
excluir_produto = "DELETE FROM Produtos WHERE id = ?"

#Executando o comando SQL de exclusão
cursor.execute(excluir_produto, (produto_id))

#Confirmando as alterações
conn.commit()

#Fechando a conexão
conn.close()

#Saida
#(2, 'Camiseta', 28.99, 50)
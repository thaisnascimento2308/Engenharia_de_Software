import sqlite3

#Passo1: Conectar ao banco de dados SQLite (ou criá-lo se não exisitr)
conn = sqlite3.connect('funcionarios.db')

#Passo2: Criar a tabela de funcionários
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS funcionarios (
        id INTERGER PRIMAY KEY,
        nome TEXT,
        cargo TEXT,
        salario REAL
    )
''')

#Passo3: Inserir um novo funcionario na tabela
novo_funcionario = (3, 'Eduarda', 'Desenvolvedor', 10000.00)
cursor.execute('INSERT INTO funcionarios VALUES (?, ?, ?, ?)', novo_funcionario)
conn.commit()
#Para adicionar é so alterar o ID, Nome... que ja vai inserindo na tabela

#Passo4: Consultar e exibir funcionários
cursor.execute('SELECT * FROM funcionarios')
funcionarios = cursor.fetchall()
print('Funcionários Cadastrados')
for funcionario in funcionarios:
    print(funcionario)
    
#Passo5: atualizar informações de um funcionario
atualizacao = ('Thais Nascimento', 5500.00, 1)
cursor.execute('UPDATE funcionarios SET nome = ?, salario = ? WHERE id = ?', atualizacao)
conn.commit()

#Passo6: Deletar um funcionario da tabela
id_funcionario_para_deletar = 3
cursor.execute('DELETE FROM funcionarios WHERE id = ?', (id_funcionario_para_deletar,))
conn.commit()
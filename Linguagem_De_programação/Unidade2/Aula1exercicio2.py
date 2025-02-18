#Vamos, agora, colocar em prática o que aprendemos pensando no problema apresentado no início desta aula. Cada venda é registrada como uma tupla com os seguintes elementos: data da venda, nome do produto, quantidade vendida e preço unitário. Essas tuplas são armazenadas em uma lista chamada registros_de_vendas. Além disso, você recebeu uma lista de produtos que precisam ser reabastecidos no estoque, chamada produtos_a_reabastecer. Também é preciso acompanhar o total de vendas de cada produto. Para fazer isso, você deve criar um dicionário chamado total_de_vendas_por_produto, no qual as chaves são os nomes dos produtos, e os valores são os totais de vendas para cada um. Vamos ao código!

registros_de_vendas = [("2024-09-12", "Arroz", 8, 28.90),
                       ("2024-09-12", "Feijão", 5, 8.90),
                       ("2024-09-13", "Fubá", 11, 5.99), 
                       ("2024-09-12", "Farinha", 6, 4.50)]

produtos_a_reabastecer = ["Arroz", "Fubá"]

# Dicionário para armazenar o total de vendas por produto
total_de_vendas_por_produto = {}

# Percorre os registros de vendas
for venda in registros_de_vendas:
    data, produto, quantidade, preco_unitario = venda
    total_venda = quantidade * preco_unitario
    
    # Atualiza o total de vendas por produto
    if produto in total_de_vendas_por_produto:
        total_de_vendas_por_produto[produto] += total_venda
    else:
        total_de_vendas_por_produto[produto] = total_venda
    
    # Verifica se o produto precisa ser reabastecido
    if produto in produtos_a_reabastecer:
        print(f"O produto {produto} precisa ser reabastecido.")

# Exibe o total de vendas por produto
print("Total de vendas por produto:")
for produto, total in total_de_vendas_por_produto.items():
    print(f"{produto}: R${total:.2f}")
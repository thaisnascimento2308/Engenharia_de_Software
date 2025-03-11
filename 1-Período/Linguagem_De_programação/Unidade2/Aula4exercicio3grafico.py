#Suponha que você precisa fazer uma visualização da contagem de venda de um produto hipotético, vamos usar essa aula para construir essa visualização?
import matplotlib.pyplot as grafico

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio']
vendas = [100, 250, 300, 270, 520]

#Criar um gráfico de barras
grafico.bar(meses, vendas, color='green')

#Criar um gráfico em linhas
#grafico.plot(meses, vendas, color='green')

#Adicionar rótulos aos eixos
grafico.xlabel('Mês')
grafico.ylabel('Vendas (em unidade)')

#Adicionar um título ao gráfico
grafico.title('Vendas Mensais')

#Mostrar o gráfico
grafico.show()
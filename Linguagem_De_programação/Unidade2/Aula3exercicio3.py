#Suponha agora, que você, precisa criar um algoritmo que a partir de características imputadas, mostre um resumo e status de um veículo. E ainda, você deve fazer algo semelhante para uma subdivisão dessa classe veículos. Vamos juntos para resolver isso?

class Veiculo:
    def __init__(self, marca, modelo, ano):
        # self é uma convenção em Python que se refere à própria instância da classe.
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0

    def acelerar(self, incremento):
        self.velocidade += incremento

    def frear(self, decremento):
        self.velocidade -= decremento
    
    def status(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Velocidade: {self.velocidade} km/h"

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, potencia):
        super().__init__(marca, modelo, ano)
        self.potencia = potencia
    
    def acelerar(self, incremento):
        #Carros podem acelerar mais rapido
        self.velocidade += incremento + self.potencia

class Bicicleta(Veiculo):
    def __init__(self, marca, modelo, ano, tipo):
        super().__init__(marca, modelo, ano)
        self.tipo = tipo
    
    def status(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Tipo: {self.tipo}, Velocidade: {self.velocidade} km/h"

#Criando objetos
carro1 = Carro("Toyota", "Corolla", 2022, 150)
bicicleta1 = Bicicleta("Trek", "Mountain Bike", 2021, "MTB")

#Acelerando e verificando o status
carro1.acelerar(50)
bicicleta1.acelerar(20)

#Exibindo o status do veiculo
print("Status do Carro:")
print(carro1.status())

print("\nStatus da Bicicleta")
print(bicicleta1.status())
# 1 Crie uma classe chamada Carro com os atributos marca, modelo e ano.
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

# 2 Adicione um método mostrar_info à classe Carro que exiba os detalhes do carro.
    def mostrarInfo(self):
        print(f"Carro: {self.marca} {self.modelo}, Ano: {self.ano}")

# 4 Modifique a classe Carro para incluir um método atualizar_ano que permita ao usuário mudar o ano do carro.
    def atualizarAno(self, novo_ano):
        self.ano = novo_ano
        print(f"Ano atualizado para {self.ano}")

# 3 Crie uma instância da classe Carro e chame o método mostrar_info.
meu_carro = Carro("Toyota", "Corolla", 2020)
meu_carro.mostrarInfo()

# 4 Executar 
meu_carro.atualizarAno(2022)
meu_carro.mostrarInfo()

# 5 Implemente a classe Veiculo com um método mover que exiba uma mensagem genérica "O veículo está se movendo."
class Veiculo:
    def mover(self):
        print("O veículo está se movendo.")
    def tipo(self):
        return "Veículo"

# 6 Faça a classe Carro herdar de Veiculo e sobrescreva o método mover para incluir "O carro está se movendo."
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano):
        super().__init__()
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def mover(self):
        print("O carro está se movendo.")
    def tipo(self):
        return "Carro"

# 7 Crie uma nova classe chamada Moto que também herde de Veiculo e adicione um atributo tipo (ex: esportiva, touring).
class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, tipo):
        super().__init__()
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.tipoMoto = tipo
    
    # 8 Adicione um método mostrar_tipo na classe Moto que exiba o tipo da moto.
    def mostrarTipo(self):
        print(f"Tipo da moto: {self.tipoMoto}")
    def mover(self):
        print("A moto está se movendo.")
    def tipo(self):
        return "Moto"

# 10 Crie uma função chamada mostrar_tipos que aceita uma lista de objetos Veiculo e exibe o tipo de cada veículo usando o método tipo.
def mostrarTipos(veiculos):
    for veiculo in veiculos:
        print(f"Tipo: {veiculo.tipo()}")

# 11 Teste a função mostrar_tipos com uma lista que contém instâncias de Carro e Moto.
carro1 = Carro("Ford", "Fiesta", 2018)
moto1 = Moto("Honda", "Pcx 150", 2019, "Moto")
listaVeiculos = [carro1,moto1]
mostrarTipos(listaVeiculos)

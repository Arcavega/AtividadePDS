class Automovel:
    def __init__(self, marca, modelo, ano):
        self.mcar = marca
        self.mmodelo = modelo
        self.classe = self.__class__.__name__
        self.anocar = ano

    def falardados(self):
        print(f"motor do carro {self.classe}: ", self.mtcar)
        print(f"litros por km do carro {self.classe}: ", self.litro)

        
class Carro:
    def __init__(self,modelo,marca, ano):
        self.__modelo = modelo
        self.__marca = marca
        self.__ano = ano
        self.__disponivel = True
        
    @property
    def modelo(self):
        return self.__modelo
    @property
    def marca(self):
        return self.__marca
    @property
    def ano(self):
        return self.__ano
    @property
    def disponivel(self):
        return self.__disponivel
    
    @disponivel.setter
    def set_disponibilidade(self,status):
        self.disponivel = status
        
    def carro_informacoes(self):
        if self.disponivel:
            return f"Nome: {self.__modelo}\nMarca: {self.__marca}\nAno: {self.__ano}"
        else:
            return f"Nome: {self.__modelo}\nMarca: {self.__marca}\nAno: {self.__ano} (Indisponível)"
    
    
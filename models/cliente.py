class Cliente:
    def __init__(self,nome,cpf,idade):
        self.__nome = nome
        self.__cpf = cpf
        self.__idade = idade
        # self.__senha_hash = None
    @property
    def nome(self):
        return self.__nome
    
    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def idade(self):
        return self.__idade
        
    def exibir_informacoes(self):
        return f"Nome: {self.__nome}\nCPF: {self.__cpf}\nIdade: {self.__idade}"
    
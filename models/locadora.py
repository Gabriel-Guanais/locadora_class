

class Locadora:
    def __init__(self,nome):
        self.nome = nome
        self.carros = []
        self.clientes = [] 
        self.locacao = []
        
 
    def cadastrar_cliente(self,cliente):
        self.clientes.append(cliente)
        print(f"Cliente {cliente.nome} cadastrado com sucesso")
    
    def buscar_cliente(self,cpf):
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                print(cliente.exibir_informacoes())
                return cliente  
        print('Clente nao encontrado')
        return None

    def listar_clientes(self):
        if not self.clientes:
            print("Nenhum cliente encontrado")
        for c in self.clientes:
            print('_'*20)
            print(c.exibir_informacoes())

    def cadastrar_carro(self,carro):
        self.carros.append(carro)
        print(f"Carro {carro.modelo} foi cadastrado com sucesso")
        
    def listar_carro(self):
        if not self.carros:
            print('Nenhum carro encontrado')
        for car in self.carros:
            print("_"*30)
            print(car.carro_informacoes())
        print('_'*30)
        
    def alugar_carro(self):
        for i, carro in enumerate(self.carros):
            print(f"{i}. {carro.modelo}")
            
        usr = input('qual carro voce quer alugar')
        return usr 
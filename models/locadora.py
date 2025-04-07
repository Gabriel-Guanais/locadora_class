

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
                return cliente
        ...
    
    def listar_clientes(self):
        if not self.clientes:
            print("Nenhum cliente encontrado")
        for c in self.clientes:
            print(c.exibir_informacoes())

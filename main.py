import os
from models.cliente import Cliente
from models.locadora import Locadora


def tabela():        
    print('-----Bem vindo a locadoura Simasturbo-----')
    print('|    1-Cadastrar Cliente                 |')
    print('|    2-Listar clientes                   |') #dentro de login colocar a funcao de alugar carro
    print('|    3-Buscar clientes                   |')
    print('|    4-Cadastrar Carro                   |')
    print('|    5-Relatorio                         |')
        
        
        
def main():
    locadora = Locadora("Simasturbo Locadora")
    
    while True:
        tabela()
        opcao = input('Escolha uma opcao: ')
        
        if opcao == "1":
            nome = input("digite o nome do cliente")
            cpf = input("digite o Cpf do cliente")
            idade = int(input("digite a idade do cliente"))

            cliente = Cliente(nome, cpf, idade)
            locadora.cadastrar_cliente(cliente)
            
        elif opcao == "2":
            locadora.listar_clientes()
            
        elif opcao == "3":
            
                
        
            ...
       

if __name__ == "__main__":
    main()
        
        

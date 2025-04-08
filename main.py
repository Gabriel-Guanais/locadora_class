import os
from models.cliente import Cliente
from models.locadora import Locadora
from models.carro import Carro


def tabela():        
    print('\n-----Bem vindo a locadoura Simasturbo-----')
    print('|    1-Cadastrar Cliente                 |')
    print('|    2-Listar clientes                   |') #dentro de login colocar a funcao de alugar carro
    print('|    3-Buscar clientes                   |')
    print('|    4-Cadastrar Carro                   |')
    print('|    5-Lista Carros Disponiveis          |')
    print('|    6-Alugar Carro                      |')
    print('|    6-Relatorio                         |')
    print('------------------------------------------')
        
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')   
        
def main():
    locadora = Locadora("Simasturbo Locadora")
    
    while True:
        tabela()
        opcao = input('Escolha uma opcao: ')
        limpar_terminal()
        
        if opcao == "1":
            print('--Cadastro de Cliente--')
            nome = input("digite o nome do cliente: ")
            cpf = input("digite o Cpf do cliente: ")
            idade = int(input("digite a idade do cliente: "))

            cliente = Cliente(nome, cpf, idade)
            locadora.cadastrar_cliente(cliente)
            
        elif opcao == "2":
            locadora.listar_clientes()
            
        elif opcao == "3":
            print('--Bem Vindo ao Buscador de Cliente--')
            cliente_cpf = input('Digite o CPF do cliente: ').strip()
            locadora.buscar_cliente(cliente_cpf)                
          
        elif opcao == "4":
            print('--Cadastro de Carro--')
            modelo = input('Digite o Modelo:')
            marca = input('Digite o marca:')
            ano = input('Digite o ano:')
            
            carro = Carro(modelo, marca, ano)
            locadora.cadastrar_carro(carro)  
            
        elif opcao == "5":
            locadora.listar_carro() 
        
        elif opcao == "6":
            locadora.alugar_carro() 

if __name__ == "__main__":
    main()
        
        

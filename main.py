from dbm.dumb import error
from distutils import errors
from msilib.schema import Error
import os, time
import re
from poplib import error_proto
import banco.conexao_bd as bd

clientes = []
#produtos = []
#pedidos = []

#Cores

vermelho = '\033[1;31m'
magenta =  '\033[1;35m'
verde = '\033[1;32m'
amarelo = '\033[1;33m'
ciano = '\033[1;96m'
restaura = '\033[m'

def cabecalho():
    texto = f"{verde}BEM VINDO AO LANCHES QUARENTENA{restaura}"
    len_texto = int(len(texto)) - 10
    print('='*len_texto)
    print(texto)
    print('='*len_texto)


def cadastro():
    os.system('cls')
    while True:
        try:
            cabecalho()
            print(f'{amarelo}[Digite as informações do cliente]{restaura}')
            nome = str(input('Nome: '))
            telefone = int(input('Telefone [(47)997202655] +55'))
            if len(str(telefone)) == 11:
                resultado = bd.add_clientes(nome, telefone)
                print(resultado)
                if resultado.__contains__('Concluído'):
                    print(f'{verde}{resultado}{restaura}')
                else:
                    print(f'{vermelho}{resultado}{restaura}')
                opcao = input('Deseja informar mais algum cliente? (S/N): ').strip().lower()
                if (opcao == 'n'):
                    menu()
                    break
                elif (opcao == 's'):
                    cadastro()
            else:
                print(f'{vermelho}Telefone incorreto !, precisa ter 11 digitos com o ddd incluido{restaura}')
                time.sleep(1.5)
                os.system('cls')
        except ValueError:
            print(f'{magenta}Por favor digite um número !{restaura}')
            time.sleep(1.5)
            os.system('cls')

def editar_cliente():
    while True:
        try:
            print(f'''{ciano}
0. Sair
1. Editar Cliente
{restaura}''')
            menu = int(input("Escolha uma opção: "))
            if(menu==1):
                #EDITANDO CLIENTES
                nome = str(input('Digite o nome do cliente: '))
                telefone = int(input('Telefone [(47)997202655] +55'))
                if len(str(telefone)) == 11:
                    nv_nome = ""
                    resultado = bd.editar_cliente(nome, telefone, nv_nome)
                    if resultado == 'ok':
                        print(f'''{ciano}
                        
0. Sair
1. Editar Nome
2. Editar Telefone
3. Excluir Usuário
{restaura}''')
                        menu = int(input("Escolha uma opção: "))
                        if(menu==0):
                            break
                        if(menu==1):
                            nv_nome = str(input('Novo nome:'))
                            resultado = bd.editar_cliente(nome, telefone,'editar')
                            if resultado == 'ok':
                                print('Adicionado com sucesso')
                        if(menu==2):
                            nv_telefone = int(input('Novo telefone +55'))
                            bd.editar_cliente(nome, telefone, nv_telefone)
                        if(menu==3):
                            excluir = 'excluir'
                            resultado = bd.editar_cliente(nome, telefone, excluir)
                            print(f'{verde}{resultado}{restaura}')
                else:
                    print('Numero invalido')

            elif(menu==0):
                print('Programa encerrado, Obrigado!')
                break
    

                        
                
        except ValueError as erro:
            print(f'{vermelho}Por favor digite um número !{restaura}')
            time.sleep(1.5)
            os.system('cls')





def cadProduto():
        os.system('cls')
        while True:
            try:
                cabecalho()
                print(f'{amarelo}[Digite as informações do produto]{restaura}')
                nome_produto = str(input('Nome do produto: '))
                preco_produto = int(input('Preço da Unidade R$'))
                resultado = bd.add_produtos(nome_produto, preco_produto)
                print(f'{verde}{resultado}{restaura}')
                opcao = input('Deseja informar mais algum produto? (S/N): ').strip().lower()
                if (opcao == 'n'):
                        menu()
                        break
                elif (opcao == 's'):
                        cadProduto()                
            except ValueError:
                print(f'{magenta}Por favor o preço do produto está incorreto !{restaura}')
                time.sleep(1.5)
                os.system('cls')
            

def cadPedido():
    os.system('cls')
    while True:
        try:
            cabecalho()
            print(f'{amarelo}[Digite as informações do pedido]{restaura}')
            nome_cliente = str(input('seu nome: '))
            nome_produto = str(input('nome do produto: '))
            quantidade_produto = int(input('quantidade produto: '))
            resultado = bd.add_pedidos(nome_cliente, nome_produto, quantidade_produto)
            if resultado.__contains__('Concluído'):
                print(f'{verde}{resultado}{restaura}')
            else:
                print(f'{vermelho}{resultado}{restaura}')
            opcao = input('Deseja informar mais algum produto? (S/N): ').strip().lower()
            if (opcao == 'n'):
                menu()
                break
            elif (opcao == 's'):
                    cadProduto()
        except ValueError:
                print(f'{magenta}Por favor o preço do produto está incorreto !{restaura}')
                time.sleep(1.5)
                os.system('cls')

        # Pedido só será registrado se o cliente existir.
        
        opcao = input('Deseja informar mais algum pedido? (S/N): ').strip().lower()
        if (opcao == 'n'):
            menu()
        elif (opcao == 's'):
            cadPedido()

def mostrarClientes():

    os.system('cls')
    cabecalho() 
    resultado = bd.mostrar_clientes()

def mostrar_soma():
    os.system('cls')
    cabecalho() 
    resultado = bd.soma_faturados()

def mostrarProdutos():

    os.system('cls')
    cabecalho() 
    resultado = bd.mostrar_produtos()

def total_pedido_cliente():

    os.system('cls')
    cabecalho() 
    resultado = bd.soma_pedidos()

def total_pedido_produto():
    os.system('cls')
    cabecalho() 
    resultado = bd.soma_pedidos_produto()    


  
def menu():
    os.system('cls')
    cabecalho()
    while True:
        print(f'''{ciano}
0. Sair
1. Cadastro Cliente
2. Cadastro Produto
3. Cadastro Pedido
4. Mostrar Clientes
5. Mostrar Produtos
6. Editar Cliente
7. Valor total de pedidos para cada cliente
8. Quantidade total de pedidos para cada produto
9. Valor total em reais faturados até o momento{restaura}''')

        try:
            menu = int((input("Escolha uma opção: ")))
            if(menu==1):
                cadastro()
            elif(menu==2):
                cadProduto()
            elif(menu==3):
                cadPedido()
            elif(menu==4):
                mostrarClientes()
            elif(menu==5):
                mostrarProdutos()
            elif(menu==6):
                editar_cliente()
            elif(menu==7):
                total_pedido_cliente()
            elif(menu==8):
                total_pedido_produto()
            elif(menu==9):
                mostrar_soma()
            elif(menu==0):
                print('Programa encerrado, Obrigado!')
                break
            
        except ValueError as erro:
            print(f'{vermelho}Por favor digite um número !{restaura}')
            time.sleep(1.5)
            os.system('cls')
menu()
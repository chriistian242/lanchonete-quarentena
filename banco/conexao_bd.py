from ast import Delete
from msilib.schema import Error
from multiprocessing.dummy import current_process
from shutil import ExecError
import sqlite3

#ABRINDO CONEXAO BD

banco = sqlite3.connect("econocom.db")
cursor = banco.cursor()


def add_clientes(nome, telefone):

    nome = str(nome)
    telefone = int(telefone)
    #ADICIONADO NO BANCO DE DADOS
    try:
        #ADICIONA USUARIO NA TABELA CLIENTES
        cursor.execute(f'INSERT INTO tb_clientes VALUES("{nome}", {telefone})')
        banco.commit()
        return 'Concluído !'
    except Exception as erro:
        return erro


def add_produtos(nome_produto, preco_produto):

    #ADICIONADO NO BANCO DE DADOS
    try:
        #ADICIONA PRODUTO NA TABELA CLIENTES
        cursor.execute(
            f'INSERT INTO tb_produtos VALUES("{nome_produto}", {preco_produto})'
        )
        banco.commit()
        return 'Concluído !'
    except Exception as erro:
        return erro

def add_pedidos(nome_cliente, nome_produto, quantidade_produto):
    try:
        #ADICIONA PRODUTO NA TABELA PEDIDOS
        cursor.execute(
            f'INSERT INTO tb_pedidos VALUES("{nome_cliente}", "{nome_produto}", {quantidade_produto})'
        )
        banco.commit()
        return 'Concluído !'
    except Exception as erro:
        return erro

def editar_cliente(nome, telefone, edit_cliente):

    nome = str(nome)
    telefone = int(telefone)

    try:
        if type(edit_cliente) != "" and type(edit_cliente) == str:  #NOME
            print('cheguei aqui')
            return 'ok'
    except Exception as erro:
        return erro


#  if type(edit_cliente) == int: #TELEFONE

    try:
        #PROCURANDO ELEMENTO BANCO DE DADOS
        if edit_cliente == "editar":
            cursor.execute(f'SELECT * FROM tb_clientes WHERE nome = "{nome}"')
            dados = cursor.fetchone()
            resultado = validar_cliente(dados)

            if resultado == 'null':
                return 'Esse usuário não existe'
            else:
                nome_cliente = resultado[0]
                telefone_cliente = resultado[1]
                cursor.execute(
                    f'UPDATE tb_clientes SET nome="{nome_cliente}" WHERE nome="{nome}"'
                )
                banco.commit()
                return 'ok'

            if telefone_cliente != telefone:
                return 'Telefone incorreto !'
            else:
                return 'ok'
    except sqlite3.Error as erro:
        return f'Ocorreu um erro: {erro}'


def mostrar_clientes():
    try:
        cursor.execute('SELECT * FROM tb_clientes')
        dados = cursor.fetchall()
        banco.commit()
        for dado in dados:
            print(f'{dado[0]} - {dado[1]}')
        banco.close
    except Exception as erro:
        return erro

#

#
#

#

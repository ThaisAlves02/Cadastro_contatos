"""
database.py
------------
Responsável por TUDO que envolve ler e escrever no arquivo JSON.
A interface (main.py) nunca deve mexer diretamente no arquivo,
sempre chama as funções daqui.
"""

import json
import os

ARQUIVO = "contatos.json"


def carregar_contatos():
    """
    Lê o arquivo JSON e retorna uma lista de contatos.
    Se o arquivo não existir ainda, retorna uma lista vazia.

    TODO (fazer com a turma):
    1. Verificar se o arquivo existe (os.path.exists)
    2. Se não existir, retornar []
    3. Se existir, abrir o arquivo, usar json.load() e retornar o conteúdo
    """
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO,'r',encoding='utf-8') as contatos:
        return json.load(contatos)


def salvar_contatos(lista_contatos):
    """
    Recebe a lista completa de contatos e regrava o arquivo JSON.
    É chamada sempre depois de adicionar, editar ou excluir.

    TODO (fazer com a turma):
    1. Abrir o arquivo em modo escrita ("w")
    2. Usar json.dump() para salvar a lista_contatos
       (dica: usar indent=4 para o arquivo ficar legível)
    """
    with open(ARQUIVO,'w',encoding='utf-8') as contatos:
        json.dump(lista_contatos,contatos,indent=4,ensure_ascii=False)


def adicionar_contato(nome, telefone, email):
    """
    Cria um novo contato e adiciona na lista existente.

    TODO (fazer com a turma):
    1. Carregar a lista atual (carregar_contatos)
    2. Criar um dicionário: {"nome": nome, "telefone": telefone, "email": email}
    3. Adicionar (append) esse dicionário na lista
    4. Salvar a lista atualizada (salvar_contatos)
    """
    contatos = carregar_contatos()
    
    novo_contato = {
        "nome": nome,
        "telefone": telefone,
        "email":email
    }
    
    contatos.append(novo_contato)
    salvar_contatos(contatos)
    


def atualizar_contato(indice, nome, telefone, email):
    """
    Atualiza um contato já existente, dado seu índice na lista.

    TODO (fazer com a turma):
    1. Carregar a lista atual
    2. Substituir o item na posição 'indice' pelos novos dados
    3. Salvar a lista atualizada
    """
    pass


def excluir_contato(indice):
    """
    Remove um contato da lista, dado seu índice.

    TODO (fazer com a turma):
    1. Carregar a lista atual
    2. Remover o item na posição 'indice' (lista.pop(indice) ou del lista[indice])
    3. Salvar a lista atualizada
    """
    pass
#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho
import os, subprocess, random, socket

def conexao(meuIP):
    # servidor
    f=open('private_key.txt','r')
    chave_privada=f.read()
    print(chave_privada)
    print('Servidor rodando')
    while True:
        porta=6064

        socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_obj.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # se der ctrl + c, ele para de escutar na porta
        socket_obj.bind((meuIP, porta))
        socket_obj.listen(1) # escuta apenas 1 "vitma"
        #os.system('clear')
        conexao,endereco=socket_obj.accept()

        # ao se conectar, envia a chave privada (S)
        conexao.send(str(chave_privada))
        # recebeu do cliente o ID

        print(recebido)


conexao('127.0.0.1')

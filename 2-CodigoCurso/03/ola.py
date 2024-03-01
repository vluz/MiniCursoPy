#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def diz_ola(nome):
    if nome == '':
        print("Não entrou o seu nome!")  # Imprimir mensagem se o nome estiver vazio
    else:
        print('Olá...')  # Imprimir mensagem de saudação
        
    for letter in nome:
        print(letter)  # Imprimir cada letra do nome

while True:
    nome = input('Entre o seu nome: ')
    diz_ola(nome)  # Chamar a função diz_ola para cumprimentar o usuário
    print("\n")
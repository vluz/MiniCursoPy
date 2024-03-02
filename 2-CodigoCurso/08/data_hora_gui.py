#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
from tkinter import *
from tkinter.ttk import *

def atualiza():
    """
    Atualiza o texto com a data e hora atuais.
    """
    hoje = time.strftime("%d-%m-%y")
    agora = time.strftime("%H:%M:%S")
    mostrador.config(text=hoje + "\n" + agora)
    mostrador.after(1000, atualiza)

# Criar uma nova janela utilizando a biblioteca Tkinter
janela = Tk()

# Definir o título da janela
janela.title("DATA E HORA")

# Criar um widget para exibir dados com a fonte, fundo e cor especificados
mostrador = Label(janela, font=("",60), background="black", foreground="red")

# Empacotar o widget no centro da janela
mostrador.pack(anchor="center")

atualiza()  # Inicia o processo de atualização

mainloop()


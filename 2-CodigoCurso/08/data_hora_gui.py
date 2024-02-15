import time
from tkinter import *
from tkinter.ttk import *


def atualiza():
    hoje = time.strftime("%d-%m-%y")
    agora = time.strftime("%H:%M:%S")
    mostrador.config(text=hoje + "\n" + agora)
    mostrador.after(1000, atualiza)


janela = Tk()
janela.title("DATA E HORA")

mostrador = Label(janela, font=("",60), background="black", foreground="red")
mostrador.pack(anchor="center")

atualiza()

mainloop()
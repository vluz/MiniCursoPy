#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time


# Imprimir data e hora
print("=== DATA E HORA ===")
while True:
    # Obter data e hora atual
    hoje = time.strftime("%d-%m-%Y")
    agora = time.strftime("%H:%M:%S")
    # Imprimir data e hora com retorno do carro para rescrever a linha
    print(hoje + " " + agora, end="\r")
    time.sleep(1)
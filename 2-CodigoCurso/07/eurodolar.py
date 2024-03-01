#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
from pprint import pprint


# Obter a cotações do Euro
response = requests.get("https://open.er-api.com/v6/latest/EUR")
# pprint(response.json())  # Descomente esta linha para imprimir o JSON de resposta completo
exchange_rate = response.json()['rates']['USD']
print("\nUm Euro vale " + str(round(exchange_rate,3)) + " Dólares.\n")

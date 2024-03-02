#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import json


def get_metro_status():
    """
    Obtém o estado das linhas do Metro de Lisboa a partir da API e imprime o estado de cada linha.
    """
    response = requests.get("https://app.metrolisboa.pt/status/getLinhas.php")
    response_json = json.loads(response.text)
    data = response_json["resposta"]

    # Imprime o estado de cada linha
    print("*Metro de Lisboa*\nEstado das linhas")
    print(f"  Amarela  : {data['amarela'].strip()}")
    print(f"  Azul     : {data['azul'].strip()}")
    print(f"  Verde    : {data['verde'].strip()}")
    print(f"  Vermelha : {data['vermelha'].strip()}")

get_metro_status()


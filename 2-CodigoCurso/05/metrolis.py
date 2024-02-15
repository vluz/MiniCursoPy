import requests
import json
import time


resposta = requests.get("https://app.metrolisboa.pt/status/getLinhas.php")
respjson = json.loads(resposta.text)
dados = respjson["resposta"]

# print(dados)

print("*Metro de Lisboa*\nEstado das linhas")
print(f"  Amarela  : {dados['amarela'].strip()}")
print(f"  Azul     : {dados['azul'].strip()}")
print(f"  Verde    : {dados['verde'].strip()}")
print(f"  Vermelha : {dados['vermelha'].strip()}")
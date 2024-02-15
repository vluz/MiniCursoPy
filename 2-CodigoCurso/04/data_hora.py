import time


print("=== DATA E HORA ===")
while True:
    hoje = time.strftime("%d-%m-%Y")
    agora = time.strftime("%H:%M:%S")
    print(hoje + " " + agora, end="\r")
    time.sleep(1)
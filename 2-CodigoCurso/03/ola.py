def diz_ola(nome):
    if nome == '':
        print("Não entrou o seu nome!")
    else:
        print('Olá...')
    
    for letter in nome:
        print(letter)

while True:
    nome = input('Entre o seu nome: ')
    diz_ola(nome)
    print("\n")

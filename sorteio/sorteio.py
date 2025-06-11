import random

def participantes():
    numPessoas = input("Qual a quantidade de pessoas participando? ")
    if numPessoas.isdigit():
        numPessoas = int(numPessoas)
        print(f"Teremos {numPessoas} participantes.\n")
    else:
        print("Coloque um numero valido!!!")

    nomes = []

    print("Quais os nomes dos participantes?")
    for i in range(numPessoas):
        nome = input({i+1})
        nomes.append(nome)
    print("\nOs nomes dos participantes são:")
    for i, nome in enumerate(nomes):
        print(f"{i+1}. {nome}")
    randomnumber = random.randint(0, numPessoas)
    print (F"O nome sorteado foi {nomes[randomnumber]}.Parabens!!!!")

print("===Bem vindo ao sorteio===\n")
participantes()



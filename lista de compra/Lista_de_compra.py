lista =[]

def mostraMenu():
    print("\n ====Lista de Compras====\n")
    print("1.Adcionar Item: ")
    print("2.Ver Lista: ")
    print("3.Remover item da lista: ")
    print("4.Sair")

def AdcionarItem():
    item = input("Qual item deseja adicionar:")
    lista.append(item)
    print(f"O Item {item} foi adicionado a lista.")
    resposta = input("Deseja Adicionar mais um item?(S/N) ")
    if resposta == "s" and "S":
       AdcionarItem()
    else :
       mostraMenu()

def VerLista():
    if not lista:
     print ("Lista esta Vazia")
    else:
     print("Ver item na lista:")
     for i,item in enumerate (lista):
        print(f"{i+1} . {item}")

def RemoverItem():
   VerLista()
   indice = int(input(f"Qual item deseja Remover? "))
   if 0 <= indice < len(lista):
      removido = lista.pop(indice)
      print(f"O item '{removido}' foi removido da lista.")
      respostaDois = str(input("Deseja Remover outro item?(S/N) "))
      if respostaDois == "s" or "S":
         RemoverItem()
      else respostaDois == "n" or "N":
        print("Opção Invalida") 
   else:
    print("Nao tem item nessa numeração!!!")

   
def Sair():
    print("Saindo...") 

while True:
    mostraMenu()
    opcao = input("Qual a Opção: ")
    if opcao == "1":
        AdcionarItem()
    elif opcao == "2":
        VerLista()
    elif opcao == "3":
       RemoverItem()
    elif opcao == "4":
        Sair()
        break
    else:
        print("Opção Invalida")

    






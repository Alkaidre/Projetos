import random
pontuacao = 0
pontuacao2 = 0
empate = 0
ninguemAcertou = 0
pcescolha = 0
opescolha = 0
numero = 0
opçoes = ["i" ,"p"]

while True:
    opescolha = input("""                Vamos a um jogo de Impar ou Par diferente
                no qual você jogara contra o seu proprio PC,
                ele vai escolher um numero de 0 ate 100, e
                voce tem que acerta se e impar ou par. 
                Caso queira sair do jogo aperte(Q),
                Qual a sua escolha (I/P) ?  """).lower()
    if opescolha == 'q':
        break
    if opescolha not in opçoes:
        print("Escolha inválida. Digite apenas I, P ou Q.")
        continue
        
    numero = random.randint(0, 100)
    pcescolha = random.choice(opçoes)
    
    resultado = "i" if numero % 2 != 0 else "p"
    if opescolha == resultado and pcescolha != resultado:
        pontuacao += 1
        print("\nVocê GANHOUUUU!!!\n")
        continue
    elif opescolha != resultado and pcescolha == resultado:
        pontuacao2 += 1
        print("\nO PC ganhou... Boa sorte na proxima.\n")
        continue
    elif opescolha == resultado and pcescolha == resultado:
        empate += 1
        print("\nEmpatouuuu!!!\n") 
        continue
    else:
        ninguemAcertou += 1
        print("\nXIII, niguem acertou essa?\n")
        continue
    
print(f"\nVocê fez {pontuacao} e o pc {pontuacao2}\n e empantou {empate} e parece que ninguem acertou {ninguemAcertou} vezes")        
print("\nObrigado por jogar ate a proxima!!!\n")
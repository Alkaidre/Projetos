def geografia():
    pontos = 0
    respA = input("""Qual o maior oceano do mundo?
            1) Oceano Atlântico
            2) Oceano Índico
            3) Oceano Pacífico 
            4) Oceano Ártico
            -""")
    if respA != "3":
        print ("Resposta errada...")
    else :
        pontos += 1
        print("""   Resposta CERTA !!!
        Vamos para proxima pergunta\n""")
        
    respB = input("""Qual é o país com o maior território do planeta?

            1) Estados Unidos  
            2) China  
            3) Rússia 
            4) Canadá
            -   """)
    if respB != "3":
        print ("Resposta errada...")
    else :
        pontos += 1
        print("""   Resposta CERTA !!!
                 Vamos para proxima pergunta\n""")
        
    respC = input("""Qual continente possui o maior número de países?

            1) América do Sul  
            2) África   
            3) Europa  
            4) Ásia
            - """)
    if respC != "2":
        print ("Resposta errada...")
    else :
        pontos += 1
        print("""   Resposta CERTA !!!
                 Vamos para proxima pergunta\n""")
        
    respD = input("""Qual é a montanha mais alta do mundo?

            1) Monte Kilimanjaro  
            2) Monte Fuji  
            3) Monte Everest   
            4) Mont Blanc
            - """)
    if respD != "3":
        print ("Resposta errada...")
    else :
        pontos += 1
        print("""   Resposta CERTA !!!
                 Acabou as perguntas""")

    print(f"\nVocê acertou {pontos} de 4 perguntas.\n")  

    resposta = input("Gostaria de testar os outros assuntos (S/N)?").lower()
    if resposta != "s":
        print ("Ok ate a proxima!!!")
    else :
        print("""  Devolta ao menu então!!!""")
        
        menu()   
def historia():
    respA = input("""Quem foi o primeiro presidente do Brasil?
            1)Juscelino Kubitschek
            2)Marechal Deodoro da Fonseca
            3)Getúlio Vargas
            4)Dom Pedro II
            - """)
    if respA != "2":
        print ("Resposta errada...")
    else :
        print("""   Resposta CERTA !!!
        Vamos para proxima pergunta\n""")

    respB = input("""Em que ano aconteceu a Proclamação da República no Brasil?
            1)1822
            2)1888
            3)1889
            4)1891
            - """)
    if respB != "3":
        print ("Resposta errada...")
    else :
        print("""   Resposta CERTA !!!
        Vamos para proxima pergunta\n""")

    respC = input("""Qual acontecimento deu início à Segunda Guerra Mundial?
            1) Ataque ao Pearl Harbor
            2) Invasão da Alemanha à Polônia
            3) Batalha de Stalingrado 
            4) Criação da ONU
            - """)
    if respC != "2":
        print ("Resposta errada...")
    else :
        print("""   Resposta CERTA !!!
        Vamos para proxima pergunta\n""")
    respD = input("""Quem assinou a Lei Áurea no Brasil?
            1) Dom Pedro I
            2) Marechal Deodoro
            3) Princesa Isabel
            4) Getúlio Vargas
            - """)
    if respD != "3":
        print ("Resposta errada...")
    else :
        print("""   Resposta CERTA !!!
        Vamos para proxima pergunta\n""")
    resposta = input("Gostaria de testar os outros assuntos (S/N)?").lower()
    if resposta != "s":
        print ("Ok ate a proxima!!!")
    else :
        print("""  Devolta ao menu então!!!""")
        menu()  
def anime():
    respA = input("""Qual o nome do protagonista de "Naruto"?
            1)Sasuke Uchiha
            2)Naruto Uzumaki
            3)Kakashi Hatake
            4)Itachi Uchiha
            - """)
    if respA != "2":
        print ("Resposta errada...")
    else :
        print("""   Resposta CERTA !!!
        Vamos para proxima pergunta\n""")

    respB = input("""Em "Dragon Ball Z", qual é a transformação mais poderosa de Goku (até Dragon Ball Super)?
            1)Super Saiyajin 1
            2)Super Saiyajin 3
            3)Super Saiyajin Blue
            4)Instinto Superior
            - """)
    if respB != "4":
        print ("Resposta errada...")
    else :
        print("""   Resposta CERTA !!!
        Vamos para proxima pergunta\n""")

    respC = input("""Qual o nome do titã que Eren se transforma em "Attack on Titan"?
            1) Titã Fêmea
            2) Titã Colossal
            3) Titã de Ataque
            4) Titã Bestial
            - """)
    if respC != "3":
        print ("Resposta errada...")
    else :
        print("""   Resposta CERTA !!!
        Vamos para proxima pergunta\n""")
    respD = input("""Em "One Piece", qual é o sonho de Luffy?
            1) Encontrar todos os mares
            2) Encontrar o One Piece
            3) Ser o maior espadachim
            4) Ser o rei dos piratas
            - """)
    if respD != "4":
        print ("Resposta errada...")
    else :
        print("""   Resposta CERTA !!!
        Vamos para proxima pergunta\n""")
    resposta = input("Gostaria de testar os outros assuntos (S/N)?").lower()
    if resposta != "s":
        print ("Ok ate a proxima!!!")
    else :
        print("""  Devolta ao menu então!!!""")
        menu()  
def animais():
    respA = input("""Qual é o maior animal terrestre do mundo?
            1) Rinoceronte
            2) Urso Polar
            3) Elefante Africano
            4) Girafa
            - """)
    if respA != "3":
        print ("Resposta errada...")
    else :
        print("""   Resposta CERTA !!!
        Vamos para proxima pergunta\n""")

    respB = input("""Qual desses animais é conhecido por sua habilidade de mudar de cor?
            1) Camaleão
            2) Leão-marinho
            3) Cavalo-marinho
            4) Jacaré
            - """)
    if respB != "1":
        print ("Resposta errada...")
    else :
        print("""   Resposta CERTA !!!
        Vamos para proxima pergunta\n""")

    respC = input("""Qual desses animais é um mamífero marinho?
            1) Tubarão
            2) Polvo
            3) Golfinho
            4) Cavalo-marinho
            - """)
    if respC != "3":
        print ("Resposta errada...")
    else :
        print("""   Resposta CERTA !!!
        Vamos para proxima pergunta\n""")
    respD = input("""uantas patas tem uma aranha?
            1) 6
            2) 8
            3) 10
            4) 4
            - """)
    if respD != "2":
        print ("Resposta errada...")
    else :
        print("""   Resposta CERTA !!!
        Vamos para proxima pergunta\n""")
    resposta = input("Gostaria de testar os outros assuntos (S/N)?").lower()
    if resposta != "s":
        print ("Ok ate a proxima!!!")
    else :
        print("""  Devolta ao menu então!!!""")
        menu()  
def menu():    
    assunto = input("""Sobre qual assunto gostaria de responder o Quiz?
                Temos: 1- Geografia
                       2- Historia         
                       3- Anime
                       4- Animais
                Qual a sua escolha? """)
    if assunto == "1":
        print("Voce escolheu Geografia!!!")
        geografia()
    elif assunto == "2":
        print("Voce escolheu Historia!!!")
        historia()
    elif assunto == "3":
        print("Voce escolheu Anime!!!")
        anime()
    elif assunto == "4":
        print("Voce escolheu Animais!!!")
        animais()
    else:
        print("Opçcao Invalida")

print("===Bem Vindo ao Quiz===")
name = input("Qual o seu nome ? ")
print(f"Bem vindo(a) ao Quiz {name}.")
menu()

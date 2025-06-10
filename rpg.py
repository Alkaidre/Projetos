import random

herois = "herois.txt"
chefe = "chefe.txt"
hp_heroi = 200
hp_chefe = 200

def gerreiro():
    print("""\nO Guerreiro: Força Inabalável
Com o clangor do aço em seus ouvidos e a terra tremendo sob seus pés, 
          você empunha a força bruta como sua maior arma. Treinado nas artes da guerra e forjado em batalhas incontáveis, 
          o Guerreiro é a muralha que protege os inocentes, o escudo que se ergue contra a escuridão. 
          Sua honra é seu guia, e sua coragem, inquebrável.
\n""")

def mago():
    print("""\nO Mago: Conhecimento e Poder
O ar crepita com a energia primordial enquanto você invoca as forças elementais a seu comando.
          O Mago é um estudioso das artes arcanas, um canal para o poder bruto do universo. 
          Seus feitiços podem curar ou destruir, proteger ou aprisionar. 
          A sabedoria é sua fortaleza, e a magia, sua maior arma.\n""")
    
def ladrao():
    print("""\nO Ladrão: Sombra e Subterfúgio
Nas vielas escuras e nos becos esquecidos, você se move como uma sombra, a lâmina afiada e os dedos ágeis. 
          O Ladrão é mestre da furtividade, do engano e da astúcia, 
          capaz de desvendar segredos e desarmar armadilhas com uma graciosidade mortal. 
          O perigo é seu playground, e a riqueza, sua recompensa.\n""")

def ataque_gerreiro():
    global hp_chefe
    print("\nCom um grito de guerra estrondoso, você avança, seu machado (ou espada) brilhando com a luz da coragem.\n")
    print("\nO metal pesado atinge Mor'Draal com força brutal, fazendo-o cambalear por um instante!\n")
    hp_chefe -= 15 
    print(f"\n Seu ataque causou -15 no Necromante ficando com {hp_chefe} HP\n")
    print("\nApesar do golpe, o Necromante ri, uma aura pútrida emanando dele.\n")
    hp_chefe += 15
    print(f"\nHp do Necromante {hp_chefe}")

def ataque_mago():
    global hp_chefe
    print("\nVocê ergue as mãos, e runas arcanas brilham no ar. Uma bola de fogo crepitante (ou um raio gélido) se forma em suas palmas.\n")
    print("\nCom um comando, o feitiço voa, explodindo contra Mor'Draal com um impacto mágico!\n")
    hp_chefe -= 15 
    print(f"\n Seu ataque causou -15 no Necromante ficando com {hp_chefe} HP\n")
    print("\nA energia arcana o envolve por um momento, mas ele dissipa a magia com um aceno displicente, seus olhos frios fixos em você.\n")
    hp_chefe += 15
    print(f"\nHp do Necromante {hp_chefe}")

def ataque_ladrao():
    global hp_chefe
    print("\nDesaparecendo nas sombras com uma agilidade sobrenatural, você se move para flanquear Mor'Draal.\n")
    print("\nSua adaga cintila antes de desferir um golpe rápido e preciso em um ponto vital.\n")
    hp_chefe -= 15 
    print(f"\n Seu ataque causou -15 no Necromante ficando com {hp_chefe} HP\n")
    print("\nO Necromante sente o corte, mas ele se cura rapidamente, a carne morta se unindo. Ele murmura algo sobre sua 'ousadia tola'.\n")
    hp_chefe += 15
    print(f"\nHp do Necromante {hp_chefe}")

def necromante():
    global hp_heroi
    print("\n--- CONTRA-ATAQUE DE MOR'DRAAL! ---")
    print("Mor'Draal estende uma mão esquelética, e uma nuvem de miasma pútrido (ou um raio sombrio) se lança em sua direção!")
    print(f"Você sente sua energia sendo drenada. Você sofre -40 de dano!")
    hp_heroi -= 40
    print(f"Seu HP atual: {hp_heroi}")

def ataque_heroi_random(play1):
   global hp_chefe
   dano_min_heroi = 20
   dano_max_heroi = 50
   dano_causado = random.randint(dano_min_heroi, dano_max_heroi)

   if play1 == "g":
        print("Você desfere um ataque poderoso com sua arma!")
   elif play1 == "m":
        print("Um feitiço crepita de suas mãos e atinge o chefe!")
   elif play1 == "l":
        print("Você se move com furtividade para atacar o Necromante!")

   hp_chefe -= dano_causado
   hp_chefe = max(0, hp_chefe)
   print(f"Seu ataque causou {dano_causado} de dano ao Necromante!")
   print(f"HP de Mor'Draal: {hp_chefe}\n")
    
   if hp_chefe > 0:
       print("O Necromante se enfurece com seu golpe!")
    
   if hp_chefe > 0: 
       print("Apesar do golpe, o Necromante ri, uma aura pútrida emanando dele.")

def ataque_necromante():
    global hp_heroi
    
    dano_min_chefe = 20
    dano_max_chefe = 35
    dano_sofrido = random.randint(dano_min_chefe, dano_max_chefe)

    print("\n--- CONTRA-ATAQUE DE MOR'DRAAL! ---")
    print("Mor'Draal estende uma mão esquelética, e uma nuvem de miasma pútrido (ou um raio sombrio) se lança em sua direção!")
    print(f"Você sente sua energia sendo drenada. Você sofre {dano_sofrido} de dano!")
    
    hp_heroi -= dano_sofrido
    hp_heroi = max(0, hp_heroi)
    print(f"Seu HP atual: {hp_heroi}\n")  

try:
    with open(herois, 'r', encoding='utf-8') as arquivo:
        herois = arquivo.read()
        print(herois)
except FileNotFoundError:
    print(f"Erro: O arquivo '{herois}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro ao ler o arquivo: {herois}")

play1 = input(f"A cidade de Silverwood aguarda sua escolha. Qual lenda você está pronto para forjar?(G/M/L)").lower()

if play1 == "g":
    print("\nOtima escolha, voce e o mais novo Guerreiro em Silverwood!!!\n")
    gerreiro()
elif play1 == "m":
    print("\nOtima escolha, voce e o mais novo Mago em Silverwood!!!\n")
    mago()
elif play1 == "l":
    print("\nOtima escolha, voce e o mais novo Ladrão em Silverwood!!!\n")
    ladrao()
else:
    print("\nEscolha corretamente, o seu destino esta dentro de um desses três caminhos...\n")

print("\n--- O Mal Se Revela ---\n")

try:
    with open(chefe, 'r', encoding='utf-8') as arquivo:
        chefe = arquivo.read()
        print(chefe)
except FileNotFoundError:
    print(f"Erro: O arquivo '{chefe}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro ao ler o arquivo: {chefe}")

print("\nA jornada começa!")

if play1 == "g":
    print("\nChegando ao campo de batalha, voce sente que e o unico guerreio capaz de salvar Silverwood!!!\n")
    ataque_gerreiro()
elif play1 == "m":
    print("\nChegando ao campo de batalha, voce sente que e o unico mago capaz de salvar Silverwood!!!\n")
    ataque_mago()
elif play1 == "l":
    print("\nChegando ao campo de batalha, voce sente que e o unico ladrao capaz de salvar Silverwood!!!\n")
    ataque_ladrao()

print("\n O heroi se prepara o contra ataque do Necromante!!!\n")
necromante()

print("\n--- BATALHA CONTRA O NECROMANTE MOR'DRAAL! ---\n")

while hp_heroi > 0 and hp_chefe > 0:
    print(f"\n--- Status Atual ---")
    print(f"Seu HP: {hp_heroi} | HP de Mor'Draal: {hp_chefe}")
    input("\nPressione ENTER para atacar Necromante...")

    ataque_heroi_random(play1)

    if hp_chefe <= 0:
        print("\nCom um último e poderoso golpe, Mor'Draal cambaleia, sua aura pútrida se dissipa. Seu corpo esquelético desmorona em pó, e o silêncio finalmente toma conta do campo de batalha.")
        print("A escuridão se retrai, e os céus de Silverwood se abrem, banhando a terra com uma luz renovada.")
        print("PARABÉNS, HERÓI! VOCÊ SALVOU SILVERWOOD DA RUÍNA DE MOR'DRAAL!")
        break 

    print("\nMor'Draal se recompõe, sua fúria crescente.")
    ataque_necromante()

    
    if hp_heroi <= 0:
        print("\nSua visão escurece, o último golpe de Mor'Draal é esmagador. Você cai, sentindo a esperança se esvair de Silverwood.")
        print("A risada gélida do Necromante ecoa, e a escuridão avança, consumindo tudo.")
        print("VOCÊ FOI DERROTADO! SILVERWOOD CAIU SOB O DOMÍNIO DE MOR'DRAAL.")
        break 

print("\n--- Fim da Batalha ---")
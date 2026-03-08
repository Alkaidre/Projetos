import random
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.metrics import dp
from kivy.uix.scrollview import ScrollView

class StartScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=dp(40), spacing=dp(20), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.label = Label(text="Vamos jogar RPG!\nSalve Silverwood!", halign='center', font_size=dp(24), bold=True, color=[1, 1, 1, 1])
        self.button = Button(text="Começar", size_hint=(0.8, 0.2), pos_hint={'center_x': 0.5})
        self.button.bind(on_press=self.go_to_main_screen)
        
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.button)
        self.add_widget(self.layout)

    def go_to_main_screen(self, instance):
        self.manager.current = 'main'

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(10))

        file_path = os.path.join(os.path.dirname(__file__), "herois.txt")

        try:
            with open(file_path, 'r', encoding='utf-8') as arquivo:
                intro = arquivo.read()
        except FileNotFoundError:
            intro = "Erro: O arquivo 'herois.txt' não foi encontrado. Certifique-se de que os arquivos 'herois.txt' e 'chefe.txt' estão na mesma pasta do script."
        
        self.label_intro = Label(
            text=intro, 
            halign='left', 
            valign='top', 
            size_hint_y=None,
            color=[1, 1, 1, 1],
            font_size=dp(18),
            padding=(dp(10), dp(10))
        )
        self.label_intro.bind(texture_size=self.label_intro.setter('size'))
        
        self.scroll_view_intro = ScrollView(size_hint_y=0.7)
        self.scroll_view_intro.add_widget(self.label_intro)
        
        self.scroll_view_intro.bind(width=lambda instance, value: setattr(self.label_intro, 'text_size', (value, None)))
        
        self.buttons_layout = BoxLayout(orientation='vertical', size_hint_y=0.3, spacing=dp(5))

        self.button_guerreiro = Button(text='Guerreiro', size_hint_y=0.3)
        self.button_guerreiro.bind(on_press=lambda x: self.start_game('g'))

        self.button_mago = Button(text='Mago', size_hint_y=0.3)
        self.button_mago.bind(on_press=lambda x: self.start_game('m'))

        self.button_ladrao = Button(text='Ladrão', size_hint_y=0.3)
        self.button_ladrao.bind(on_press=lambda x: self.start_game('l'))
        
        self.buttons_layout.add_widget(self.button_guerreiro)
        self.buttons_layout.add_widget(self.button_mago)
        self.buttons_layout.add_widget(self.button_ladrao)

        self.layout.add_widget(self.scroll_view_intro)
        self.layout.add_widget(self.buttons_layout)
        
        self.add_widget(self.layout)

    def start_game(self, escolha):
        self.manager.get_screen('game').start_game_with_hero(escolha)
        self.manager.current = 'game'

class GameScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.hp_heroi = 200
        self.hp_chefe = 200
        self.dano_min_heroi = 20
        self.dano_max_heroi = 35
        self.dano_min_chefe = 20
        self.dano_max_chefe = 35
        self.play1 = None

        self.layout = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(10))
        
        self.label_status = Label(
            text="Seu HP: 200 | HP de Mor'Draal: 200", 
            size_hint_y=0.1,
            color=[1, 1, 1, 1],
            font_size=dp(20),
            bold=True
        )
        self.label_log = Label(
            text="A jornada começa!", 
            halign='left', 
            valign='top', 
            size_hint_y=None, 
            color=[1, 1, 1, 1],
            font_size=dp(16),
            padding=(dp(10), dp(10))
        )
        self.label_log.bind(texture_size=self.label_log.setter('size'))

        self.scroll_view_log = ScrollView(size_hint_y=0.7)
        self.scroll_view_log.add_widget(self.label_log)
        
        self.scroll_view_log.bind(width=lambda instance, value: setattr(self.label_log, 'text_size', (value, None)))
        
        self.button_ataque = Button(text="Atacar Mor'Draal!", size_hint_y=0.2)
        self.button_ataque.bind(on_press=self.batalha)
        
        self.exit_button = Button(text="Sair do Jogo", size_hint_y=0.2, disabled=True)
        self.exit_button.bind(on_press=lambda x: App.get_running_app().stop())

        self.layout.add_widget(self.label_status)
        self.layout.add_widget(self.scroll_view_log)
        self.layout.add_widget(self.button_ataque)
        self.layout.add_widget(self.exit_button)

        self.add_widget(self.layout)

    def start_game_with_hero(self, escolha):
        self.play1 = escolha
        self.hp_heroi = 200
        self.hp_chefe = 200
        self.label_status.text = f"Seu HP: {self.hp_heroi} | HP de Mor'Draal: {self.hp_chefe}"
        self.label_log.text = self.get_intro_text()
        self.button_ataque.disabled = False
        self.exit_button.disabled = True
    
    def get_intro_text(self):
        file_path = os.path.join(os.path.dirname(__file__), "chefe.txt")
        try:
            with open(file_path, 'r', encoding='utf-8') as arquivo:
                historia_chefe = arquivo.read()
        except FileNotFoundError:
            historia_chefe = "Erro: O arquivo 'chefe.txt' não foi encontrado. Certifique-se de que os arquivos 'herois.txt' e 'chefe.txt' estão na mesma pasta do script."
        
        if self.play1 == "g":
            return f"{historia_chefe}\n\nChegando ao campo de batalha, voce sente que e o unico guerreiro capaz de salvar Silverwood!!!"
        elif self.play1 == "m":
            return f"{historia_chefe}\n\nChegando ao campo de batalha, voce sente que e o unico mago capaz de salvar Silverwood!!!"
        elif self.play1 == "l":
            return f"{historia_chefe}\n\nChegando ao campo de batalha, voce sente que e o unico ladrao capaz de salvar Silverwood!!!"
        return "A jornada começa!"

    def batalha(self, instance):
        if self.hp_heroi <= 0 or self.hp_chefe <= 0:
            return

        dano_heroi = random.randint(self.dano_min_heroi, self.dano_max_heroi)
        self.hp_chefe -= dano_heroi
        self.hp_chefe = max(0, self.hp_chefe)
        log_ataque_heroi = f"Seu ataque causou {dano_heroi} de dano ao Necromante!\n"
        log_ataque_heroi += f"HP de Mor'Draal: {self.hp_chefe}\n\n"
        
        dano_chefe = random.randint(self.dano_min_chefe, self.dano_max_chefe)
        self.hp_heroi -= dano_chefe
        self.hp_heroi = max(0, self.hp_heroi)
        log_ataque_chefe = f"--- CONTRA-ATAQUE DE MOR'DRAAL! ---\nVocê sofreu {dano_chefe} de dano!\n"
        log_ataque_chefe += f"Seu HP atual: {self.hp_heroi}\n\n"
        
        self.label_log.text += log_ataque_heroi
        self.label_log.text += log_ataque_chefe

        self.label_status.text = f"Seu HP: {self.hp_heroi} | HP de Mor'Draal: {self.hp_chefe}"

        if self.hp_chefe <= 0:
            self.label_log.text += "PARABÉNS, HERÓI! VOCÊ SALVOU SILVERWOOD DA RUÍNA DE MOR'DRAAL!"
            self.button_ataque.disabled = True
            self.exit_button.disabled = False
        elif self.hp_heroi <= 0:
            self.label_log.text += "VOCÊ FOI DERROTADO! SILVERWOOD CAIU SOB O DOMÍNIO DE MOR'DRAAL."
            self.button_ataque.disabled = True
            self.exit_button.disabled = False

class RPGApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(StartScreen(name='start'))
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(GameScreen(name='game'))
        return sm

if __name__ == '__main__':
    RPGApp().run()

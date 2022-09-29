from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout

class Incrementar(BoxLayout):
    pass

class aula2_1(App):
    def build(self):
        return Incrementar()

if __name__ == "__main__":
    aula2_1().run()
from kivy.app import App 
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label


class Atividades(ScrollView):
    def __init__(self, atividades):
        super().__init__()
        for ativ in atividades:
            self.ids.box.add_widget(Label(text = ativ, font_size = 30, size_hint_y = None, height = 200))

class aula2_3(App):
    def build(self):
        return Atividades(['Andar', 'Correr', 'Caminhar', 'Pular'])

    
if __name__ == "__main__":
    aula2_3().run()
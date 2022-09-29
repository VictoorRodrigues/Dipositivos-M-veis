from kivy.app import App 
from kivy.uix.relativelayout import RelativeLayout

class AreadeDesenho(RelativeLayout):
    pass

class test2(App):
    def build(self):
        return AreadeDesenho()

if __name__ == "__main__":
    test2().run()
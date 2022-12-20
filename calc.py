from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window  # la taille

# Set la taille de l'image
Window.size = (500, 700)

# Choisis où l'on prend le kv
Builder.load_file('calc.kv')


class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = '0'

    def addition(self):
        self.ids.calc_input.text += '+'

    # Creation du on_press
    def button_press(self, button):
        # variable contenant ce qu'il y a dans le text_input
        prior = self.ids.calc_input.text

        #  Determiner si 0
        if prior == '0':
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{prior}{button}'
            # Prior va garder en mémoire ce qu'il y avait avant

    # Addition
    def add(self):
        # variable contenant ce qu'il y a dans le text_input
        prior = self.ids.calc_input.text
        # Ajouter le +
        self.ids.calc_input.text = f'{prior}+'

    # Soustraction
    def subtract(self):
        # variable contenant ce qu'il y a dans le text_input
        prior = self.ids.calc_input.text
        # Ajouter le -
        self.ids.calc_input.text = f'{prior}-'

    # Multiplication
    def multiply(self):
        # variable contenant ce qu'il y a dans le text_input
        prior = self.ids.calc_input.text
        # Ajouter le *
        self.ids.calc_input.text = f'{prior}*'

    # Division
    def divide(self):
        # variable contenant ce qu'il y a dans le text_input
        prior = self.ids.calc_input.text
        # Ajouter le /
        self.ids.calc_input.text = f'{prior}/'

    # Égalisation
    def equals(self):
        # variable contenant ce qu'il y a dans le text_input
        prior = self.ids.calc_input.text
        # Ajouter le =
        # Enlever le signe du string

        # Addition
        if "+" in prior:
            num_list = prior.split("+")
            res = 0
            for num in num_list:
                res += int(num)

            self.ids.calc_input.text = str(res)


class CalculatorApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    CalculatorApp().run()
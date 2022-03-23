from posixpath import split
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang import Builder


Builder.load_file('calc.kv')

Window.size = (400, 500)
Window.clearcolor  = (1,1,1,1)
class Calculadora(Widget):
    counter = 0
    ponto = 0
    def insert(self, valor):
        
        texto = self.ids.conteudo.text
        if texto == 'Erro indefinido' or texto == 'Erro semântico':
            self.ids.conteudo.text = ''
            self.ids.conteudo.foreground_color = (0,0,0)
        if self.counter == 0:
            self.ids.conteudo.insert_text(valor)
            self.counter = 1
        else:
            if self.avaliacao(texto, valor):                
                self.ids.conteudo.insert_text(valor)
            else:
                return

        print('Bumbou, ', self.counter )

    def clear(self):
        self.ids.conteudo.foreground_color = (0,0,0)
        self.ids.conteudo.font_size = 32
        self.ids.conteudo.text = ''
        self.counter = 0
    def delete(self):
        valor = self.ids.conteudo.text
        self.ids.conteudo.text = valor[0:-1]
        if self.ids.conteudo.text == '':
            self.counter = 0
    def equal(self):
        
        texto = self.ids.conteudo.text
        lista = [[],[],[],[]]
        for i,smb in enumerate('+-/*'):
            if smb in texto:
                lista[i] = (texto.split(smb))
        for lst in lista:
            for coisas in lst:
                if coisas.count('.') > 1:
                    self.ids.conteudo.text = 'Erro semântico'
                    self.ids.conteudo.foreground_color = (1,0,0)
                    return
        try:
            self.ids.conteudo.text = str(eval(texto))
        except:
            self.ids.conteudo.text  = 'Erro indefinido'
            self.ids.conteudo.foreground_color = (1,0,0)
          
        
    def avaliacao(self, texto, avaliado):
        simbolos = '+-/*.'
        if avaliado in simbolos and texto[-1] in simbolos:
            return False
        elif avaliado == '.' and texto[-1] not in simbolos and self.ponto == 1:
            False
        elif avaliado not in simbolos:
            self.ponto = 0
            return True
        else:
            self.ponto = 0
            return True

class CalculadoraApp(App):
    def build(self):
        return Calculadora()

if __name__ == '__main__':
    CalculadoraApp().run()
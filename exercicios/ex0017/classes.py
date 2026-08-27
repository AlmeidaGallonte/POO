class Numero:
    def __init__(self, valor: int|float = 0):
        self.valor = valor

    def dobrar(self):
        self.valor = self.valor * 2

    def __str__(self):
        return f'Tenho o número {self.valor} dentro so número'

class Texto:
    def __init__(self, txt: str = ''):
        self.texto = txt

    def dobrar(self):
        self.texto = self.texto + ' ' + self.texto

    def __str__(self):
            return f'Tenho o texto "{self.texto}" dentro do texto'

class Lista:
    def __init__(self, lst: list = []):
        self.valores = lst

    def dobrar(self):
        self.valores = self.valores + self.valores

    def __str__(self):
            return f'Tenho os itens {self.valores} dentro da lista'

class Papel:
    def __init__(self):
        self.dobrado = False

    def dobrar(self):
        self.dobrado = True

    def __str__(self):
            return f'O papel esta {'novo' if not self.dobrado else 'dobrado'}'

class Casa:
    def __init__(self):
        pass

    def __str__(self):
            return f'...'

#duck typing

def tente_dobrar(obj):
    try:
          obj.dobrar()
    except:
         print(f'Tive um erro ao tentar dobrar {obj.__class__.__name__}')
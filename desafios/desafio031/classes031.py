class Retangulo:
    def __init__(self, base = 1, altura = 1):
        self._base = base
        self._altura = altura
        self._area = None

    @property
    def base(self):
        return self._base
    
    @base.setter
    def base(self, valor):
        if valor > 0:
            self._base = valor


    @property
    def area(self):
        return self.base * self.altura
    

    @property
    def altura(self):
        return self._altura
    @altura.setter
    def altura(self, valor):
        if valor > 0:
            self._altura = valor


    @property
    def medidas(self):
        return f'Base = {self._base} \nAltura = {self._altura}\nArea = {self.area}'


        
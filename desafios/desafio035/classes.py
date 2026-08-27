from abc import ABC

class Arquivo(ABC):
    def __init__(self,nome:str='',tam:int|float=0):
        self.nome = nome
        self.nome_completo = None
        self.tamanho = tam
        self._extensao = None

class PDF(Arquivo):
    def __init__(self,nome:str='',tam:int|float=0):
        super().__init__(nome,tam) 
        self.tamanho = self.tamanho / 1_000_000
        self.nome_completo = f"'{self.nome}.pdf'({self.tamanho}MB)"
        self._extensao = 'Adobe Reader'
        

class DOC(Arquivo):
    def __init__(self,nome:str='',tam:int|float=0):
        super().__init__(nome,tam) 
        self.tamanho = self.tamanho / 1_000_000
        self.nome_completo = f"'{self.nome}.docx'({self.tamanho}MB)"
        self._extensao = 'Microsoft World'

def abrir_aquivo(obj):
    try:
        print(f"Abrindo o arquivo {obj.nome_completo} no {obj._extensao}")
    except:
        print('ERRO:não foi possivel abrir esse arquivo!')

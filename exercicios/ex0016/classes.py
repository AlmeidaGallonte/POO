class Porta:
    def abrir(self):
        print(f'Girar a maçaneta e empurre/puxar a pota')

class Empresa:
    def abrir(self):
        print(f'vá ao portal do empreendedor com toda a documentação para abrir um CNPJ')

class Ovo:
    def abrir(self):
        print(f'Quebre a casca com um garfo e separe as partes sobre a frigideira')

class Pedra:
    pass

# METODO PYTHONICO POLIMORFICO DUCK TYPINGO

def tentar_abrir(obj):
    try:
        obj.abrir()
    except:
        print(f'Encontrei problemas ao tentar abrir um objeto tipo  {obj.__class__.__name__}')
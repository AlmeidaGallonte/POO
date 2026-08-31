from abc import ABC, abstractmethod

class Arquivo(ABC):
    def __init__(self,nome:str, ext:str ,tam:int):
        self.nome = nome
        self.tamanho = tam
        self._extensao = None
        self.extensao = ext

    @abstractmethod
    def abrir():
            pass

    @property
    def extensao(self):
            return self._extensao

    @extensao.setter
    def extensao(self, ext):
        formatos = ['pdf','doc', 'docx']
        ext = ext.lower().strip()
        if ext in formatos:
            self._extensao = ext
        else:
            print('Erro: Attributoerror')

    @property
    def nome_completo(self):
         return f"'{self.nome}.{self.extensao}'({self.tamanho/ 1_048_576:.2f}MB)"


class PDF(Arquivo):

    def __init__(self,nome:str,tam:int):
        super().__init__(nome, 'pdf',tam) 
        

    def abrir(self):
        print(f"Abrindo o arquivo {self.nome_completo} no Adobe Reader")
    
    
        

class DOC(Arquivo):

    def __init__(self,nome:str,tam:int):
        super().__init__(nome, 'docx',tam) 
        

    def abrir(self):
        print(f"Abrindo o arquivo {self.nome_completo} no Microsoft Word")
    
def abrir_arquivo(arq):
     arq.abrir()


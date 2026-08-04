from POO.exercicios.ex009.classe09 import *
from rich import print, inspect
def main():

    av1 = Avaliacao('Jamerson', 'Analise e Desenvolvimento de Sistemas(ADS)')
    av1.set_nota(9.5)
    print(f'{av1.nome} tirou {av1.get_nota()} em {av1.disciplina}')
    #inspect(av1, private=True)
    
if __name__ == "__main__":
    main()
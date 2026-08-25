from POO.exercicios.ex011.classe10 import *
from rich import print, inspect
def main():

    av1 = Avaliacao('Jamerson', 'Analise e Desenvolvimento de Sistemas(ADS)')
    av1.nota = 100
    print(f'{av1.nome} tirou {av1.nota} em {av1.disciplina}')
    #inspect(av1, private=True)
    
if __name__ == "__main__":
    main()
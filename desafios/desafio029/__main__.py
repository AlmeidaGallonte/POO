from rich import print, inspect
from POO.desafios.desafio029.classes import *
def main():
    meudiario = Diario()
    meudiario.escrever('neymar acabou')
    meudiario.escrever('Estou aprendendo a amar e ser amado!')
    try:
        meudiario.ler('Cev!@')
    except Exception as e:
        print(f'[red]ERRO: {e}[/]')

if __name__ == '__main__':
    main()
from classes import *
from rich import print

def main():

    funcionarios = [

        Desenvolvedor('Pedro', 18_000),
        Desingner('José', 25_000),
        Gerente('Mariana', 45_000)
    ]

    for f in funcionarios:
        print(f)

if __name__ == '__main__':
    main()
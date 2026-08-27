from classes import *
from rich import print

def main():

    a = Gerente('Marcio', 1000)
    b = Desenvolvedor('Jamerson', 1000)
    c = Desingner('Luna', 1000)

    b.salario = 1500
    a.salario = 900
    
    print(a)
    print(b)
    print(c)

if __name__ == '__main__':
    main()
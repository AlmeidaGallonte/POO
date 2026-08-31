from classes import *
from rich import inspect
def main():

    validar_dado(Usuário(), 'gus1234')
    validar_dado(Email(), 'xpto@gmail.com')
    validar_dado(Senha(), 'Te#stando7')
  

if __name__ == '__main__':
    main()
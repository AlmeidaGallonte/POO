from classes import *
from rich import print, inspect

def main():
    a2 = PDF('conta', 1_550_000)
    a1 = DOC('prova', 550_000)
    abrir_arquivo(a1)
    abrir_arquivo(a2)
    
if __name__ == '__main__':
    main()
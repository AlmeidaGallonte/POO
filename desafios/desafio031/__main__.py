from POO.desafios.desafio031.classes031 import Retangulo
from rich import print, inspect

def main():
    r = Retangulo()
    r.base = 12
    r.altura = 33
    inspect(r, private=True, methods=True)

if __name__ == "__main__":
    main()

from POO.desafios.desafio028.classes import Termostato
from rich import print, inspect

def main():
    t = Termostato()
    try:
        t.temperatura = 25.5
    except Exception as e:
        print(f'teve um prblema burro: {e}')
    
    print(f'a temperatura atual é {t.ftemperatura}')


if __name__ == '__main__':
    main()
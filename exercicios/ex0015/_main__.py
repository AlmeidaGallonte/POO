from classes import *

def main():
    c1 = Carteira(100)
    c2 = Carteira(100)

    c1 += 90
    c2 += 30
    c1 -= 60

    print(c1 == c2)
    print(c1<c2)

    if (c1 == c2):
        print('Carteira com o mesmo valor')
    else:
        print('Carteira com valores diferentes')

    if (c1 < c2):
        print('Cateira 1 tem menos dinheiro q a Carteira 2')
    elif (c2 < c1):
        print('Cateira 2 tem menos dinheiro q a Carteira 1')
    else:
        print('Cateiras com o mesmo valor')

    print(c1)
    print(c2)

if __name__ == '__main__':
    main()
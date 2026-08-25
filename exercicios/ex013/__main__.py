from POO.exercicios.ex014.classes import *

def main():
    
    p1 = Mãe('Claudineide')
    p2 = Filho('Jamerson')
    p3 = Filha('Carla')

    p1.fazer_pudim()
    p1.fritar_coxinha()

    p2.fazer_pudim()
    p2.fritar_coxinha()

    p3.fazer_pudim()
    p3.fritar_coxinha()

if __name__ == '__main__':
    main()
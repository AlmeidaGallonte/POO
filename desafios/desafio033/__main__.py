from rich import inspect
from POO.desafios.desafio033.classe33 import *

def main():
    j = Aluno('ADS', 'Jamerson', 2006)
    j.nascimento = 2006
    j.add_curso('MODA')
    j.curso = 'MODA'
    print(j.idade)
    inspect(j, private=True, methods=True)
if __name__ == "__main__":
    main()

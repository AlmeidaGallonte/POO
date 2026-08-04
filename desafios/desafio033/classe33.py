from abc import ABC
from datetime import date

class Pessoa(ABC):
    def __init__(self, nome = None, nascimento = None):
        self._nome = nome
        self._nascimento = nascimento

    @property
    def nome(self):
        return self._nome

    @property
    def nascimento(self):
        return self._nascimento
    @nascimento.setter
    def nascimento(self, novonascimento):
        if novonascimento < 2026:
            self._nascimento = novonascimento
        else:
            print(f'A ano {novonascimento} é inváido')

    @property
    def idade(self):
        return 2026 - self._nascimento
        
class Aluno(Pessoa):
    def __init__(self, curso,  nome = None, nascimento = None):
        super().__init__(nome, nascimento)
        self.cursos_oficiais = ['ADM','ADS','ENG','CONT']
        self._curso = curso

    @property
    def curso(self):
            return self._curso
    
    @curso.setter
    def curso(self, novo_curso:str):
        if novo_curso in self.cursos_oficiais:
            self._curso = novo_curso
        else:
            print(f'O curso {novo_curso} não é oficial')

    def add_curso(self, novo_curso):
        self.cursos_oficiais.append(novo_curso)

import os

class LivrosLidos2k25:

    livros = []

    def __init__(self, autor: str, titulo: str, tempo_de_leitura_em_minutos: int):
        self.autor = autor.title()
        self.titulo = titulo.title()
        self.tempo_de_leitura_em_minutos = tempo_de_leitura_em_minutos
        self.status = False
        LivrosLidos2k25.livros.append(self)

    def __str__(self):
        return f"{self.titulo} - {self.autor}"
    
    @classmethod
    def lista_livros(cls):
        os.system('cls')
        print('\n-----------------------------------| Lista de Livros Lidos em 2025 |----------------------------------')
        print(f'\n| {'Autor:':<30} | {'Título:':<30} | {'Status:':<30} | {'Tempo de Leitura:':<30} |')
        for livro in cls.livros:
            print(f'| {livro.autor:<30} | {livro.titulo:<30} | {livro.definir_status():<30} | {livro.minutos_para_horas():<30} |')
    

    def alternar_status(self):
        self.status = not self.status

    def definir_status(self):
        return 'Leitura Finalizada' if self.status else 'Leitura em Andamento'

    def minutos_para_horas(self):
        horas = self.tempo_de_leitura_em_minutos // 60
        minutos = self.tempo_de_leitura_em_minutos % 60
        return f'{horas} horas e {minutos} minutos'


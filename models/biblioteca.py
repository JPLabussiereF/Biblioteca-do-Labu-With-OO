import os
class Livros:

    livros = []

    def __init__(self, autor: str, titulo: str, ano_da_leitura: int):
        if len(str(ano_da_leitura)) != 4:
            raise ValueError("O ano da leitura deve conter 4 dígitos!")
        
        if ano_da_leitura > 2025:
            raise ValueError("O ano da leitura deve ser menor ou igual a 2025!")

        self.autor = autor.title()
        self.titulo = titulo.title()
        self.ano_da_leitura = ano_da_leitura
        self.tempo_de_leitura_em_minutos = 0
        self.status = False
        Livros.livros.append(self)

    def __str__(self):
        return f"{self.titulo} - {self.autor}"
    
    @classmethod
    def lista_livros(cls):
        os.system('cls')
        if not Livros.livros:
            print('Nenhum livro foi adicionado à lista. Adicione um livro para visualizar a lista!')
            return
        
        print('\n-----------------------------------| Lista de Livros Lidos em 2025 |----------------------------------')
        print(f'\n| {'Autor:':<20} | {'Título:':<25} | {'Status:':<22} | {'Tempo de Leitura:':<22} |')
        for livro in cls.livros:
            print(f'| {livro.autor:<20} | {livro.titulo:<25} | {livro.definir_status():<22} | {livro.minutos_para_horas():<22} |')
    
    def alternar_status(self):
        self.status = not self.status

    def definir_status(self):
        return 'Leitura Finalizada' if self.status else 'Leitura em Andamento'

    def minutos_para_horas(self):
        horas, minutos = divmod(self.tempo_de_leitura_em_minutos, 60)
        hora_str = "hora" if horas == 1 else "horas"
        minuto_str = "minuto" if minutos == 1 else "minutos"
        return f'{horas} {hora_str} e {minutos} {minuto_str}' if horas or minutos else '0 hora e 0 minuto'
    
    def adicionar_tempo_de_leitura(self, minutos: int):
        self.tempo_de_leitura_em_minutos += minutos

    


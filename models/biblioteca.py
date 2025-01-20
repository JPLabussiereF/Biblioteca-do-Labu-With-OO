import os
class Livros:
    """
    Classe para representar livros lidos em 2025.

    Atributos:
    ----------
    autor : str
        O autor do livro.
    titulo : str
        O título do livro.
    ano_da_leitura : int
        O ano em que o livro foi lido.
    tempo_de_leitura_em_minutos : int
        O tempo total de leitura do livro em minutos.
    status : bool
        Indica se a leitura do livro está finalizada (True) ou em andamento (False).

    Métodos:
    --------
    __init__(self, autor: str, titulo: str, ano_da_leitura: int):
        Inicializa um objeto Livros com autor, título, ano de leitura e adiciona à lista de livros lidos.
        Lança ValueError se o ano_da_leitura não tiver 4 dígitos ou for maior que 2025.

    __str__(self):
        Retorna uma representação em string do objeto no formato "Título - Autor".

    lista_livros(cls):
        Método de classe que lista todos os livros lidos em 2025, mostrando autor, título, status e tempo de leitura.

    alternar_status(self):
        Alterna o status da leitura entre finalizada e em andamento.

    definir_status(self):
        Retorna uma string indicando se a leitura está "Leitura Finalizada" ou "Leitura em Andamento".

    minutos_para_horas(self):
        Converte o tempo de leitura em minutos para horas e minutos formatados.

    adicionar_tempo_de_leitura(self, minutos: int):
        Adiciona tempo de leitura em minutos ao livro.
    """

    livros = []

    def __init__(self, autor: str, titulo: str, ano_da_leitura: int):
        """
        Inicializa um objeto Livros com autor, título, ano de leitura e adiciona à lista de livros lidos.

        Parâmetros:
        -----------
        autor : str
            O autor do livro.
        titulo : str
            O título do livro.
        ano_da_leitura : int
            O ano em que o livro foi lido.

        Lança ValueError se o ano_da_leitura não tiver 4 dígitos ou for maior que 2025.
        """
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
        """
        Retorna uma representação em string do objeto no formato "Título - Autor".
        """
        return f"{self.titulo} - {self.autor}"
    
    @classmethod
    def lista_livros(cls):
        """
        Método de classe que lista todos os livros lidos em 2025, mostrando autor, título, status e tempo de leitura.
        """
        os.system('cls')
        if not Livros.livros:
            print('Nenhum livro foi adicionado à lista. Adicione um livro para visualizar a lista!')
            return
        
        print('\n-----------------------------------| Lista de Livros Lidos em 2025 |----------------------------------')
        print(f'\n| {'Autor:':<20} | {'Título:':<25} | {'Status:':<22} | {'Tempo de Leitura:':<22} |')
        for livro in cls.livros:
            print(f'| {livro.autor:<20} | {livro.titulo:<25} | {livro.definir_status():<22} | {livro.minutos_para_horas():<22} |')
    
    def alternar_status(self):
        """
        Alterna o status da leitura entre finalizada e em andamento.
        """
        self.status = not self.status

    def definir_status(self):
        """
        Retorna uma string indicando se a leitura está "Leitura Finalizada" ou "Leitura em Andamento".
        """
        return 'Leitura Finalizada' if self.status else 'Leitura em Andamento'

    def minutos_para_horas(self):
        """
        Converte o tempo de leitura em minutos para horas e minutos formatados.

        Retorna:
        --------
        str
            Uma string formatada representando o tempo de leitura em horas e minutos.
        """
        horas, minutos = divmod(self.tempo_de_leitura_em_minutos, 60)
        hora_str = "hora" if horas == 1 else "horas"
        minuto_str = "minuto" if minutos == 1 else "minutos"
        return f'{horas} {hora_str} e {minutos} {minuto_str}' if horas or minutos else '0 hora e 0 minuto'
    
    def adicionar_tempo_de_leitura(self, minutos: int):
        """
        Adiciona tempo de leitura em minutos ao livro.

        Parâmetros:
        -----------
        minutos : int
            O tempo de leitura a ser adicionado em minutos.
        """
        self.tempo_de_leitura_em_minutos += minutos

    


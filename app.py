from models.biblioteca import Livros

# Criação de instâncias da classe Livros
livro1 = Livros('George Orwell', 'A Revolução dos Bichos', 2025)
livro1.adicionar_tempo_de_leitura(224)
livro1.alternar_status()

livro2 = Livros('George Orwell', '1984', 2025)

def __main__():
    """
    Função principal que exibe a lista de livros cadastrados.

    Chama o método de classe `lista_livros()` da classe `Livros` para exibir os livros adicionados.
    """
    Livros.lista_livros()

if __name__ == '__main__':
    """
    Ponto de entrada do script.

    Executa a função `__main__` se o script for executado diretamente.
    """
    __main__()
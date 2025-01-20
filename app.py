from models.biblioteca import Livros

livro1 = Livros('George Orwell', 'A Revolução dos Bichos', 2025, 224)

livro1.alternar_status()
livro2 = Livros('George Orwell', '1984', 2025, 0)

def __main__():
    Livros.lista_livros()

if __name__ == '__main__':
    __main__()
from models.biblioteca import LivrosLidos2k25

a_revolucao_dos_bichos = LivrosLidos2k25('George Orwell', 'A Revolução dos Bichos', 224)
a_revolucao_dos_bichos.alternar_status()


def __main__():

    print(a_revolucao_dos_bichos)
    LivrosLidos2k25.lista_livros()

if __name__ == '__main__':
    __main__()
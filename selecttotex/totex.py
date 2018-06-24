import pandas as pd
from selecttotex.database import Database


class Totex:
    """Classe para transformar resultados de selects em Latex
    """

    def __init__(self):
        self.db = Database().get_connection()

    def to_tex(self, command_list: list, output_file: str) -> None:
        """Função para transformar select em tabela latex
        :param: command_list: Lista com os selects que deverão ser utilizados
        :param: output_file: Caminho/Nome do arquivo a ser salvo com as tabelas
        """

        # Criando arquivo para armazenar resultados
        file = open(output_file, 'w')
        file.write('Tabelas geradas pelo SelectToTex\n\n\n')

        # Criando o loop para percorrer os comandos da lista
        for command in command_list:

            self.db.execute(command)
            # Recupera o resultado e já transforma ele em String
            r = str(pd.DataFrame(self.db.fetchall()).to_latex())

            file.write(r)
            file.write('\n\n')

        file.close()

import json
import psycopg2


def get_config() -> str:
    """Recupera as informações de configuração do banco de dados
    """

    j = None
    with open('config.json', 'r') as config:
        j = json.load(config)

    return "host={} port={} dbname={} user={} password={}".format(
                                                                    j['host'], 
                                                                    j['port'], 
                                                                    j['dbname'], 
                                                                    j['user'], 
                                                                    j['password']
                                                        )


class Database:
    """Classe para conexão com banco de dados
    """

    @classmethod
    def get_connection(self): 
        """Método para criar conexão com o banco de dados
        """

        conn_string = get_config()
        conn = psycopg2.connect(conn_string)
        
        return conn.cursor()

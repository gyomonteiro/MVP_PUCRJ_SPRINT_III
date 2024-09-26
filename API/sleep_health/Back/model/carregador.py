import pandas as pd

class Carregador:

    def carregar_dados(self, url: str, atributos: list):
        """ 
        Carrega e retorna um DataFrame a partir de um arquivo CSV.
        Diversos parâmetros do read_csv podem ser configurados para oferecer mais opções,
        como por exemplo tipos de dados, tratamento de valores ausentes, entre outros.
        """
        
        return pd.read_csv(url, names=atributos,
                           skiprows=1, delimiter=',') # Esses parâmetros são específicos para este dataset. Ajustes podem ser necessários para outros casos.

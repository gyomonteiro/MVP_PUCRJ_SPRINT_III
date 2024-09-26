from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

class PreProcessador:

    def pre_processar(self, dataset, percentual_teste, seed=7):
        """ 
        Executa todas as etapas do pré-processamento.
        Inclui limpeza de dados, eliminação de outliers, seleção de features,
        e normalização/padronização dos dados.
        """
        # Divisão dos dados em treino e teste
        X_train, X_test, Y_train, Y_test = self.__preparar_holdout(dataset,
                                                                   percentual_teste,
                                                                   seed)
        # Padronização dos dados
        scaler = StandardScaler().fit(X_train)
        X_train_scaled = scaler.transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        
        # Retorna os dados padronizados e o scaler para uso futuro
        return (X_train_scaled, X_test_scaled, Y_train, Y_test, scaler)
    
    def __preparar_holdout(self, dataset, percentual_teste, seed):
        """ 
        Divide os dados em treino e teste usando o método holdout.
        Assume que a variável alvo (target) está na última coluna do dataset.
        O parâmetro test_size define o percentual de dados destinados ao conjunto de teste.
        """
        dados = dataset.values
        X = dados[:, 1:-1]  # Excluindo 'person_ID' se não for relevante
        Y = dados[:, -1]    # Seleção da variável target (última coluna)
        return train_test_split(X, Y, test_size=percentual_teste, random_state=seed)

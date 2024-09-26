from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score

class Avaliador:

    def avaliar(self, modelo, X_test, Y_test):
        """ 
        Realiza a predição e avalia o modelo em termos de diversas métricas. 
        Futuramente, pode-se parametrizar o tipo de avaliação ou outros aspectos.
        """
        predicoes = modelo.predict(X_test)
        
        # Para problemas multiclasses, altere o parâmetro 'average' conforme necessário
        return (accuracy_score(Y_test, predicoes),
                recall_score(Y_test, predicoes, average='binary'),
                precision_score(Y_test, predicoes, average='binary'),
                f1_score(Y_test, predicoes, average='binary'))

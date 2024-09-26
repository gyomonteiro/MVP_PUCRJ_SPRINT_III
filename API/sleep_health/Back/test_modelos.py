from model.avaliador import Avaliador
from model.carregador import Carregador
from model.modelo import Model
import os

# Instanciação das Classes
carregador = Carregador()
modelo = Model()
avaliador = Avaliador()

# Parâmetros
# Caminho base para garantir a localização correta dos arquivos
base_dir = r'C:\Users\Giovanny\Desktop\PUCRJ MVP Sprint 3 - Qualidade de Software, Segurança e Sistemas Inteligentes\API\sleep_health\Back'

# Caminho completo para o arquivo CSV
url_dados = os.path.join(base_dir, "database", "sleep_health_golden.csv")
colunas = [
    "person_ID",
    "gender",
    "age",
    "sleep_duration",
    "quality_sleep",
    "activity_level",
    "stress_level",
    "bmi_category",
    "blood_pressure",
    "heart_rate",
    "daily_steps",
    "disorder",
]

# Carga dos dados
dataset = carregador.carregar_dados(url_dados, colunas)

# Separando em dados de entrada e saída
X = dataset.iloc[:, 1:-1]  # Excluindo 'person_ID' se não for relevante
Y = dataset.iloc[:, -1]

# Método para testar o modelo do KNN a partir do arquivo correspondente
# O nome do método a ser testado necessita começar com "test_"
def test_modelo_knn():
    # Importando o modelo do KNN
    knn_path = os.path.join(base_dir, "ml_model", "sleep_health_knn.joblib")
    scaler_path = os.path.join(base_dir, "ml_model", "scaler_knn.joblib")
    
    modelo_knn = modelo.carrega_modelo(knn_path)
    scaler = modelo.carrega_modelo(scaler_path)

    # Padronizando os dados de entrada usando o scaler treinado
    X_rescaled = scaler.transform(X)

    # Obtendo as métricas do KNN
    acuracia_knn, recall_knn, precisao_knn, f1_knn = avaliador.avaliar(modelo_knn, X_rescaled, Y)

    # Testando as métricas do KNN
    # Modifique os valores de acordo com seus requisitos
    assert acuracia_knn >= 0.75
    assert recall_knn >= 0.5
    assert precisao_knn >= 0.5
    assert f1_knn >= 0.5

if __name__ == '__main__':
    import unittest

    class TestSeuScript(unittest.TestCase):
        def test_modelo_knn(self):
            test_modelo_knn()

    unittest.main()

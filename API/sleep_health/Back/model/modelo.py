import numpy as np
import pickle
import joblib
from logger import logger

class Model:
    def __init__(self):
        self.model = None
        self.scaler = None

    def carrega_modelo(self, model_path, scaler_path):
        """ 
        Carrega o modelo e o scaler a partir dos caminhos fornecidos.
        Suporta arquivos com as extensões .pkl (pickle) e .joblib (Joblib).
        """
        # Carregamento do modelo
        if model_path.endswith(".pkl"):
            self.model = pickle.load(open(model_path, "rb"))
        elif model_path.endswith(".joblib"):
            self.model = joblib.load(model_path)
        else:
            raise Exception("Formato de arquivo de modelo não suportado")

        # Carregamento do scaler
        if scaler_path.endswith(".pkl"):
            self.scaler = pickle.load(open(scaler_path, "rb"))
        elif scaler_path.endswith(".joblib"):
            self.scaler = joblib.load(scaler_path)
        else:
            raise Exception("Formato de arquivo do scaler não suportado")

    def preditor(self, form):
        """ 
        Realiza a predição para uma pessoa com base no modelo treinado.
        Recebe um formulário com os dados da pessoa e retorna o diagnóstico previsto.
        """
        # Converte os dados do formulário para um array NumPy
        X_input = np.array(
            [
                form.gender,
                form.age,
                form.sleep_duration,
                form.quality_sleep,
                form.activity_level,
                form.stress_level,
                form.bmi_category,
                form.blood_pressure,
                form.heart_rate,
                form.daily_steps,
            ]
        )

        # Reshape dos dados para que o modelo receba a entrada no formato correto
        X_input = X_input.reshape(1, -1)

        # Verifica se o scaler foi carregado
        if self.scaler is None:
            raise Exception("Scaler não carregado. Por favor, carregue o scaler antes de fazer predições.")

        # Aplica o scaler aos dados de entrada para padronizá-los de acordo com o treino
        X_input_scaled = self.scaler.transform(X_input)

        # Predição com base nos dados de entrada padronizados
        diagnosis = self.model.predict(X_input_scaled)

        # Log da predição realizada
        logger.info(f"================ diagnosis[0] ============ : '{diagnosis[0]}'")
        
        return int(diagnosis[0])

from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from model import Base

# Definição do modelo da tabela 'pessoas'

class Pessoa(Base):
    __tablename__ = "pessoas"

    # Definição das colunas da tabela
    id = Column(Integer, primary_key=True)
    person_id = Column("ID Pessoa", Integer)
    gender = Column("Genero", Integer)
    age = Column("Idade", Integer)
    sleep_duration = Column("Duracao", Float)
    quality_sleep = Column("Qualidade", Integer)
    activity_level = Column("Atividade", Integer)
    stress_level = Column("Estresse", Integer)
    bmi_category = Column("IMC", Integer)
    blood_pressure = Column("Pressao", Float)
    heart_rate = Column("FrequenciaCardiaca", Integer)
    daily_steps = Column("Passos", Integer)
    outcome = Column("Disturbio", Integer, nullable=True)
    data_insercao = Column(DateTime, default=datetime.now)

    def __init__(
        self,
        person_id: int,
        gender: int,
        age: int,
        sleep_duration: float,
        quality_sleep: int,
        activity_level: int,
        stress_level: int,
        bmi_category: int,
        blood_pressure: float,
        heart_rate: int,
        daily_steps: int,
        outcome: int,
        data_insercao: Union[DateTime, None] = None,
    ):
        """
        Inicializa uma instância de 'Pessoa' com os atributos fornecidos.

        Arguments:
            person_id: identificador para cada indivíduo.
            gender: Gênero da pessoa (Masculino/Feminino).
            age: Idade da pessoa.
            sleep_duration: Duração do sono em horas.
            quality_sleep: Qualidade do sono em uma escala de 1 a 10.
            activity_level: Nível de atividade física em uma escala de 1 a 10.
            stress_level: Nível de estresse em uma escala de 1 a 10.
            bmi_category: Categoria de IMC (1: Normal, 2: Sobrepeso, 3: Obeso).
            blood_pressure: Pressão arterial (sistólica/diastólica).
            heart_rate: Frequência cardíaca em batimentos por minuto (bpm).
            daily_steps: Número de passos diários.
            outcome: Diagnóstico de distúrbio do sono.
            data_insercao: Data de inserção no banco de dados (padrão: data atual).
        """
        self.person_id = person_id
        self.gender = gender
        self.age = age
        self.sleep_duration = sleep_duration
        self.quality_sleep = quality_sleep
        self.activity_level = activity_level
        self.stress_level = stress_level
        self.bmi_category = bmi_category
        self.blood_pressure = blood_pressure
        self.heart_rate = heart_rate
        self.daily_steps = daily_steps
        self.outcome = outcome

        # Se a data de inserção não for fornecida, define como a data atual
        if data_insercao:
            self.data_insercao = data_insercao

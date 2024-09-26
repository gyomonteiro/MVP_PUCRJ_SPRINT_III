from pydantic import BaseModel
from typing import Optional, List
from model.pessoa import Pessoa
import json
import numpy as np


class PessoaSchema(BaseModel):
    """Define o esquema para representar uma nova pessoa a ser inserida no sistema."""

    person_id: int = 1
    gender: int = 1
    age: int = 50
    sleep_duration: float = 6.1
    quality_sleep: int = 6
    activity_level: int = 42
    stress_level: int = 8
    bmi_category: int = 2
    blood_pressure: float = 126.83
    heart_rate: int = 77
    daily_steps: int = 4200


class PessoaViewSchema(BaseModel):
    """Define o esquema para representar uma pessoa ao ser retornada."""

    id: int = 1
    person_id: int = 1
    gender: int = 1
    age: int = 50
    sleep_duration: float = 6.1
    quality_sleep: int = 6
    activity_level: int = 42
    stress_level: int = 8
    bmi_category: int = 2
    blood_pressure: float = 126.83
    heart_rate: int = 77
    daily_steps: int = 4200
    outcome: int = None


class PessoaBuscaSchema(BaseModel):
    """Define o esquema da estrutura utilizada para buscar uma pessoa pelo seu ID."""

    person_id: int = "1"


class ListaPessoasSchema(BaseModel):
    """Define o esquema para representar uma lista de pessoas."""

    pessoas: List[PessoaSchema]


class PessoaDelSchema(BaseModel):
    """Define o esquema para representar a deleção de uma pessoa."""

    person_id: int = "1"


# Apresenta os dados de uma única pessoa
def apresenta_pessoa(pessoa: Pessoa):
    """Retorna a representação de uma pessoa de acordo com o esquema
    definido em PessoaViewSchema.
    """
    return {
        "id": pessoa.id,
        "person_id": pessoa.person_id,
        "gender": pessoa.gender,
        "age": pessoa.age,
        "sleep_duration": pessoa.sleep_duration,
        "quality_sleep": pessoa.quality_sleep,
        "activity_level": pessoa.activity_level,
        "stress_level": pessoa.stress_level,
        "bmi_category": pessoa.bmi_category,
        "blood_pressure": pessoa.blood_pressure,
        "heart_rate": pessoa.heart_rate,
        "daily_steps": pessoa.daily_steps,
        "outcome": pessoa.outcome,
    }


# Apresenta os dados de uma lista de pessoas
def apresenta_pessoas(pessoas: List[Pessoa]):
    """Retorna a representação de uma lista de pessoas de acordo com o esquema
    definido em PessoaViewSchema.
    """
    result = []
    for pessoa in pessoas:
        result.append(
            {
                "id": pessoa.id,
                "person_id": pessoa.person_id,
                "gender": pessoa.gender,
                "age": pessoa.age,
                "sleep_duration": pessoa.sleep_duration,
                "quality_sleep": pessoa.quality_sleep,
                "activity_level": pessoa.activity_level,
                "stress_level": pessoa.stress_level,
                "bmi_category": pessoa.bmi_category,
                "blood_pressure": pessoa.blood_pressure,
                "heart_rate": pessoa.heart_rate,
                "daily_steps": pessoa.daily_steps,
                "outcome": pessoa.outcome,
            }
        )

    return {"pessoas": result}

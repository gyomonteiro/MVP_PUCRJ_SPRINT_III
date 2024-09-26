from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote
import joblib
from sqlalchemy.exc import IntegrityError
from model import Session, Pessoa, Model
from logger import logger
from schemas import *
import os
from flask_cors import CORS

# Instanciando o objeto OpenAPI com as informações da API
info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definindo tags para agrupamento das rotas
home_tag = Tag(
    name="Documentação",
    description="Seleção de documentação: Swagger, Redoc ou RapiDoc",
)
pessoa_tag = Tag(
    name="Pessoa",
    description="Adição, visualização, remoção e predição de pessoa com um distúrbio do sono",
)

# Rota home
@app.get("/", tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação."""
    return redirect("/openapi")


# Rota de listagem de pacientes
@app.get(
    "/pessoas",
    tags=[pessoa_tag],
    responses={"200": PessoaViewSchema, "404": ErrorSchema},
)
def get_pessoas():
    """Lista todas as pessoas cadastradas na base de dados."""
    session = Session()

    # Buscando todas as pessoas cadastradas
    pessoas = session.query(Pessoa).all()

    if not pessoas:
        logger.warning("Não há pessoas cadastradas na base.")
        return {"message": "Não há pessoas cadastradas na base."}, 404
    else:
        logger.debug(f"{len(pessoas)} pessoas encontradas.")
        return apresenta_pessoas(pessoas), 200


# Rota de adição de pessoa
@app.post(
    "/pessoa",
    tags=[pessoa_tag],
    responses={"200": PessoaViewSchema, "400": ErrorSchema, "409": ErrorSchema},
)
def predict(form: PessoaSchema):
    """Adiciona uma nova pessoa à base de dados e retorna o diagnóstico previsto."""
    
    # Definindo o caminho base para o diretório do modelo
    base_dir = r'C:\Users\Giovanny\Desktop\PUCRJ MVP Sprint 3 - Qualidade de Software, Segurança e Sistemas Inteligentes\API\sleep_health\Back\ml_model'
    
    # Caminhos completos para os arquivos do modelo e scaler
    ml_path = os.path.join(base_dir, "sleep_health_knn.joblib")
    scaler_path = os.path.join(base_dir, "scaler_knn.joblib")

    # Instanciando o objeto Model
    modelo = Model()  # Instância da classe Model

    # Carregando o modelo de machine learning
    modelo.carrega_modelo(ml_path, scaler_path)  # Carregar o modelo e o scaler usando a instância criada


    pessoa = Pessoa(
        person_id=form.person_id,
        gender=form.gender,
        age=form.age,
        sleep_duration=form.sleep_duration,
        quality_sleep=form.quality_sleep,
        activity_level=form.activity_level,
        stress_level=form.stress_level,
        bmi_category=form.bmi_category,
        blood_pressure=form.blood_pressure,
        heart_rate=form.heart_rate,
        daily_steps=form.daily_steps,
        outcome=Model.preditor(modelo, form),
    )
    logger.info(f"Adicionando pessoa de número: '{pessoa.person_id}'")

    try:
        # Criando sessão com o banco de dados
        session = Session()

        # Verifica se a pessoa já está cadastrada
        if session.query(Pessoa).filter(Pessoa.person_id == form.person_id).first():
            error_msg = "Pessoa já existente na base."
            logger.warning(f"Erro ao adicionar pessoa '{pessoa.person_id}', {error_msg}")
            return {"message": error_msg}, 409

        # Adicionando pessoa
        session.add(pessoa)
        session.commit()
        logger.debug(f"Adicionado pessoa de número: '{pessoa.person_id}'")
        return apresenta_pessoa(pessoa), 200

    except Exception as e:
        error_msg = "Não foi possível salvar o novo registro."
        logger.warning(f"Erro ao adicionar pessoa '{pessoa.person_id}', {error_msg}")
        return {"message": error_msg}, 400


# Rota de busca de paciente por ID
@app.get(
    "/pessoa",
    tags=[pessoa_tag],
    responses={"200": PessoaViewSchema, "404": ErrorSchema},
)
def get_pessoa(query: PessoaBuscaSchema):
    """Busca uma pessoa cadastrada na base de dados pelo ID."""
    
    pessoa_id = query.person_id
    logger.debug(f"Coletando dados sobre pessoa #{pessoa_id}")
    session = Session()
    
    pessoa = session.query(Pessoa).filter(Pessoa.person_id == pessoa_id).first()

    if not pessoa:
        error_msg = f"Pessoa {pessoa_id} não encontrada na base."
        logger.warning(f"Erro ao buscar pessoa '{pessoa_id}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        logger.debug(f"Pessoa encontrada: '{pessoa_id}'")
        return apresenta_pessoa(pessoa), 200


# Rota de remoção de paciente por ID
@app.delete(
    "/pessoa",
    tags=[pessoa_tag],
    responses={"200": PessoaViewSchema, "404": ErrorSchema},
)
def delete_pessoa(query: PessoaBuscaSchema):
    """Remove uma pessoa cadastrada na base de dados pelo ID."""
    
    pessoa_id = query.person_id
    logger.info(f"Deletando dados sobre pessoa #{pessoa_id}")
    
    session = Session()

    # Buscando a pessoa na base de dados
    pessoa = session.query(Pessoa).filter(Pessoa.person_id == pessoa_id).first()

    if not pessoa:
        error_msg = "Pessoa não encontrada na base."
        logger.warning(f"Erro ao deletar pessoa '{pessoa_id}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        session.delete(pessoa)
        session.commit()
        logger.debug(f"Pessoa #{pessoa_id} deletada com sucesso.")
        return {"message": f"Pessoa {pessoa_id} removida com sucesso!"}, 200

if __name__ == "__main__":
    app.run(debug=True)
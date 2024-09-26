from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

# Importa os elementos necessários definidos no modelo
from model.base import Base
from model.pessoa import Pessoa
from model.modelo import Model

# Diretório para armazenamento do banco de dados
db_path = "database/"

# Verifica se o diretório existe; se não, cria-o
if not os.path.exists(db_path):
    os.makedirs(db_path)

# URL de conexão com o banco de dados (SQLite)
db_url = f"sqlite:///{db_path}/sleep-health.sqlite3"

# Inicializa a engine para conexão com o banco de dados
engine = create_engine(db_url, echo=False)

# Configura a fábrica de sessões vinculada à engine
Session = sessionmaker(bind=engine)

# Cria o banco de dados se ele não existir
if not database_exists(engine.url):
    create_database(engine.url)

# Cria todas as tabelas definidas pelo metadata do modelo, caso ainda não existam
Base.metadata.create_all(engine)

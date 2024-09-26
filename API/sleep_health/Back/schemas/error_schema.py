from pydantic import BaseModel

class ErrorSchema(BaseModel):
    """ 
    Define o esquema para representar uma mensagem de erro.
    """
    message: str

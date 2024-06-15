from typing import Annotated
from pydantic import Field
from dio_fastapi_crossfit.contrib.schemas import BaseSchema


class CentroTreinamento(BaseSchema):
    nome: Annotated[str, Field(description='Nome do centro de treinamento', example='CT King', max_length=20)]
    endereco: Annotated[str, Field(description='Endereco do centro de treinamento', example='Rua X Q02', max_length=60)]
    proprietario: Annotated[str, Field(description='Proprietario do centro de treinamento', example='Marcos', max_length=30)]
from fastapi import APIRouter, Body, status

from dio_fastapi_crossfit.atleta.schemas import AtletaIn
from dio_fastapi_crossfit.contrib.dependecies import DatabaseDependency

router = APIRouter()

@router.post('/', summary='Criar novo atleta', status_code=status.HTTP_201_CREATED)
async def post(db_session: DatabaseDependency, atleta_in: AtletaIn = Body(...)):
    pass
"""Стандартные HTTP json ответы."""
from starlette.responses import JSONResponse
from starlette.status import (
    HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND,
    HTTP_422_UNPROCESSABLE_ENTITY
)

from src.responses.schemas import (
    CreateScheme, NotFoundScheme, UnpassableEntityScheme, OkScheme
)

OkJSONResponse = JSONResponse(
    content=OkScheme().dict(),
    status_code=HTTP_200_OK,
)

CreateJSONResponse = JSONResponse(
    content=CreateScheme().dict(),
    status_code=HTTP_201_CREATED,
)

NotFoundJSONResponse = JSONResponse(
    content=NotFoundScheme().dict(),
    status_code=HTTP_404_NOT_FOUND,
)

UnpassableEntityJSONResponse = JSONResponse(
    content=UnpassableEntityScheme().dict(),
    status_code=HTTP_422_UNPROCESSABLE_ENTITY,
)

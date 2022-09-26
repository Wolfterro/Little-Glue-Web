from fastapi import APIRouter, status, Body
from fastapi.responses import RedirectResponse

from views import generate_view
from views.examples.body_examples import generate_view_body_examples
from views.examples.response_examples import generate_view_response_examples

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK, include_in_schema=False)
async def root():
    """
    Redireciona para a documentação em /docs.
    """
    return RedirectResponse("/docs")


@router.post("/generate", status_code=status.HTTP_201_CREATED, responses=generate_view_response_examples)
async def generate(body: dict = Body(examples=generate_view_body_examples)):
    """
    Gera uma nova colinha com os dados passados através do body e fornece o caminho para download do arquivo.

    Para mais informações sobre o JSON passado no body, acesse:
    - https://github.com/Wolfterro/Little-Glue
    - https://github.com/Wolfterro/Little-Glue-Web
    """
    return generate_view(body)

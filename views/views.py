from fastapi.responses import JSONResponse
from core.little_glue import LittleGlue


def generate_view(body):
    try:
        little_glue = LittleGlue(**body)
        filename = little_glue.generate()
    except Exception as e:
        response_data = {
            "error": "Não foi possível gerar a colinha! Verifique os dados enviados e tente novamente.",
            "detail:": str(e)
        }
        return JSONResponse(response_data, status_code=500)

    if not filename:
        response_data = {
            "error": "Não foi possível gerar a colinha! Verifique os dados enviados e tente novamente.",
            "detail": None
        }
        return JSONResponse(response_data, status_code=400)

    return JSONResponse({"file": "/generated_glues/{}".format(filename)}, status_code=201)

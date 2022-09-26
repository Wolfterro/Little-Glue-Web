generate_view_response_examples = {
    201: {
        "content": {
            "application/json": {
                "example": {
                    "file": "/generated_glues/municipal_2022-09-26T00:21:05.jpg"
                }
            }
        },
        "description": "Retorna um JSON com o caminho para o download da colinha.",
    },
    400: {
        "content": {
            "application/json": {
                "example": {
                    "error": "Não foi possível gerar a colinha! Verifique os dados enviados e tente novamente.",
                    "detail": "Formato de exportação inválido."
                }
            }
        },
        "description": "Retorna um JSON indicando erro e o detalhe do erro.",
    },
    500: {
        "content": {
            "application/json": {
                "example": {
                    "error": "Não foi possível gerar a colinha! Verifique os dados enviados e tente novamente.",
                    "detail": "Formato de exportação inválido."
                }
            }
        },
        "description": "Retorna um JSON indicando erro e o detalhe do erro.",
    }
}

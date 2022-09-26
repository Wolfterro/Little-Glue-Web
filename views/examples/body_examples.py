generate_view_body_examples = {
    "presidential": {
        "summary": "Eleições Presidenciais",
        "description": "Exemplo de geração de colinha para eleições presidenciais.",
        "value": {
            "candidates_data": {
                "federal_deputy": [
                    {
                        "number": "9999",
                        "name": "João da Feira"
                    }
                ],
                "state_deputy": [
                    {
                        "number": "99999",
                        "name": "Marcos do Gás"
                    }
                ],
                "senator": [
                    {
                        "number": "999",
                        "name": "Toninho da Padaria"
                    }
                ],
                "governor": {
                    "number": "99",
                    "name": "Delegado José"
                },
                "president": {
                    "number": "99",
                    "name": "Professor Pereira"
                }
            },
            "color_scheme": ["#ffffff", "#000000"],
            "export_format": "pdf",
            "font_configs": [12, 32, 15, "bold"],
            "election_type": "presidential"
        }
    },
    "municipal": {
        "summary": "Eleições Municipais",
        "description": "Exemplo de geração de colinha para eleições municipais.",
        "value": {
            "candidates_data": {
                "alderman": [
                    {
                        "number": "99999",
                        "name": "João da Feira"
                    }
                ],
                "prefect": {
                    "number": "99",
                    "name": "Professor Pereira"
                }
            },
            "color_scheme": ["#ffffff", "#000000"],
            "export_format": "jpg",
            "font_configs": [12, 32, 15, "bold"],
            "election_type": "municipal"
        }
    }
}

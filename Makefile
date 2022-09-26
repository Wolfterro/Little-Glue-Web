run:
	@uvicorn main:app --reload

install:
	@sudo apt-get update
	@sudo apt-get install -y wkhtmltopdf
	@echo "================================================================================"
	@echo "===!!! Você vai precisar criar agora uma virtualenv para rodar o projeto! !!!==="
	@echo "================================================================================"
	@echo "===!!! Para isso, execute: mkvirtualenv liitle-glue --python=python3 && workon little-glue"
	@echo ""
	@echo "===!!! OU !!!==="
	@echo ""
	@echo "===!!! Execute este: virtualenv little-glue --python=python3 && source little-glue/bin/activate"
	@echo "===!!! Após esse processo, execute o comando: pip install -r requirements.txt"
	@echo "===!!! E pronto, basta rodar o projeto usando o comando: make run"

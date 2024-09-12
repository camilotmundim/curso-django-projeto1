Execute os comandos abaixo em um terminal (bash/prompt) *dentro da pasta raiz deste projeto*.

    # criar um ambiente virtual do Python 
    python -m venv venv

    # Ativar ambiente virtual
    . venv/bin/activate 
    (Windows: venv\Scripts\activate)

    # instalar as dependencias...
    python -m pip install -r requirements-dev.txt

    # Desativar ambiente virtual
    deactivate
    
    #Ativar o Pré-commit, para padronização e organização do projeto
    pre-commit install
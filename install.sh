#!/bin/bash

# Clonar o repositório em /tmp/loteria
git clone git@github.com:juliano777/loteria.git /tmp/loteria

# Acessar o diretório
cd /tmp/loteria

# Criar ambiente virtual
python3 -m venv /tmp/venv

# Habilitar o ambiente virtual
source /tmp/venv/bin/activate

# Instalar requerimentos
pip install -r /tmp/loteria/requirements.txt


# PI-4-Petshop


Como executar o projeto no ambiente Windows

Istalar o Python
git clone https://github.com/Valdelainecristinaribeiro/PI-4-Petshop.git
cd lPI-4-Petshop
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
cd Shop
python manage.py makemigrations
python manage.py migrate
python manage.py runserver



Como executar o projeto no ambiente Linux

Istalar o Python
Ambiente Linux:
git clone https://github.com/Valdelainecristinaribeiro/PI-4-Petshop.git
cd lPI-4-Petshop
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
cd Shop
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
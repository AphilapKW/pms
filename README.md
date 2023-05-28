# pms


# set environment
cd /backend/

brew install python

python -m pip install --user --upgrade pip

python -m pip install --user virtualenv

python -m venv venv

source venv/bin/activate

python -m pip install --upgrade pip

pip install -r requirements.txt 

Enjoy!!


# runserver

python manage.py runserver 8001


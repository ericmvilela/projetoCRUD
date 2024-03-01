import os
from dotenv import load_dotenv

load_dotenv()

# configuração db
db = os.environ.get('DB')
user_db = os.environ.get('USER_DB')
password_db = os.environ.get('PASSWORD_DB')
host_db = os.environ.get('HOST_DB')
port_db = os.environ.get('PORT_DB')
name_db = os.environ.get('NAME_DB')

SQLALCHEMY_DATABASE_URI = f'{db}://{user_db}:{password_db}@{host_db}:{port_db}/{name_db}'
SQLALCHEMY_TRACK_MODIFICATIONS = True

# assinatura
SECRET_KEY = os.environ.get('SECRET_KEY', 'not secure')

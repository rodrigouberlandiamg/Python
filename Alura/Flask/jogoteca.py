from flask import Flask
from flask_mysqldb import MySQL

# Criar objeto
app = Flask(__name__)
app.config.from_pyfile('config.py')

# Instaciar Banco de dados
db = MySQL(app)

from views import *

if __name__ == '__main__':
    # Iniciar Server
    app.run(debug=True)
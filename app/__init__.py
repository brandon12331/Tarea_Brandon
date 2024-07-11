from flask import Flask

app = Flask(__name__)
app.secret_key = 'secret_key'

# Importa las rutas después de crear la aplicación
from app import routes

from config.database import init_app
from flask import Flask

app = Flask(__name__)

# Initialiser la base de données
init_app(app)

if __name__ == "__main__":
    app.run(debug=True)

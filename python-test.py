from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "¡Hola, mundo!"

@app.route("/acerca-de")
def about():
    return "Esta es una aplicación web básica creada con Flask"

if __name__ == "__main__":
    app.run()

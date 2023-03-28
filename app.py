from flask import Flask
import random

app = Flask(__name__)

counter = 0
numbers = []

@app.route("/")
def index():
    global counter
    global numbers
    
    counter += 1
    numbers.append(random.randint(1, 1000000))
    
    return f"Hola, mundo! Esta página ha sido vista {counter} veces"

@app.route("/numbers")
def show_numbers():
    global numbers
    
    return str(numbers)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

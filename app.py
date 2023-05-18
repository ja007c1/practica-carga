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
    numbers.append(random.randint(1, 1000000000000))
    
    # Realizar un cálculo intensivo de manera repetida
    for i in range(1000000):
        x = i ** 2
    return f"Esta página ha sido vista {counter} veces"

@app.route("/reset")
def reset():
    global counter
    global numbers
    
    counter = 0
    numbers = []
    
    return "Memoria reiniciada"

@app.route("/healthcheck")
def healthcheck():
    return "OK"

@app.route("/numbers")
def show_numbers():
    global numbers
    
    return str(numbers)

@app.route("/memory_intensive")
def memory_intensive():
    # Uso intensivo de memoria
    memory_list = []
    #for _ in range(100000):
    #    memory_list.append([0] * 100000)
    for _ in range(10000):
        memory_list.append([0] * 10000)
    
    return "Uso intensivo de memoria realizado"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

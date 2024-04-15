from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route("/<name>")
def freet(name):
    return f"Hello there {name}!"

if __name__ == "__main__":
    #execute only if run as a script
    app.run(debug=True)
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    #execute only if run as a script
    app.run()
from flask import Flask
app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper



@app.route('/')
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/<name>")
def freet(name):
    return f"Hello there {name}!"

@app.route("/bye")
@make_bold
def bye():
    return "Bye!"

if __name__ == "__main__":
    #execute only if run as a script
    app.run(debug=True)
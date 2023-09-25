from flask import Flask

app = Flask(__name__)

@app.route('/') #decorator
def home():
    return "Welcome to my first Flask demo!"

@app.route('/about/') #decorator
def about():
    return "This is about section"

if __name__ == "__main__":
    app.run(debug=True)
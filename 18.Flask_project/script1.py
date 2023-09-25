from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') #decorator
def home():
    return render_template("home.html") #html file should be under templates folder

@app.route('/about/') #decorator
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
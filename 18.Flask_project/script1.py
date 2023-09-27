from flask import Flask, render_template
# we can use pythonanywhere to deploy our python code and use python virtual 
#  env for flask projects

app = Flask(__name__)

@app.route('/') #decorator
def home():
    return render_template("home.html") #html file should be under templates folder

@app.route('/about/') #decorator
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
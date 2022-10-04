from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/') 
def index():
    return render_template("index.html")

@app.route('/profile') 
def profile():
    return render_template("profile.html")

@app.route('/listpokemon') 
def listpokemon():
    return render_template("listpokemon.html")

@app.route('/randompokemon') 
def randompokemon():
    return render_template("randompokemon.html")

@app.route('/getpokemon') 
def getpokemon():
    return render_template("getpokemon.html")

@app.route('/dataplayer') 
def dataplayer():
    return render_template("dataplayer.html")

@app.route('/battle') 
def battle():
    return render_template("battle.html")

if __name__ == "__main__":
    app.run(debug=True)

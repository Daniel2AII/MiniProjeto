from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def Index():
    return render_template("Index.html")

@app.route("/formulario")
def Form():
    return render_template("Formulario.html")
    

if __name__ == "__main__":
    app.run(debug = True)
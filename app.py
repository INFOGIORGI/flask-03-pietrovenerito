from flask import Flask, render_template  

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html",titolo='Home Page')

@app.route("/dettagli")
def detail():
    prodotti = (("Laptop","6","50€"), ("telefono","5","50€"),("computer","2","1000€"))
    return render_template("detail.html",titolo='Dettagli',prodotti=prodotti)

app.run()

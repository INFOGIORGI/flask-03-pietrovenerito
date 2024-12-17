from flask import Flask, render_template  

app = Flask(__name__)
prodotti = (("Laptop","6","50€"), ("telefono","5","50€"),("computer","2","1000€"))

@app.route("/")
def home():
    return render_template("home.html",titolo='Home Page')

@app.route("/dettagli")
def detail():
    return render_template("detail.html",titolo='Dettagli',prodotti=prodotti)

@app.route("/scaffale/<numscaffale>")
def scaffale(numscaffale):
    l=[]
    for t in prodotti:
        if t[1]==numscaffale:
            l.append(t)
    return render_template("scaffale.html",titolo='Scaffale',numscaffale=numscaffale,prodotti=l)



app.run()

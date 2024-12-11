from flask import Flask, render_template, request
app = Flask(__name__)


conteudos = []
@app.route('/', methods=["GET","POST"])
def principal():
    if request.method == "POST":
        if request.form.get("conteudo"):
            conteudos.append(request.form.get("conteudo"))

    return render_template("index.html",conteudos=conteudos,)

@app.route('/diario')
def diario():
    diario = {
        "Fulano":5,
        "Beltrano":5.8,
        "Sicrano":5.2,
        "Styven":10,

    }
    return render_template("diario.html",diario=diario)


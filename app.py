from flask import Flask, render_template, request
from list_movie import data_json
app = Flask(__name__)


conteudos = []
@app.route('/', methods=["GET","POST"])
def principal():
    if request.method == "POST":
        if request.form.get("conteudo"):
            conteudos.append(request.form.get("conteudo"))

    return render_template("index.html",conteudos=conteudos,)






diarios = []
@app.route('/diario', methods=["GET","POST"])
def diario():
    if request.method == "POST":
        if request.form.get("aluno") and request.form.get("nota"):
            aluno = request.form.get("aluno")
            nota = request.form.get("nota")
            diarios.append({"aluno":aluno, "nota":nota})
    
    return render_template("diario.html",diarios=diarios)


@app.route('/filmes')
def list_movie():
    return render_template("movie.html",filmes=data_json)


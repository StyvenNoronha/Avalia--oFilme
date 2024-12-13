from flask import Flask, render_template, request
from list_movie import list_movies
from flask_sqlalchemy import SQLAlchemy
from livros import Livro

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///livros.sqlite3'

db = SQLAlchemy()
db.init_app(app)

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


@app.route('/filmes/<props>')
def list_movie(props):
    return render_template("movie.html",filmes=list_movies(props))


@app.route('/livros')
def list_books():
    return render_template("livros.html", book=Livro.query.all())


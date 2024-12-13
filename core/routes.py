from core import app, db
from flask import render_template, request, redirect, url_for
from core.list_movie import list_movies
from core.livros import Livro
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
    return render_template("livros.html", livro=Livro.query.all())



@app.route('/cadLivros', methods=["GET","POST"])
def cadastro_livros():
    nome = request.form.get('nome')
    valor = request.form.get('valor')
    descricao = request.form.get('descricao')

    if request.method == 'POST':
        livro= Livro(nome,descricao,valor)
        db.session.add(livro)
        db.session.commit()
        return redirect(url_for('list_books'))

    return render_template("cadastroLivros.html")



@app.route('/atualiza_livro/<int:id>', methods=["GET","POST"])
def atualiza_livro(id):
    livroDb = Livro.query.filter_by(id=id).first()
    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        valor = request.form['valor']

        Livro.query.filter_by(id=id).update({
            "nome":nome,
            "valor":valor,
            "descricao": descricao
        })   
        db.session.commit()
        return redirect(url_for('list_books'))
    return render_template("atualizaLivro.html", livro=livroDb)


@app.route('/delete_book/<int:id>')
def remove_livro(id):
    livroDb = Livro.query.filter_by(id=id).first()
    if livroDb:
        db.session.delete(livroDb)
        db.session.commit()
    return redirect(url_for('list_books'))

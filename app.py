from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    conteudos = [
        'manipulação de dados',
        'Herança e Templates',
        'integração de APIs',
        'Banco de dados'

    ]

    return render_template(
        "index.html",
        conteudos=conteudos,
        )

@app.route('/sobre')
def sobre():
    return render_template("sobre.html")


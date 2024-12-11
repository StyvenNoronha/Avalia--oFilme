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

@app.route('/diario')
def diario():
    diario = {
        "Fulano":5,
        "Beltrano":5.8,
        "Sicrano":5.2,
        "Styven":10,

    }
    return render_template("diario.html",diario=diario)


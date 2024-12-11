from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    conteudo = 'manipulação de dados'
    conteudo1 = 'Herança e Templates'
    conteudo2 = 'integração de APIs'
    conteudo3 = 'Banco de dados'
    return render_template(
        "index.html",
        conteudo=conteudo,
        conteudo1=conteudo1,
        conteudo2=conteudo2,
        conteudo3=conteudo3
        )

@app.route('/sobre')
def sobre():
    return render_template("sobre.html")


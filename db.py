from app import db
from app import app
from livros import Livro

app.app_context().push()
db.create_all()

livro1 = Livro(nome="Naruto",descricao="Top", valor=35)

db.session.add(livro1)
db.session.commit()
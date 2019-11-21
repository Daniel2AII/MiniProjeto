from flask import Flask, render_template
from Forms import MensagemForm, CadastroUsuario
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///msgs.db'
app.config['SECRET_KEY'] = "vbhfdbvhbfdvbfdbvfd"
db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    senha = db.Column(db.String(10), unique=False, nullable=False)
    mensagem = db.relationship('Mensagem', backref='usuario', lazy=True)

    def __repre__(self):
        return '[User: %r]' % self.login    

class Mensagem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mensagem = db.Column(db.Text, nullable=False)
    titulo = db.Column(db.String(100), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)

    def __repre__(self):
        return self.mensagem

        
@app.route("/")
def Index():
    return render_template("Index.html")

@app.route("/cadastro", methods=['POST', 'GET'])
def Form():

    form = CadastroUsuario()
    print(form.login.data)
    print(form.email.data)
    print(form.senha.data)

    if form.validate_on_submit():
        user1 = Usuario()
        user1.login = form.login.data
        user1.email = form.email.data
        user1.senha = form.senha.data
        db.session.add(user1)
        db.session.commit()

    return render_template("Cadastro.html", form=form)

@app.route("/mensagem", methods=['POST', 'GET'])
def MSG():

    form = MensagemForm()
    print(form.mensagem.data)
    print(form.titulo.data)

    if form.validate_on_submit():
        msg = Mensagem()
        msg.mensagem = form.mensagem.data
        msg.titulo = form.titulo.data
        db.session.add(msg)
        db.session.commit()

    return render_template("Mensagem.html", form=form)    

if __name__ == "__main__":
    app.run(debug = True)
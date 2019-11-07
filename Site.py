from flask import Flask, render_template
from Forms import MensagemForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///msgs.db'
app.config['SECRET_KEY'] = "vbhfdbvhbfdvbfdbvfd"
db = SQLAlchemy(app)

class Mensagem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mensagem = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<MSG: %r>' % self.mensagem

        
@app.route("/")
def Index():
    msgs = Mensagem.query.filter_by(mensagem=mensagem).first()
    return render_template("Index.html", msgs=msgs)

@app.route("/formulario", methods=['POST', 'GET'])
def Form():
    form = MensagemForm()
    if form.validate_on_submit():
        msg = Mensagem()
        msg.mensagem = form.mensagem.data
        db.session.add(msg)
        db.session.commit()

    return render_template("Formulario.html", form=form)


if __name__ == "__main__":
    app.run(debug = True)
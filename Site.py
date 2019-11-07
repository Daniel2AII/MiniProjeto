from flask import Flask, render_template
from Forms import MensagemgForm
from flask_sqlalchemy import SQLALchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///msgs.db'
app.config['SECRET_KEY'] = ""
db = SQLAlchemy(app)

class Msg(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    msg = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<MSG: %r>' % self.msg

        
@app.route("/")
def Index():
    msgs = Mensagem.query.all()
    return render_template("Index.html", msgs=msgs)

@app.route("/formulario", methods=['POST', 'GET'])
def Form():
    form = MensagemForm()
    if form.validate_on_submit():
        msg1 = MensagemForm()
        msg1.mensagem = form.mensagem.data
        db.session.add()
        db.session.commit()

    return render_template("Formulario.html", form=form)


if __name__ == "__main__":
    app.run(debug = True)
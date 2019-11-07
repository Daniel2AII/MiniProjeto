from flask_sqlalchemy import SQLAlchemy
from Site import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///msgs.db'
db = SQLAlchemy(app)

class Msg(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    msg = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<MSG: %r>' % self.msg
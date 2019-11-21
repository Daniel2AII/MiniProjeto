from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email

class CadastroUsuario(FlaskForm):
    login = StringField('Login', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    button = SubmitField('Fazer Cadastro')

class MensagemForm(FlaskForm):
    mensagem = StringField('Mensagem', validators=[DataRequired()])
    titulo = StringField('Título', validators=[DataRequired()])
    button = SubmitField('Enviar MSG')
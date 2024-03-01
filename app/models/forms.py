from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, TextAreaField
from wtforms.validators import DataRequired, NumberRange
from wtforms import DecimalField


class ProdutoForm(FlaskForm):
    nome = StringField('nome', validators=[DataRequired()])
    preco = DecimalField('preco', validators=[DataRequired(), NumberRange(min=0)])
    descricao = TextAreaField('descricao', validators=[DataRequired()])


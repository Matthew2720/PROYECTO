from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,TextAreaField,BooleanField
from wtforms.validators import DataRequired,Email,Length

class SignupForm(FlaskForm):
    name_vet = StringField('Nombre_vet', validators=[DataRequired(), Length(max=50)])
    city_vet = StringField('Ciudad_vet', validators=[DataRequired(), Length(max=50)])
    name = StringField('Nombre', validators=[DataRequired(), Length(max=50)])
    lastname = StringField('Nombre', validators=[DataRequired(), Length(max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Registrar')
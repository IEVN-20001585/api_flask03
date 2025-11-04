from wtforms import Form, FloatField, StringField,  EmailField, PasswordField, IntegerField
from wtforms import validators

class UserForm(Form):
    matricula=IntegerField('Matricula',
                           [validators.DataRequired(message="La matricula es obligatoria ")])
    nombre=StringField("Nombre", 
                       [validators.DataRequired(message='El campo es requerido')])
    apellido=StringField("Apellido",
                          [validators.DataRequired(message='El campo es requerido')])
    correo=StringField("Correo",
                          [validators.DataRequired(message='El Correo no es valido')])
    
    
class FigurasForm(Form):
    valor1 = IntegerField(
        'Primer numero',
        [validators.DataRequired(message="Ingresa un numero")]
    )

    valor2 = IntegerField(
        'Segundo numero',
        [validators.Optional()]
    )
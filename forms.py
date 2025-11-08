from wtforms import Form, FloatField, StringField,  EmailField, PasswordField, IntegerField
from wtforms import validators
import forms as formularios

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
class PizzaForm(Form):
    nombre = StringField('Nombre', [validators.DataRequired(message="El nombre es obligatorio")])
    direccion = StringField('Direccion', [validators.DataRequired(message="La dirección es obligatoria")])
    telefono = StringField('Telefono', [validators.DataRequired(message="El teléfono es obligatorio")])
    cantidad = IntegerField('Cantidad', [
        validators.NumberRange(min=1, message="Debe ser al menos 1"),
        validators.DataRequired(message="La cantidad es obligatoria")
    ])
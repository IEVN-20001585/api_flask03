from flask import Flask,render_template, request
import forms


app =Flask(__name__)

@app.route('/')
def home():
    return "Hello, Word!"


@app.route("/figuras", methods=['GET', 'POST'])
def figuras():
    form = forms.FigurasForm(request.form)
    area = ""
    figura = ""
    
    if request.method == 'POST' and form.validate():
        figura = request.form.get('figura')
        f1 = form.valor1.data
        f2 = form.valor2.data

        if figura == 'circulo':
            area = 3.1416 * (f1 * f1)
        elif figura == 'triangulo':
            area = (f1 * f2) / 2
        elif figura == 'rectangulo':
            area = f1 *f2
        elif figura == 'cuadrado':
            area = f1 * f1

    return render_template('figuras.html', form=form, area=area, figura=figura)

@app.route("/Alumnos", methods=['GET','POST']) 
def alumnos():
    mat=0
    nom=""
    ape=""
    em=""
    alumnos_clase=forms.UserForm(request.form)
    if request.method=='POST':
        mat=alumnos_clase.matricula.data
        nom=alumnos_clase.nombre.data
        ape=alumnos_clase.apellido.data
        em=alumnos_clase.correo.data
    return render_template('alumnos.html', form=alumnos_clase, mat=mat, nom=nom,ape=ape, em=em)

    
    

@app.route('/index')
def index():
    titulo="IEVN1003"
    listado=["Opera 1,Opera 2,Opera 3,Opera 4"]
    return render_template('index.html',titulo=titulo, listado=listado)

@app.route('/operas',  methods=['GET','POST'])
def operas():
    if request.method=='POST':
        x1=request.form.get('x1')
        x2=request.form.get('x2')
        resultado=x1+x2
        return render_template('operas.html', resultado=resultado)

    return render_template('operas.html')

@app.route('/distancia')
def distancia():
    return render_template('distancia.html')


@app.route('/layout')
def layout():
    return render_template('layout.html')

@app.route('/about')
def about():
    return"<h1> This is the about page.</h1>"

@app.route("/user/<string:user>")
def user(user):
    return "Hola" + user

@app.route("/numero/<int:n>")
def numero(n):
    return"Numero: {}".format(n)

@app.route("/user/<int:id>/<string:username>")
def username(id,username):
    return"ID : {} nombre {}".format(id,username)

@app.route("/suma/<float:n1>/<float:n2>")
def func(n1,n2):
    return "La suma es: {}".format(n1+n2)

@app.route("/prueba")
def prueba():
    return ''' 
    <h1>Prueba de HTML</h1>
    <p>Esto es un parrafo</p>
    <ul>
    <li>Elemento 1 </li>
 <li> Elemento 2</li>
   <li> Elemento 3</li>
   </ul>
   '''
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask,render_template, request, make_response, jsonify
import json
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
    estudiantes=[]
    tem=[]
    datos={}

    alumnos_clase=forms.UserForm(request.form)
    if request.method=='POST'and alumnos_clase.validate():
        mat=alumnos_clase.matricula.data
        nom=alumnos_clase.nombre.data
        ape=alumnos_clase.apellido.data
        em=alumnos_clase.correo.data
        datos={"matricula":mat, "nombre":nom, "apellido":ape,"correo":em}
        
        datos_str=request.cookies.get('estudiante')
        if not datos_str:
           return "No hay cookie"
        tem=json.loads(datos_str)
        estudiantes=tem
        estudiantes.append(datos)
    response= make_response(render_template('Alumnos.html', 
                                            form=alumnos_clase,mat=mat, ape=ape ,nom=nom,em=em))
    response.set_cookie('estudiante', json.dumps(estudiantes))
    return response 
@app.route("/get_cookie")
def get_cookie():
    datos_str=request.cookies.get('estudiante')
    if not datos_str:
        return "No hay cookie"
    datos=json.loads(datos_str)

    return jsonify(datos)

@app.route("/Pizza", methods=['GET', 'POST'])
def pizza():
    nom = ""
    dir = ""
    tel = ""
    tam = ""
    cant = 0
    pizzas = []
    ventas = []
    total_dia = 0
    mostrar_ventas = False
    precios = {'chica': 40, 'mediana': 80, 'grande': 120}
    pizza_form = forms.PizzaForm(request.form)
    datos_str = request.cookies.get('pizzas')
    if datos_str:
        try:
            pizzas = json.loads(datos_str)
        except:
            pizzas = []

    ventas_str = request.cookies.get('ventas')
    if ventas_str:
        try:
            ventas = json.loads(ventas_str)
            total_dia = sum(v.get('total', 0) for v in ventas)
        except:
            ventas = []
  
    mostrar_cookie = request.cookies.get('mostrar_ventas')
    if mostrar_cookie == 'true':
        mostrar_ventas = True

    if request.method == 'POST':
        accion = request.form.get('accion')

     
        if accion == 'agregar' and pizza_form.validate():
            nom = pizza_form.nombre.data
            dir = pizza_form.direccion.data
            tel = pizza_form.telefono.data
            tam = request.form.get('tamano')
            ingredientes = request.form.getlist('ingrediente')
            cant = pizza_form.cantidad.data

            sub = precios.get(tam, 0) * cant + len(ingredientes) * 10 * cant
            datos = {
                "nombre": nom,
                "direccion": dir,
                "telefono": tel,
                "tamano": tam,
                "ingredientes": ", ".join(ingredientes),
                "cantidad": cant,
                "subtotal": sub
            }
            pizzas.append(datos)
            mostrar_ventas = False 

        elif accion == 'quitar':
            if pizzas:
                pizzas.pop()
            mostrar_ventas = False  
    
        elif accion == 'terminar':
            if pizzas:
                total_pedido = sum(p.get('subtotal', 0) for p in pizzas)
                venta = {"nombre": pizzas[0].get('nombre', 'Cliente'), "total": total_pedido}
                ventas.append(venta)
                total_dia = sum(v.get('total', 0) for v in ventas)
                pizzas = []
            mostrar_ventas = False  

        
        elif accion == 'ver_ventas':
       
            mostrar_ventas = not mostrar_ventas

    
    response = make_response(render_template(
        "Pizza.html",
        form=pizza_form,
        pizzas=pizzas,
        ventas=ventas,
        total_dia=total_dia,
        mostrar_ventas=mostrar_ventas
    ))

  
    response.set_cookie('pizzas', json.dumps(pizzas))
    response.set_cookie('ventas', json.dumps(ventas))
    response.set_cookie('mostrar_ventas', 'true' if mostrar_ventas else 'false')

    return response


@app.route("/get_ventas")
def get_ventas():
    datos_str = request.cookies.get('ventas')
    if not datos_str:
        return "No hay cookie"
    try:
        datos = json.loads(datos_str)
    except:
        datos = []
    return jsonify(datos)


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
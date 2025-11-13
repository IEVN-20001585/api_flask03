from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS
from config import config

app = Flask(__name__)
conexion=MySQL(app)

@app.route('/alumnos', methods=['GET'])
def listar_alumnos():
    try:
        cursor=conexion.connection.cursor()
        sql="SELECT matricula, nombre, apaterno,amaterno,correo FROM alumnos"
        cursor.execute(sql)
        datos=cursor.fetchall()
        alumnos=[]
        for fila in datos:
            alumno= {'matricula':fila[0],'nombre':fila[1],'apellido':fila[2],'correo':fila[3]}
            alumnos.append(alumno)
        return jsonify({'alumnos':alumnos, 'mensaje':'Alumnos encontrados',"exito":True})
    except Exception as ex:
        return jsonify({'mensaje':'Error al listar alumnos:{} '+str(ex),"exito":False})


                            

def pagina_no_encontrada(error):
    return "<h1> La pagina que intentas buscar no existe</h1>", 404


def leer_alumno_bd(matricula):
    try:
        cursor = conexion.connection.cursor()
        sql="SELECT matricula, nombre, apaterno,amaterno,correo FROM alumnos WHERE matricula = {0}".format(matricula)
        cursor.execute(sql)
        datos=cursor.fetchone()
        if datos != None:
            alumno = {'matricula':datos[0],'nombre':datos[1],'aparterno':[2],'amaterno':[3],'correo':datos[4]}
            return alumno
        else:
            return None
    except Exception as ex:
        raise ex
            
@app.route('/alumnos/<mat>', methods=['GET'])
def leer_curso(mat):
    try:
        alumno = leer_alumno_bd(mat)
        if alumno is not None:
            return jsonify({'alumno': alumno, 'mensaje': 'Alumno encontrado', 'exito': True})
        else:
            return jsonify({'mensaje': 'Alumno no encontrado', 'exito': False})
    except Exception as ex:
        return jsonify({'mensaje': f'Error: {str(ex)}', 'exito': False})
 
    
if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()
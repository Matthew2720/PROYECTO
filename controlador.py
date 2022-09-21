from flask import Flask,render_template,request
from conexion import *
from models import *

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    return render_template("index.html")#,name=name)

@app.route('/registro', methods=['GET','POST'])
def registro():
    if request.method=="POST":
        nombre_vet = request.form.get("nombre_vet")
        ciudad_vet = request.form.get("ciudad_vet")
        nombre = request.form.get("nombre")
        apellido = request.form.get("apellido")
        documento = request.form.get("documento")
        password = request.form.get("password")
        telefono = request.form.get("telefono")
        email = request.form.get("email")
        veterinaria = Veterinaria(nombre_vet,ciudad_vet,nombre,apellido,documento,telefono,email,password)
        veterinaria.crear_contacto()
        return render_template ("index.html")
    else:
        return render_template("registro.html")

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=="POST":
        contra = request.form.get("password")
        nombre_vet = request.form.get("nombre_vet")
        print(nombre_vet + contra)
        inicio = Veterinaria.login(Veterinaria,nombre_vet,contra)  #CON ESTE METODO VALIDAMOS EL LOGIN
        if inicio[0] == True:
            nombrelogin = Veterinaria.get_name_veterinaria(nombre_vet) #CON ESTE METODO SI EL NOMBRE EXISTE LO PASAMOS COMO NOMBRE DE LOGIN
            print(inicio)
            return render_template('logued.html',logueado=nombrelogin[0])
        else:
            malingreso = "USUARIO O CONTRASEÑA INCORRECTA"
            return render_template("login.html",malingreso = malingreso)
    return render_template("login.html")

@app.route('/registroEmpleado',methods=['GET','POST'])
def regemp():
    if request.method=="POST":
        pass
    else:
        usuario = Veterinaria.get_logueado(Veterinaria,"vacio")
        if usuario:
            print("Inicio =")
            usuario = usuario[0]
            print(usuario)
            return render_template('regemp.html',user = usuario)
        else:
            return render_template('index.html')
    

@app.route('/prueba',methods=['GET'])
def prueba():
    return render_template('logued.html')
    
#INICIO DEL SERVIDOR
if __name__ == '__main__':
    app.run('127.0.0.1', 5000, debug=True)
from flask import Flask,render_template,request,redirect,url_for
from conexion import *
from models import *

app = Flask(__name__)

#LOGIN MANAGER
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = "login"

@app.route('/', methods=['GET','POST'])
def index():
    # name = "carlos"
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
        inicio = Veterinaria.login(nombre_vet,contra)  #CON ESTE METODO VALIDAMOS EL LOGIN
        if inicio:
            nombrelogin = Veterinaria.get_name_veterinaria(nombre_vet) #CON ESTE METODO SI EL NOMBRE EXISTE LO PASAMOS COMO NOMBRE DE LOGIN
            print(nombrelogin)
            return render_template('inicioexitoso.html',logueado=nombrelogin[0])
        else:
            malingreso = "USUARIO O CONTRASEÑA INCORRECTA"
            return render_template("login.html",malingreso = malingreso)
    return render_template("login.html")

@app.route('/logueado',methods=['GET'])
def sidio():
    return render_template("inicioexitoso.html")
    
#INICIO DEL SERVIDOR
if __name__ == '__main__':
    app.run('127.0.0.1', 5000, debug=True)
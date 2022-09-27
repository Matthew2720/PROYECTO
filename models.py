from conexion import *
# from werkzeug.security import generate_password_hash
class Veterinaria():
    logued = "vacio"
    #Metodo constructor
    def __init__(self,nombre_vet,ciudad_vet, nombre,apellido, documento, telefono, email,password):
        self.nombre_vet = nombre_vet
        self.ciudad_vet = ciudad_vet
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento
        self.telefono = telefono
        self.email = email
        self.password = password

#Método CREATE -> Crear una nueva persona o contacto de la base de datos
    def crear_contacto(self):
        #Creamos nueva instancia
            # hash = generate_password_hash(self.password)
            cursor = db.cursor()
            consulta = "INSERT INTO CENTRO(NOMBRE_VET,CIUDAD_VET,NOMBRE,APELLIDO,DOCUMENTO,TEL_CENTRO,EMAIL_CENTRO,PASSWORD) VALUES (?,?,?,?,?,?,?,?);"
            cursor.execute(consulta,self.nombre_vet,self.ciudad_vet,self.nombre,self.apellido,self.documento,self.telefono,self.email,self.password)
            cursor.commit()
            cursor.close()
            

    def login(self,nombre_vet,password):
        inicio = False
        cursor = db.cursor() #APUNTA A LA BASE DE DATOS
        #PRIMER CONSULTA
        consulta = "SELECT nombre_vet FROM CENTRO WHERE nombre_vet = ?"
        cursor.execute(consulta,nombre_vet)
        persona = cursor.fetchone()
        #SEGUNDA CONSULTA
        consulta2 = "SELECT password from CENTRO where password = ?"
        cursor.execute(consulta2,password)
        password = cursor.fetchone()
        if persona and password:
                inicio = True
                self.logued = persona
        else:
            inicio = False
        cursor.close()
        return inicio,self.logued
          
    def get_name_veterinaria(nombre_vet):
        cursor = db.cursor()
        consulta="SELECT nombre_vet FROM CENTRO WHERE nombre_vet = ?"
        cursor.execute(consulta,nombre_vet)
        existe = cursor.fetchone()
        if existe:
            print(existe)
            return existe
        else:
            print("No existe la veterinaria en la base de datos")
            
    def get_logueado(self,vacio):
        if vacio == self.logued:
            print("Sigue vacio")
        else:
            logued = self.logued
            return logued

# Veterinaria.login(Veterinaria,"Carlos","nomelase")
# jj = Veterinaria.get_logueado(Veterinaria,"vacio")
# print("Aqui esta el resultado")
# print(jj)

class Usuario():
    def __init__(self,documento,nombre_usuario,telefono,direccion,email):
         self.documento = documento
         self.nombre_usuario = nombre_usuario
         self.telefono = telefono
         self.direccion = direccion
         self.email = email
         
    def subirUsuario(self,veteApuntada):
            cursor = db.cursor()
            consulta = "INSERT INTO USUARIOS(id_Usuario,nombre_Usuario,tel_Usuario,direccion_Usuario,email_Usuario,fnombre_vet) VALUES (?,?,?,?,?,?);"
            cursor.execute(consulta,self.documento,self.nombre_usuario,self.telefono,self.direccion,self.email,veteApuntada)
            cursor.commit()
            cursor.close()
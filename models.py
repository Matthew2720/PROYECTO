from conexion import *
bool = False
class Veterinaria():
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
            cursor = db.cursor()
            consulta = "INSERT INTO CENTRO(NOMBRE_VET,CIUDAD_VET,NOMBRE,APELLIDO,DOCUMENTO,TEL_CENTRO,EMAIL_CENTRO,PASSWORD) VALUES (?,?,?,?,?,?,?,?);"
            cursor.execute(consulta,self.nombre_vet,self.ciudad_vet,self.nombre,self.apellido,self.documento,self.telefono,self.email,self.password)
            cursor.commit()
            cursor.close()
            
    @staticmethod
    def login(nombre_vet,password):
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
                print (f"Inicio de sesion exitoso, bienvenido {persona}")
                inicio = True
        else:
            print(f"Usuario y/o contraseña incorrecta")
        cursor.close()
        return inicio
        
        
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
    
    # login("Tobias","123456")
    # get_name_veterinaria("Tobias")
    


        

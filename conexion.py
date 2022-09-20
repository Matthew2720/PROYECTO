import pyodbc
direccion_servidor = 'DESKTOP-F9S5AFJ'
nombre_bd = 'FILEPETS'
nombre_usuario = 'sa'
password = '123456'
try:
    db = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                              direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD=' + password)
    print("Conexion exitosa")
    # OK! conexión exitosa
except Exception as e:
    # Atrapar error
    print("Ocurrió un error al conectar a SQL Server: ", e)
    
#_________________________________________________
#CREACION DEL CURSOR 
cursor = db.cursor()
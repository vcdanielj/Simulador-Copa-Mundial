import sqlite3 as sql

#Creamos un objeto que maneje las funciones de la base de datos
class database():
    #Creamos el constructor del objeto, el constructor siempre es __init__ y toma self como primer parametro
    def __init__(self, nombre) -> None:
        #Creamos el cursor
        self._conexion = sql.connect(nombre)
        self._cursor = self._conexion.cursor()
    
    #Funcion para crear las tablas
    def crear_tabla(self, nombre_tabla, datos):
        self._cursor.execute(f"CREATE TABLE IF NOT EXISTS {nombre_tabla}({datos})")
        self._conexion.commit()
    
    #Funcion que inserta un dato en la base de datos, la cantidad de datos son tantos ? como datos a ingresar y los
    #parametros son una lista con las variables, en caso de ser 1 se le pone una coma despues de referenciar la variable
    def insertar(self, tabla, cant_datos, tupla_datos):
        self._cursor.execute(f"INSERT INTO {tabla} VALUES({cant_datos})", tupla_datos)
        self._conexion.commit()
    
    def insertar_algunascolumnas(self, tabla, columnas, cant_datos, tupla_datos):
        self._cursor.execute(f"INSERT INTO {tabla}({columnas}) VALUES({cant_datos})", tupla_datos)
        self._conexion.commit()
    
    #Funcion que cambia un dato de la base de datos
    def actualizar(self, tabla, columna_acambiar, comparacion_busqueda, nuevo_valor, dato_comparacion):
        self._cursor.execute(f"UPDATE {tabla} SET {columna_acambiar} = ? WHERE {comparacion_busqueda} = ?", (nuevo_valor, dato_comparacion))
        self._conexion.commit()
    
    #Funcion que retorna un dato de la base de datos en forma de matriz
    def encontrar_un_valor(self, tabla, columna, columna_coincidencia, dato_busq):
        return self._cursor.execute(f"SELECT {columna} FROM {tabla} WHERE {columna_coincidencia} = ?", (dato_busq, )).fetchall()
    
    #Funcion que retorna un dato tipo cursor perteneciente a una columna ordenada bajo parametros
    def seleccionar_columna_ordenada(self, tabla, columna, orden):
        return self._cursor.execute(f"SELECT {columna} FROM {tabla} ORDER BY {columna} {orden}")
    
    #Retorna una matriz de una columna de la base de datos
    def seleccionar_columna(self, tabla, columna):
        return self._cursor.execute(f"SELECT {columna} FROM {tabla}").fetchall()
    
    #Funcion que retorna una tabla de la base de datos
    def retornar_tabla(self, tabla, culumna_orden, orden):
        aux = self._cursor.execute(f"SELECT * FROM {tabla} ORDER BY {culumna_orden} {orden}")
        return aux
    
    #Funcion que elimina un dato de la base de datos
    def eliminar(self, tabla, columna_busqueda, dato_referencia):
        self._cursor.execute(f"DELETE FROM {tabla} WHERE {columna_busqueda}", dato_referencia)
        self._conexion.commit()
    
    #Se le pasa un objeto tipo cursor para transformarlo en una matriz
    def matriz(self, cursor):
        return cursor.fetchall()
    
    #Funcion para eliminar el objeto
    def cerrar(self):
        self._conexion.close()
    
    #Destructor de la clase, cierra la base de datos
    def __del__(self):
        self._conexion.close()
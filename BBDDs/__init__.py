"""Desde este paquete se gestionan las bases de datos conectadas al programa"""
import sqlite3 as dbapi
import tkinter.messagebox as mbox


def abrir_conexion():
    global conn,c
    conn = dbapi.connect("agenda.db")
    c = conn.cursor()

def crear_tabla():
    c.execute("CREATE TABLE IF NOT EXISTS USUARIOS(NOMBRE TEXT,APELLIDO TEXT,USUARIO TEXT,CLAVE TEXT)")
    conn.commit()

def insertar_datos(datos):
    c.execute("INSERT INTO USUARIOS VALUES(?,?,?,?)",datos)
    conn.commit()
    mbox.showinfo(message="el usuario '"+datos[2]+"' fue registrado exitosamente")


def verificar_datos(usuario,clave):
    c.execute("SELECT CLAVE FROM USUARIOS WHERE USUARIO ='"+usuario+"'")
    for row in c.fetchall():
        if clave == row[0]:
            return True
        else:
            return False

def consultar_usuario(usuario):
    usuarios = []
    c.execute("SELECT USUARIO FROM USUARIOS")
    for row in c.fetchall():
        usuarios.append(row[0])

    if usuario in usuarios:
        return True
    else:
        return False

    
def cerrar_conexion():
    c.close()
    conn.close()

abrir_conexion()
crear_tabla()
if not consultar_usuario('admin'):
    datos = ("luis","garcia","admin","123456")
    insertar_datos(datos)




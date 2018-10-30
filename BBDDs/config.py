import sqlite3 as dbapi

bbdd = dbapi.connect("bbdd.dat")
cursor = bbdd.cursor()
crear_tblusuarios= """CREATE TABLE USUARIOS(NOMBRES VARCHAR NOT NULL,APELLIDOS VARCHAR NOT NULL,USERNAME VARCHAR NOT NULL,PASSWORD VARCHAR NOT NULL)"""
#cursor.execute(crear_tblusuarios)
cursor.execute("INSERT INTO USUARIOS VALUES('','','','')")
cursor.execute("SELECT * FROM USUARIOS")
print(cursor.fetchall())
for item in cursor.fetchall():
    print(item)
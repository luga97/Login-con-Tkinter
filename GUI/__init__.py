"""Dentro de este paquete, esta la configuracion de la interfaz grafica,la cual esta echa con la libreria Tkinter."""
import tkinter as tk
import tkinter.messagebox as mbox
import BBDDs


class Principal(tk.Frame):
    """Esta clase se encarga de crear la ventana principal"""
    def __init__(self,master=None):
        tk.Frame.__init__(self,master=None)
        self.master = master
        self.layout()


    def layout(self):
        self.pack(fill=tk.BOTH, expand=True,ipadx="50px")
        self.master.title("Ventana principal")

        self.membrete = tk.Label(self,height="2",text="Menu Principal",background="#111",foreground="#fff",borderwidth="2")
        self.membrete.pack(fill=tk.BOTH,expand=True)
        
        self.ingresar = tk.Button(self,text="Ya estoy registrado", command=self.cargar_login)
        self.ingresar.pack(fill=tk.X)

        self.registrar = tk.Button(self,text="Quiero registrarme", command=self.cargar_registro)
        self.registrar.pack(fill=tk.X)


        self.botonSalir = tk.Button(self,text="Salir", command=self.salir)
        self.botonSalir.pack(fill=tk.X)

        self.master.mainloop()

    def cargar_login(self):
        self.destroy()
        self.children = Login(self.master)

    def cargar_registro(self):
        self.destroy()
        self.children = Registro(self.master)
    
    def salir(self):
        self.master.destroy()
        quit()


class Login(tk.Frame):    
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.master = master
        self.layout()

    def layout(self):
        self.pack(fill=tk.BOTH,expand=True,ipadx="50px")
        self.master.title("Login")

        #-----DATOS USUARIO----
        self.usuarioLabel = tk.Label(self,text="Ingrese su usuario", bg="#444",fg="#fff")
        self.usuarioLabel.pack(fill=tk.X,expand=True)
        
        self.usuario = tk.StringVar()
        self.usuarioEntry = tk.Entry(self,textvariable=self.usuario,justify=tk.CENTER)
        self.usuarioEntry.pack(fill=tk.X)

        self.claveLabel = tk.Label(self,text="Ingrese su contraseña", bg="#444",fg="#fff")
        self.claveLabel.pack(fill=tk.X,expand=True)

        self.clave = tk.StringVar()
        self.claveEntry = tk.Entry(self,textvariable=self.clave,justify=tk.CENTER)
        self.claveEntry.pack(fill=tk.X)


        #-----BOTONES DEL LOGIN -----
        self.botonIngresar = tk.Button(self,text="Ingresar",command=self.ingresar)
        self.botonIngresar.pack(fill=tk.X)

        self.botonLimpiar = tk.Button(self,text="Limpiar campos",command=self.limpiar)
        self.botonLimpiar.pack(fill=tk.X)

        self.botonRegresar = tk.Button(self,text="Regresar",command=self.regresar)
        self.botonRegresar.pack(fill=tk.X)

    def ingresar(self):
        datos = {
            "usuario": self.usuario.get(),
            "clave": self.clave.get()
        }

        self.datosCompletos = True

        for key in datos:
            if datos[key] == '':
                self.datosCompletos = False
        
        if not self.datosCompletos:
            mbox.showinfo(title="Alerta",message="por favor debe llenar todos los campos")
        else:
            self.usuarioRegistrado = BBDDs.consultar_usuario(datos["usuario"])
            if self.usuarioRegistrado:
                self.datosVerificados = BBDDs.verificar_datos(datos["usuario"],datos["clave"])
                if self.datosVerificados:
                    mbox.showinfo(title="Congratulations!!!",message="Felicidades! Te has logueado exitosamente.")
                    self.master.destroy()
                else:
                    mbox.showinfo(title="Clave Incorrecta", message="Clave erronea")
            else:
                mbox.showinfo(title="Alerta",message="El usuario no se encuentra registrado.")

    def limpiar(self):
        self.usuario.set('')
        self.clave.set('')

    def regresar(self):
        self.destroy()
        self.children = Principal(self.master)

       
class Registro(tk.Frame):    
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.master = master
        self.layout()

    def layout(self):
        self.pack(fill=tk.X)
        self.master.title("Registro de Usuarios")
        self.master.geometry("300x210")
        
        self.nombresLabel = tk.Label(self,text="Ingrese su nombre", bg="#444",fg="#fff")
        self.nombresLabel.pack(fill=tk.X,expand=True)
    
        self.nombres = tk.StringVar()
        self.nombresEntry = tk.Entry(self,textvariable=self.nombres,justify=tk.CENTER)
        self.nombresEntry.pack(fill=tk.X)

        self.apellidosLabel = tk.Label(self,text="Ingrese su apellido", bg="#444",fg="#fff")
        self.apellidosLabel.pack(fill=tk.X,expand=True)

        self.apellidos = tk.StringVar()
        self.apellidosEntry = tk.Entry(self,textvariable=self.apellidos,justify=tk.CENTER)
        self.apellidosEntry.pack(fill=tk.X)

        self.usuarioLabel = tk.Label(self,text="Ingrese su nombre de usuario", bg="#444",fg="#fff")
        self.usuarioLabel.pack(fill=tk.X,expand=True)

        self.usuario = tk.StringVar()
        self.usuarioEntry = tk.Entry(self,textvariable=self.usuario,justify=tk.CENTER)
        self.usuarioEntry.pack(fill=tk.X)

        self.claveLabel = tk.Label(self,text="Ingrese su nombre de clave", bg="#444",fg="#fff")
        self.claveLabel.pack(fill=tk.X,expand=True)


        self.clave = tk.StringVar()
        self.claveEntry = tk.Entry(self,textvariable=self.clave,justify=tk.CENTER)
        self.claveEntry.pack(fill=tk.X)

        self.claveConfirm = tk.StringVar()
        self.claveConfirmEntry = tk.Entry(self,textvariable=self.claveConfirm,justify=tk.CENTER)
        self.claveConfirmEntry.pack(fill=tk.X)

        self.botonRegistrar = tk.Button(self,text="Registrar",command=self.registrar)
        self.botonRegistrar.pack(fill=tk.X)

        self.botonLimpiar = tk.Button(self,text="Limpiar campos",command=self.limpiar)
        self.botonLimpiar.pack(fill=tk.X)

        self.botonRegresar = tk.Button(self,text="Regresar",command=self.regresar)
        self.botonRegresar.pack(fill=tk.X)


    def registrar(self):
        self.claveConfirmada = self.clave.get() == self.claveConfirm.get()
        self.datos = [self.nombres.get(), self.apellidos.get(), self.usuario.get(), self.clave.get()]
        self.datosCompletos = True
        for dato in self.datos:
            if dato == '' :
                self.datosCompletos = False

        if not self.claveConfirmada or not self.datosCompletos:
            if not self.claveConfirmada:
                print("Las contraseña no coincide, por favor verifique.")
            if not self.datosCompletos:
                print("Por favor, llene todos los campos")
        else:
            print("registro de usuario exitoso")
            #TODO ENVIAR AL MENU PRINCIPAL
        
        self.datosUsuario = [self.nombres.get(),self.apellidos.get(),self.usuario.get(),self.clave.get()]
        print(self.claveConfirmada,self.datosCompletos)
    
    def limpiar(self):
        self.nombres.set('')
        self.apellidos.set('')
        self.usuario.set('')
        self.clave.set('')
        self.claveConfirm.set('')

    def regresar(self):
        self.destroy()
        self.children = Principal(self.master)


class Agenda(tk.Frame):
    def __init__(self,master,datos={}):
        tk.Frame.__init__(self,master)
        self.master = master
        self.layout()

    def layout(self):
        self.pack(fill=tk.X)
        self.master.title("Agenda")
        self.master.geometry("400x400")

        self.membrete = tk.Label(self,height="2",text="Lista de Contactos",background="#111",foreground="#fff")
        self.membrete.pack(fill=tk.BOTH)

        self.campoBusqueda = tk.StringVar()
        self.buscarContacto = tk.Entry(self,textvariable=self.campoBusqueda,justify="center")
        self.buscarContacto.pack(fill=tk.X)
        #TODO self.buscarContacto.bind() y Botones
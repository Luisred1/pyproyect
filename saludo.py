
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Created 20-jul -2020
   @Autor: jlred -Jose Luis Rojas C.
"""
import os
import sys
import tkinter as tki
from tkinter import messagebox


class Probaditan(tki.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.ventana_inicio()

    def ventana_inicio(self):
        # global self.ventana_principal
        self.pestas_color = "DarkGrey"
        #self.ventana_principal = tki.Tk()
        # self.ventana_principal.geometry("300x250")
        #self.ventana_principal.title("Login con Tkinter")
        self.e1 = tki.Label(root, text="Escoje tu opcion:",
                            bg="black", fg="white")
        self.e1.place(x=10, y=10)
        self.boton3 = tki.Button(root, bg="green", fg="white")
        self.boton3["text"] = "Acceso"
        self.boton3["command"] = self.login
        self.boton3.place(width=70, x=10, y=50)
        self.boton10 = tki.Button(root, bg="blue", fg="white")
        self.boton10["text"] = "Registrarse"
        self.boton10["command"] = self.registro
        self.boton10.place(width=70, x=10, y=80)
        self.boton = tki.Button(root, bg="yellow", fg="RED")
        self.boton["text"] = "SALIR"
        self.boton["command"] = self.master.destroy
        self.boton.place(height=50, x=10, y=120)
        # self.ventana_principal.mainloop()

    def registro(self):
        # global ventana_registro
        #self.ventana_registro = tki.Toplevel(self.ventana_principal)
        self.ventana_registro = tki.Toplevel(root)
        self.ventana_registro.title("REGISTRO")
        self.ventana_registro.resizable(100, 100)
        self.ventana_registro.geometry("300x250+300+10")
        # global self.nombre_usuario
        # global clave
        # global entrada_clave
        self.boton_salir_registro = tki.Button(
            self.ventana_registro, bg="navy", fg="white")
        self.boton_salir_registro["text"] = "SALIR"
        self.boton_salir_registro["command"] = self.ventana_registro.destroy
        self.boton_salir_registro.place(x=20, y=220)
        self.nombre_usuario = tki.StringVar(self)
        self.clave = tki.StringVar(self)
        self.e4 = tki.Label(self.ventana_registro,
                            text="Introduce tus datos:", bg="black", fg="green")
        self.e4.place(x=10, y=20)
        self.etiqueta_nombre = tki.Label(
            self.ventana_registro, text="Nombre de usuario * ")
        self.etiqueta_nombre.place(x=10, y=60)
        self.entrada_nombre = tki.Entry(
            self.ventana_registro, textvariable=self.nombre_usuario)
        self.entrada_nombre.place(x=10, y=100)
        self.etiqueta_clave = tki.Label(
            self.ventana_registro, text="Contraseña * ")
        self.etiqueta_clave.place(x=10, y=140)
        self.entrada_clave = tki.Entry(
            self.ventana_registro, textvariable=self.clave, show="*")
        self.entrada_clave.place(x=10, y=180)
        self.e5 = tki.Label(self.ventana_registro, text="")
        self.e5.place(x=50, y=50)
        self.boton11 = tki.Button(self.ventana_registro)
        self.boton11["text"] = "REGISTRARSE"
        self.boton11["command"] = self.registro_usuario
        self.boton11.place(x=10, y=250)

    def registro_usuario(self):
        self.usuario_info = self.nombre_usuario.get()
        self.clave_info = self.clave.get()

        self.file = open(self.usuario_info, "w")
        self.file.write(self.usuario_info + "\n")
        self.file.write(self.clave_info)
        self.file.close()

        self.entrada_nombre.delete(0)
        self.entrada_clave.delete(0)
        self.e6 = tki.Label(self.ventana_registro,
                            text="Registro realizado con exito")
        self.e6.pack()

    def login(self):
        # global ventana_login
        #self.ventana_login = tki.Toplevel(self.ventana_principal)
        self.ventana_login = tki.Toplevel(root)
        self.ventana_login.title("ACCESO A LA CUENTA")
        self.ventana_login.geometry("300x250+600+10")

        self.boton_salir_login = tki.Button(
            self.ventana_login, bg="navy", fg="white")
        self.boton_salir_login["text"] = "SALIR"
        self.boton_salir_login["command"] = self.ventana_login.destroy
        self.boton_salir_login.place(x=20, y=220)
        self.e7 = tki.Label(self.ventana_login,
                            text="Introduce User y Contraseña")
        self.e7.place(x=10, y=10)
        # global self.verica_usuario
        # global self.verific_clave
        self.verifica_usuario = tki.StringVar(self)
        self.verifica_clave = tki.StringVar(self)
        # global self.entrada_login_usuario
        # global self.entrada_login_clave
        self.e8 = tki.Label(self.ventana_login, text="NOMBRE DE USUARIO *")
        self.e8.place(x=10, y=40)
        self.entrada_login_usuario = tki.Entry(
            self.ventana_login, textvariable=self.verifica_usuario)
        self.entrada_login_usuario.place(x=10, y=70)
        self.e9 = tki.Label(self.ventana_login, text="")
        self.e9.place(x=10, y=100)
        self.e8 = tki.Label(self.ventana_login, text="CONTRASEÑA *")
        self.e8.place(x=10, y=100)
        self.entrada_login_clave = tki.Entry(
            self.ventana_login, textvariable=self.verifica_clave, show="*")
        self.entrada_login_clave.place(x=10, y=140)
        self.e10 = tki.Label(self.ventana_login, text="")
        self.e10.place(x=10, y=180)
        self.buton13 = tki.Button(self.ventana_login)
        self.buton13["text"] = "ACCEDER"
        self.buton13["command"] = self.verifica_login
        self.buton13.place(width=70, x=100, y=170)

    def verifica_login(self):
        self.usuario1 = self.verifica_usuario.get()
        self.clave1 = self.verifica_clave.get()
        self.entrada_login_usuario.delete(0)
        self.entrada_login_clave.delete(0)
        self.lista_archivos = os.listdir()
        if self.usuario1 in self.lista_archivos:
            self.archivo1 = open(self.usuario1, "r")
            self.verifica = self.archivo1.read().splitlines()
            if self.clave1 in self.verifica:
                self.exito_login()
            else:
                self.no_clave()
        else:
            self.no_usuario()

    def no_usuario(self):
        # global self.ventana_no_usuario
        self.ventana_no_usuario = tki.Toplevel(self.ventana_login)
        self.ventana_no_usuario.title("ERROR")
        self.ventana_no_usuario.geometry("150x100")
        self.e11 = tki.Label(self.ventana_no_usuario,
                             text="usuario no encontrado")
        self.e11.pack()
        self.buton14 = tki.Button(self.ventana_no_usuario)
        self.buton14["text"] = "OK"
        self.buton14["command"] = self.borrar_no_usuario
        self.buton14.pack()

    def exito_login(self):
        #global ventana_exito
        self.ventana_exito = tki.Toplevel(self.ventana_login)
        self.ventana_exito.title("EXITO")
        self.ventana_exito.geometry("2000x100+10+400")
        self.e12 = tki.Label(
            self.ventana_exito, text="LOGIN FINALIZADO CON EXITO", bg="blue", fg="white")
        self.e12.pack()
        self.buton15 = tki.Button(self.ventana_exito)
        self.buton15["text"] = "SALIR"
        self.buton15["command"] = self.borrar_exito_login
        self.buton15.pack()

        self.boton_inicio = tki.Button(self.ventana_exito)
        self.boton_inicio["text"] = "ACCESO CONCEDIDO\n click"
        self.boton_inicio["command"] = self.create_widgets
        self.boton_inicio.pack()

    def no_clave(self):
        # global self.ventana_no_clave
        self.ventana_no_clave = tki.Toplevel(self.ventana_login)
        self.ventana_no_clave.title("ERROR")
        self.ventana_no_clave.geometry("150x100")
        self.e13 = tki.Button(self.ventana_no_clave)
        self.e13["text"] = "CONTRASEÑA INCORRECTA"
        self.e13["command"] = self.borrar_no_clave
        self.e13.pack()

    def borrar_exito_login(self):
        self.ventana_exito.destroy()

    def borrar_no_clave(self):
        self.ventana_no_clave.destroy()

    def borrar_no_usuario(self):
        self.ventana_no_usuario.destroy()

    def create_widgets(self):
        self.hi_there = tki.Button(self)
        self.hi_there["text"] = "Hola bienvenidos\n(click)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")
        self.quit = tki.Button(self, text="QUIT", fg="red",
                               command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("Hi there, everyone")


root = tki.Tk()
myapp = Probaditan(master=root)
myapp.master.title("Mi programa empieza aqui, Ventana 1")
myapp.master.geometry("450x170+10+10")
# myapp.master.maxsize(1000x400+10+10)
# myapp.master.resizable("50x50")
myapp.master.configure(background="black")


myapp.mainloop()

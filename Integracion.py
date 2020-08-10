#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
    @Autor: Jose Luis Rojas C.
    Date:  30-jul-2020

"""
import os
import sys
import tkinter as tki
from tkinter import messagebox


class Integral(tki.Frame):
    def __init__(self,  master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.access()
    pass

    def access(self):
        self.e1 = tki.Label(root, text="Welcome to Integral",
                            bg="navy", fg="white")
        self.e1.pack()
        self.quit()

        self.b3 = tki.Button(root, bg="green", fg="white")
        self.b3["text"] = "ACCESS"
        self.b3["command"] = self.login
        self.b3.place(width=70, x=10, y=50)

        self.b4 = tki.Button(root, bg="blue", fg="white")
        self.b4["text"] = "REGISTER"
        self.b4["command"] = self.registro
        self.b4.place(width=70, x=10, y=80)

    def quit(self):
        self.b1 = tki.Button(root, bg="black", fg="white")
        self.b1["text"] = "QUIT"
        self.b1["command"] = self.master.destroy
        self.b1.place(x=50, y=370)

    def exit(self):
        self.b2 = tki.Button(self.v_r, bg="black", fg="white")
        self.b2["text"] = "EXIT"
        self.b2["command"] = self.v_r.destroy
        self.b2.place(x=50, y=340)

    def registro(self):
        self.v_r = tki.Toplevel(root)
        self.v_r.title("REGISTER")
        self.v_r.resizable(100, 100)
        self.v_r.geometry("300x400+800+40")
        self.v_r.configure(background="green")

        self.exit()

        self.user = tki.StringVar(self)
        self.clave = tki.StringVar(self)

        self.e2 = tki.Label(self.v_r,
                            text="Introduce tus datos:", bg="black", fg="white")
        self.e2.place(x=10, y=20)

        self.e3 = tki.Label(self.v_r, text="User Name * ")
        self.e3.place(x=10, y=60)
        self.e_name = tki.Entry(self.v_r, textvariable=self.user)
        self.e_name.place(x=10, y=100)

        self.e4 = tki.Label(
            self.v_r, text="Contraseña * ")
        self.e4.place(x=10, y=140)

        self.e_clave = tki.Entry(
            self.v_r, textvariable=self.clave, show="*")
        self.e_clave.place(x=10, y=180)

        #self.e5 = tki.Label(self.v_r, text="")
        #self.e5.place(x=50, y=50)

        self.b5 = tki.Button(self.v_r)
        self.b5["text"] = "REGISTRARSE"
        self.b5["command"] = self.registro_usuario
        self.b5.place(x=10, y=250)

    def registro_usuario(self):
        self.usuario_info = self.user.get()
        self.clave_info = self.clave.get()

        self.file = open(self.usuario_info, "w")
        self.file.write(self.usuario_info + "\n")
        self.file.write(self.clave_info)
        self.file.close()

        self.e_name.delete(0)
        self.e_clave.delete(0)
        self.e6 = tki.Label(self.v_r, text="Registro realizado con exito")
        self.e6.pack()

    def login(self):
        self.v_l = tki.Toplevel(root)
        self.v_l.title("ACCESO A LA CUENTA")
        self.v_l.geometry("300x250+900+40")
        self.v_l.configure(background="black")

        self.b6 = tki.Button(
            self.v_l, bg="black", fg="white")
        self.b6["text"] = "SALIR"
        self.b6["command"] = self.v_l.destroy
        self.b6.place(x=20, y=220)

        self.e7 = tki.Label(
            self.v_l, text="Introduce User y Contraseña", bg="navy", fg="white")
        self.e7.place(x=10, y=10)

        self.v_user = tki.StringVar(self)
        self.v_clave = tki.StringVar(self)

        self.e8 = tki.Label(
            self.v_l, text="NOMBRE DE USUARIO *", bg="gray", fg="white")
        self.e8.place(x=50, y=40)

        self.entrada_login_usuario = tki.Entry(
            self.v_l, textvariable=self.v_user)
        self.entrada_login_usuario.place(x=50, y=70)

        #self.e9 = tki.Label(self.v_l, text="")
        #self.e9.place(x=10, y=100)

        self.e10 = tki.Label(self.v_l, text="CONTRASEÑA *",
                             bg="gray", fg="white")
        self.e10.place(x=50, y=110)

        self.entrada_login_clave = tki.Entry(
            self.v_l, textvariable=self.v_clave, show="*")
        self.entrada_login_clave.place(x=50, y=140)
# agregue saludos en text
        #self.e11 = tki.Label(self.v_l, text="saludos")
        #self.e11.place(x=10, y=180)

        self.b7 = tki.Button(self.v_l, bg="black", fg="white")
        self.b7["text"] = "ACCEDER"
        self.b7["command"] = self.verifica_login
        self.b7.place(width=70, x=100, y=170)

    def verifica_login(self):
        self.usuario1 = self.v_user.get()
        self.clave1 = self.v_clave.get()
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
        self.v_no_user = tki.Toplevel(self.v_l)
        self.v_no_user.title("ERROR")
        self.v_no_user.geometry("150x100")
        self.e12 = tki.Label(self.v_no_user, text="usuario no encontrado")
        self.e12.pack()

        self.b8 = tki.Button(self.v_no_user)
        self.b8["text"] = "OK"
        self.b8["command"] = self.borrar_no_usuario
        self.b8.pack()

    def exito_login(self):
        self.v_e = tki.Toplevel(self.v_l)
        self.v_e.title("EXITO")
        self.v_e.geometry("300x100+20+200")
        self.e13 = tki.Label(
            self.v_e, text="LOGIN FINALIZADO CON EXITO", bg="black", fg="white")
        self.e13.pack()
        self.b9 = tki.Button(self.v_e)
        self.b9["text"] = "SALIR"
        self.b9["command"] = self.borrar_exito_login
        self.b9.pack()

        self.b10 = tki.Button(self.v_e)
        self.b10["text"] = "ACCESO CONCEDIDO\n click"
        self.b10["command"] = self.create_widgets
        self.b10.pack()

    def no_clave(self):
        self.v_no_clave = tki.Toplevel(self.v_l)
        self.v_no_clave.title("ERROR")
        self.v_no_clave.geometry("150x100")
        self.b11 = tki.Button(self.v_no_clave)
        self.b11["text"] = "CONTRASEÑA INCORRECTA"
        self.b11["command"] = self.borrar_no_clave
        self.b11.pack()

    def borrar_exito_login(self):
        self.v_e.destroy()

    def borrar_no_clave(self):
        self.v_no_clave.destroy()

    def borrar_no_usuario(self):
        self.v_no_user.destroy()

    def create_widgets(self):
        self.hi_there = tki.Button(self)
        self.hi_there["text"] = "Hola bienvenidos\n(click)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.b12 = tki.Button(root, bg="black", fg="white")
        self.b12["text"] = "[] MENU 1 []"
        self.b12["command"] = self.inicio
        self.b12.place(width=70, x=10, y=110)

        self.b16 = tki.Button(root, bg="black", fg="white")
        self.b16["text"] = "[] MENU 2 []"
        self.b16["command"] = self.abrir
        self.b16.place(width=70, x=90, y=110)

    def say_hi(self):
        print("Hi there, everyone")

    def inicio(self):
        self.raiz = tki.Tk()
        self.raiz.geometry('700x400')
        self.raiz.configure(bg='navy')
        self.raiz.resizable(width=False, height=False)
        self.raiz.title('MENU PRINCIPAL')
        self.labeltop = tki.Label(
            self.raiz, text=" Programa para el desarrollo de proyectos \n Elige la opcion deseada\n MENU ", bg='black', fg="white")
        self.labeltop.place(x=100, y=30)
        # LLAMADA A TABLAS DE MULTIPLICAR
        self.b14 = tki.Button(self.raiz,  bg="black", fg="gray")
        self.b14["text"] = 'Tablas'
        self.b14["command"] = self.win2
        self.b14.place(x=100, y=100)
        self.e14 = tki.Label(
            self.raiz, text=" Calculo de tablas matematicas rango ( 1 - 10 )", bg='black', fg="white")
        self.e14.place(x=250, y=100)
        # LLAMADA A ORDEN ASCENDENTE
        self.b15 = tki.Button(self.raiz, bg="black", fg="gray")
        self.b15["text"] = "ASCENDENTE"
        self.b15["command"] = self.ascendente
        self.b15.place(x=100, y=140)
        self.e15 = tki.Label(
            self.raiz, text=" Lectura de datos y ordenarlos de forma ascendente ", bg='black', fg='white')
        self.e15.place(x=250, y=140)

        self.watch5 = tki.Button(
            self.raiz, text='SALIR', bg="black", fg="gray", command=self.raiz.destroy)

        self.watch5.place(x=100, y=300)
        self.raiz.mainloop()

    def win2(self):
        self.tabla = tki.Toplevel(self.raiz)
        self.tabla.configure(bg='black')
        self.tabla.title('TABLA')
        self.tabla.geometry('600x600')
        self.e16 = tki.Label(
            self.tabla, text="ELIGE LA TABLA A MULTIPLICAR( 1 al 10 )", bg='azure4', fg='navy')
        self.e16.grid(column=0, row=1)
        # self.labeltop.grid(column=0, row=0)
        self.watch = tki.Button(self.tabla, text='Tabla', command=self.leer)
        self.watch.place(x=350, y=40)
        self.watch1 = tki.Button(
            self.tabla, text='calculo', command=self.calculo)
        self.watch1.grid(column=1, row=3)

        self.watch3 = tki.Button(
            self.tabla, text='biblioteca', command=self.biblioteca)
        self.watch3.grid(column=1, row=4)

        self.qinfo = tki.Text(self.tabla, width=40, height=10, bg='royal blue')
        self.qinfo.grid(column=0, row=3)

        self.finfo = tki.Text(self.tabla, width=40, height=10, bg='royal blue')
        self.finfo.grid(column=0, row=4)

        self.tinfo = tki.Text(self.tabla, width=40,
                              height=10, bg='slate blue1')
        self.tinfo.grid(column=0, row=5)

        self.binfo = tki.Button(self.tabla, text='Info', command=self.verinfo)
        self.binfo.grid(column=1, row=5)

        self.bsalir = tki.Button(
            self.tabla, text='Salir', command=self.tabla.destroy)
        self.bsalir.grid(column=2, row=5)
        self.raiz.mainloop()

    def leer(self):
        self.combo = tki.Spinbox(
            self.tabla, values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.combo.place(x=420, y=40)
        self.value = self.combo.get()

    def leer1(self):
        self.combo1 = tki.Spinbox(
            self.tabla, values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.combo1.place(x=420, y=40)
        self.value = self.combo1.get()

    def calculo(self):
        self.producto = {}
        self.mult1 = 1
        while self.mult1 <= 10:
            self.resultado = self.mult1 * int(self.combo.get())
            self.producto[self.mult1] = (self.resultado)
            self.mult1 += 1
        return self.producto

    def calculo1(self):
        self.producto1 = {}
        self.mult2 = 1
        while self.mult2 <= 10:
            self.resultado1 = self.mult2 * int(self.combo1.get())
            self.producto1[self.mult2] = (self.resultado1)
            self.mult2 += 1
        return self.producto1

    def biblioteca1(self):
        self.xinfo.delete("1.0")

        datos1 = str(self.producto1[1])
        datos2 = str(self.producto1[2])
        datos3 = str(self.producto1[3])
        datos4 = str(self.producto1[4])
        datos5 = str(self.producto1[5])
        datos6 = str(self.producto1[6])
        datos7 = str(self.producto1[7])
        datos8 = str(self.producto1[8])
        datos9 = str(self.producto1[9])
        datos10 = str(self.producto1[10])

        texto1_bib1 = " x  1 = " + datos1 + "\n"
        texto1_bib1 += " x  2 = " + datos2 + "\n"
        texto1_bib1 += " x  3 = " + datos3 + "\n"
        texto1_bib1 += " x  4 = " + datos4 + "\n"
        texto1_bib1 += " x  5 = " + datos5 + "\n"
        texto1_bib1 += " x  6 = " + datos6 + "\n"
        texto1_bib1 += " x  7 = " + datos7 + "\n"
        texto1_bib1 += " x  8 = " + datos8 + "\n"
        texto1_bib1 += " x  9 = " + datos9 + "\n"
        texto1_bib1 += " x  10= " + datos10 + "\n"

        self.xinfo.insert("1.0", texto1_bib1)

    def biblioteca(self):
        self.qinfo.delete("1.0")

        dato1 = str(self.producto[1])
        dato2 = str(self.producto[2])
        dato3 = str(self.producto[3])
        dato4 = str(self.producto[4])
        dato5 = str(self.producto[5])
        dato6 = str(self.producto[6])
        dato7 = str(self.producto[7])
        dato8 = str(self.producto[8])
        dato9 = str(self.producto[9])
        dato10 = str(self.producto[10])

        texto_bib1 = " x  1 = " + dato1 + "\n"
        texto_bib1 += " x  2 = " + dato2 + "\n"
        texto_bib1 += " x  3 = " + dato3 + "\n"
        texto_bib1 += " x  4 = " + dato4 + "\n"
        texto_bib1 += " x  5 = " + dato5 + "\n"
        texto_bib1 += " x  6 = " + dato6 + "\n"
        texto_bib1 += " x  7 = " + dato7 + "\n"
        texto_bib1 += " x  8 = " + dato8 + "\n"
        texto_bib1 += " x  9 = " + dato9 + "\n"
        texto_bib1 += " x  10= " + dato10 + "\n"

        self.qinfo.insert("1.0", texto_bib1)

    def verinfo(self):
        self.finfo.delete("1.0")
        self.tinfo.delete("1.0")
        # Obtiene información de la ventana 'self.raiz':
        info0 = self.combo.get()
        infor = self.value
        # info1 = self.raiz.winfo_class()
        info2 = self.raiz.winfo_geometry()
        info3 = str(self.raiz.winfo_width())
        info4 = str(self.raiz.winfo_height())
        info5 = str(self.raiz.winfo_rootx())
        info6 = str(self.raiz.winfo_rooty())
        info7 = str(self.raiz.winfo_id())
        info8 = self.raiz.winfo_name()
        info9 = self.raiz.winfo_manager()
        # Construye una cadena de texto con toda la
        # información obtenida:
        texto_info = "Solución y posición: " + info2 + "\n"
        texto_info += "Anchura ventana: " + info3 + "\n"
        texto_info += "Altura ventana: " + info4 + "\n"
        texto_info += "Pos. Ventana X: " + info5 + "\n"
        texto_info += "Pos. Ventana Y: " + info6 + "\n"
        texto_info += "Id. de 'raiz': " + info7 + "\n"
        texto_info += "Nombre objeto: " + info8 + "\n"
        texto_info += "Gestor ventanas: " + info9 + "\n"
        texto_info1 = "Elegiste la tabla del  : " + info0 + "\n"
        texto_info1 += "recalculo : " + infor + "\n"
        # Inserta la información en la caja de texto:
        self.tinfo.insert("1.0", texto_info)
        self.finfo.insert("1.0", texto_info1)

    def ascendente(self):
        self.ventana_ascendente = tki.Toplevel(self.raiz, bg="black")
        self.ventana_ascendente.title("OPERACIONES CON DATOS ASCENDENTES")
        self.ventana_ascendente.geometry("400x400+120+120")
        self.ventana_ascendente.resizable(100, 100)
        self.e3 = tki.Label(self.ventana_ascendente, text="BIENVENIDO A REALIZAR CALCULOS\nCON OPERACIONES ASCENDENTES",
                            bg="gray", fg="white", font=("Arial Bold", 10))
        self.e3.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tki.X)
        self.boton_salir_datos_ascendentes = tki.Button(
            self.ventana_ascendente, bg="black", fg="gray")
        self.boton_salir_datos_ascendentes["text"] = "SALIR"
        self.boton_salir_datos_ascendentes["command"] = self.ventana_ascendente.destroy
        self.boton_salir_datos_ascendentes.place(x=200, y=370)

        self.boton_leer_datos_asc = tki.Button(
            self.ventana_ascendente, bg="black", fg="gray")
        self.boton_leer_datos_asc["text"] = "LEER DATOS"
        self.boton_leer_datos_asc["command"] = self.leer_datos_ascendente
        self.boton_leer_datos_asc.place(x=50, y=70)

        self.boton_proceso_asc = tki.Button(
            self.ventana_ascendente, bg="black", fg="gray")
        self.boton_proceso_asc["text"] = "LEER  ASCENDENTE"
        self.boton_proceso_asc["command"] = self.proceso_asc
        self.boton_proceso_asc.place(x=50, y=100)

        self.boton_proceso_desc = tki.Button(
            self.ventana_ascendente, bg="black", fg="gray")
        self.boton_proceso_desc["text"] = "LEER  DESCENDENTE"
        self.boton_proceso_desc["command"] = self.proceso_des
        self.boton_proceso_desc.place(x=50, y=130)

        self.textoinfo1 = tki.Text(
            self.ventana_ascendente, width=40, height=10, bg="black", fg="white")
        self.textoinfo1.place(x=5, y=160)

        self.boton_presenta_Datos = tki.Button(
            self.ventana_ascendente, bg="black", fg="white")
        self.boton_presenta_Datos["text"] = "LEER  DATOS"
        self.boton_presenta_Datos["command"] = self.presenta_Datos
        self.boton_presenta_Datos.place(x=50, y=330)

    def leer_datos_ascendente(self):
        self.ventana_leer_datos_asc = tki.Toplevel(
            self.ventana_ascendente, bg="black")
        self.ventana_leer_datos_asc.title("Lectura de Datos")
        self.ventana_leer_datos_asc.geometry("400x320+140+140")
        self.ventana_leer_datos_asc.resizable(width=False, height=False)

        self.boton_salir_leer_datos_asc = tki.Button(
            self.ventana_leer_datos_asc, bg="black", fg="gray")
        self.boton_salir_leer_datos_asc["text"] = "SALIR"
        self.boton_salir_leer_datos_asc["command"] = self.ventana_leer_datos_asc.destroy
        self.boton_salir_leer_datos_asc.place(x=300, y=290)

        self.lista1 = []
        # self.lista2 = []
        self.control = 0
        self.valor1 = 0
        self.etiqueta_leer_dato = tki.Label(
            self.ventana_leer_datos_asc, text="INTRODUCE DIEZ NUMEROS:", bg="navy", fg="white")
        self.etiqueta_leer_dato.pack(padx=5, pady=5, ipadx=5, ipady=5)
        self.textoinfo = tki.Text(
            self.ventana_leer_datos_asc, width=30, height=15, bg="black", fg="white")
        self.textoinfo.place(x=5, y=90)
        for self.control in range(10):
            self.valor1 = int(input("Dame el valor:"))
            self.control += 1
            textobiblioteca = " Valor  : " + str(self.valor1) + "\n"
            self.textoinfo.insert("1.0", textobiblioteca)
            self.lista1.append(self.valor1)
            # self.lista2.append(self.valor1)
        print(self.lista1)
        # print(self.lista2)
        return self.lista1

    def proceso_asc(self):
        self.lista1.sort()
        print(self.lista1)
        return self.lista1

    def proceso_des(self):
        self.lista1.sort(reverse=True)
        print(self.lista1)
        return self.lista1

    def presenta_Datos(self):
        self.textoinfo1.delete("2.0")
        self.control1 = 0
        "\n"
        for self.control1 in range(10):
            textobiblioteca1 = str(self.lista1[self.control1]) + " "
            self.textoinfo1.insert("2.0", textobiblioteca1)
            # print(textobiblioteca1)
            self.control += 1

    def abrir(self):
        self.marco = tki.Frame(
            root, borderwidth=2, relief="raised")
        self.e20 = tki.Label(
            text="BIENVENIDO AL MENU MATEMATICO", bg="gray", fg="white", font=("Arial Bold", 20))
        self.e20.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tki.X)
        self.win = tki.Button(root)
        self.win.configure(background='blue')
        self.win["text"] = "Para abrir una nueva ventana\nCLICK"
        self.win["command"] = self.nueva
        self.win.place(x=10, y=70)
        # self.win.pack(side=tki.BOTTOM)
        self.boton2 = tki.Button(root, bg="yellow", fg="red")
        self.boton2["text"] = "EXIT"
        self.boton2["command"] = self.cerrar
        self.boton2.place(width=70, x=400, y=70)
        # self.boton2.pack(side=tki.BOTTOM)
        self.boton4 = tki.Button(root, bg="black", fg="green")
        self.boton4["text"] = "MENU"
        self.boton4["command"] = self.menu
        self.boton4.place(width=50, x=200, y=70)

    def nueva(self):
        self.ventana = tki.Toplevel(root)
        self.ventana.title("Ventana X")
        self.ventana.resizable(100, 100)
        self.ventana.geometry('400x100+920+120')
        self.ventana.configure(background="green")
        self.boton = tki.Button(self.ventana, bg="blue", fg="white")
        self.boton["text"] = "SALIR"
        self.boton["command"] = self.ventana.destroy
        self.boton.place(height=50, x=50, y=50)

    def menu(self):
        self.ventana_menu = tki.Toplevel(root)
        self.ventana_menu.title("MENU")
        self.ventana_menu.resizable(100, 100)
        self.ventana_menu.geometry('210x300+25+250')
        self.ventana_menu.configure(background="black")
        self.etiqueta_menu = tki.Label(
            self.ventana_menu, text="ELIGE LA OPCION DESEADA\npresiona el boton corrspondiente", bg="navy", fg="white")
        # self.etiqueta_menu.place(x=1, y=1)
        self.etiqueta_menu.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tki.X)
        self.boton = tki.Button(self.ventana_menu, bg="navy", fg="white")
        self.boton["text"] = "SALIR"
        self.boton["command"] = self.ventana_menu.destroy
        self.boton.place(height=50, x=20, y=260)
        # opcion TM
        self.boton10 = tki.Button(self.ventana_menu, bg="navy", fg="white")
        self.boton10["text"] = "TABLA DE MULTIPLICACION"
        self.boton10["command"] = self.tabla_Multiplicacion
        self.boton10.place(width=200, x=10, y=60)
        # OPCION SUMA
        self.boton11 = tki.Button(self.ventana_menu, bg="navy", fg="white")
        self.boton11["text"] = "SUMA"
        self.boton11["command"] = self.suma
        self.boton11.place(width=200, x=10, y=90)
        # OPCION RESTA
        self.boton12 = tki.Button(self.ventana_menu, bg="navy", fg="white")
        self.boton12["text"] = "RESTA"
        self.boton12["command"] = self.resta
        self.boton12.place(width=200, x=10, y=120)
        # OPCION MULTIPLICACION
        self.boton13 = tki.Button(self.ventana_menu, bg="navy", fg="white")
        self.boton13["text"] = "MULTIPLICACION"
        self.boton13["command"] = self.multiplicacion
        self.boton13.place(width=200, x=10, y=150)
        # OPCION DIVISION
        self.boton14 = tki.Button(self.ventana_menu, bg="navy", fg="white")
        self.boton14["text"] = "DIVISION"
        self.boton14["command"] = self.division
        self.boton14.place(width=200, x=10, y=180)

    def cerrar(self):
        self.bquit = tki.Button(root, text="QUIT", bg="red", fg="white",
                                command=self.master.destroy)
        self.bquit.place(width=70, x=400, y=100)

    def tabla_Multiplicacion(self):
        # window Menu
        self.opcion = tki.Toplevel(self.ventana_menu)
        self.opcion.title("TABLA DE MULTIPLICACION")
        self.opcion.resizable(100, 100)
        self.opcion.geometry('210x380+245+250')
        self.opcion.configure(background="black")
        # exit from window
        self.boton5 = tki.Button(self.opcion, bg="navy", fg="white")
        self.boton5["text"] = "SALIR"
        self.boton5["command"] = self.opcion.destroy
        self.boton5.place(width=50, x=50, y=330)
        # Etiqueta de Intrucciones
        self.e4 = tki.Label(self.opcion,
                            text="TABLA DE MULTIPLICACION", bg="purple", fg="white")
        self.e4.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tki.X)

        self.etiqueta_TM = tki.Label(
            self.opcion, text="Elige del (1 al 10):", bg="navy", fg="white")
        self.etiqueta_TM.place(x=50, y=40)

        # Realizar la seleccion mediante un if ?  ¿Cual es?

        self.leerTM()
        self.boton7 = tki.Button(self.opcion, bg="purple", fg="white")
        self.boton7["text"] = "CALCULO"
        self.boton7["command"] = self.calculo1
        self.boton7.place(width=100, x=10, y=100)

        self.boton8 = tki.Button(self.opcion, bg="purple", fg="white")
        self.boton8["text"] = "BIBLIOTECA"
        self.boton8["command"] = self.biblioteca1
        self.boton8.place(width=100, x=10, y=130)

        self.xinfo = tki.Text(self.opcion, width=40,
                              height=10, bg='royal blue')
        self.xinfo.place(x=5, y=160)
        # Obtener informacion de la ventana de tablas de multiplicacion

    def leerTM(self):
        self.combo1 = tki.Spinbox(
            self.opcion, values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.combo1.place(x=20, y=70)
        self.value = self.combo1.get()

    def suma(self):
        self.opcion_suma = tki.Toplevel(self)
        self.opcion_suma.title("SUMA")
        self.opcion_suma.resizable(100, 100)
        self.opcion_suma.geometry('210x300+465+250')
        self.opcion_suma.configure(background="black")
        self.var1 = tki.StringVar(self)
        self.boton5_S = tki.Button(self.opcion_suma, bg="navy", fg="white")
        self.boton5_S["text"] = "SALIR"
        self.boton5_S["command"] = self.opcion_suma.destroy
        self.boton5_S.place(width=50, x=160, y=270)
        self.e4 = tki.Label(self.opcion_suma,
                            text="SUMA\nINTRODUCE LOS VALORES A SUMAR", bg="green", fg="white")
        self.e4.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tki.X)
        self.suma_leer_datos()
        self.boton_suma = tki.Button(self.opcion_suma, bg="green", fg="white")
        self.boton_suma["text"] = "RESULTADO"
        self.boton_suma["command"] = self.suma_resultado
        self.boton_suma.place(x=10, y=270)
        self.etiqueta_res = tki.Label(
            self.opcion_suma, textvariable=self.var1, bg="turquoise", fg="blue")
        self.etiqueta_res.pack(padx=5, pady=5, ipadx=5, ipady=5)

    def suma_leer_datos(self):
        self.etiqueta_sumaA = tki.Label(
            self.opcion_suma, text="NUMERO A:", bg="navy", fg="white")
        self.etiqueta_sumaA.pack(padx=5, pady=5, ipadx=5, ipady=5)

        self.valorA = tki.Entry(self.opcion_suma)
        self.valorA.pack(padx=5, pady=5, ipadx=5, ipady=5)

        self.etiqueta_sumaB = tki.Label(
            self.opcion_suma, text="NUMERO B:", bg="navy", fg="white")
        self.etiqueta_sumaB.pack(padx=5, pady=5, ipadx=5, ipady=5)

        self.valorB = tki.Entry(self.opcion_suma)
        self.valorB.pack(padx=5, pady=5, ipadx=5, ipady=5)

    def suma_resultado(self):

        self.sumaAB = float(self.valorA.get()) + float(self.valorB.get())
        return self.var1.set(self.sumaAB)

    def resta(self):
        self.opcion_resta = tki.Toplevel(self)
        self.opcion_resta.title("RESTA")
        self.opcion_resta.resizable(100, 100)
        self.opcion_resta.geometry('210x300+685+250')
        self.opcion_resta.configure(background="black")
        self.var2 = tki.StringVar(self)
        # exit from window
        self.boton5_R = tki.Button(self.opcion_resta, bg="navy", fg="white")
        self.boton5_R["text"] = "SALIR"
        self.boton5_R["command"] = self.opcion_resta.destroy
        self.boton5_R.place(width=50, x=150, y=270)
        # Etiqueta de Intrucciones
        self.etiqueta1_resta = tki.Label(self.opcion_resta,
                                         text="RESTA\n sigue las instrucciones\n INTRODUCE LOS VALORES A RESTAR", bg="green", fg="white")
        self.etiqueta1_resta.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tki.X)

        self.resta_leer_datos()

        self.boton_resta = tki.Button(
            self.opcion_resta, bg="green", fg="white")
        self.boton_resta["text"] = "RESULTADO"
        self.boton_resta["command"] = self.resta_resultado
        self.boton_resta.place(x=10, y=270)

        self.etiqueta_res = tki.Label(
            self.opcion_resta, textvariable=self.var2, bg="turquoise", fg="blue")
        self.etiqueta_res.pack(padx=5, pady=5, ipadx=5, ipady=5)

    def resta_leer_datos(self):
        self.etiqueta_restaA = tki.Label(
            self.opcion_resta, text="NUMERO SUMANDO:", bg="navy", fg="white")
        self.etiqueta_restaA.pack(padx=5, pady=5, ipadx=5, ipady=5)

        self.valorD = tki.Entry(self.opcion_resta)
        self.valorD.pack(padx=5, pady=5, ipadx=5, ipady=5)

        self.etiqueta_restaB = tki.Label(
            self.opcion_resta, text="NUMERO RESTANDO:", bg="navy", fg="white")
        self.etiqueta_restaB.pack(padx=5, pady=5, ipadx=5, ipady=5)

        self.valorC = tki.Entry(self.opcion_resta)
        self.valorC.pack(padx=5, pady=5, ipadx=5, ipady=5)

    def resta_resultado(self):

        self.restaDC = float(self.valorD.get()) - float(self.valorC.get())
        return self.var2.set(self.restaDC)
# multiplicacio opcion

    def multiplicacion(self):
        self.opcion_multi = tki.Toplevel(self)
        self.opcion_multi.title("MULTIPLICACION")
        self.opcion_multi.resizable(100, 100)
        self.opcion_multi.geometry('210x300+905+250')
        self.opcion_multi.configure(background="black")
        # Variable que controla el valor  resultado de multiplicacion
        self.var3 = tki.StringVar(self)
        # exit from window
        self.boton5_M = tki.Button(self.opcion_multi, bg="navy", fg="white")
        self.boton5_M["text"] = "SALIR"
        self.boton5_M["command"] = self.opcion_multi.destroy
        self.boton5_M.place(width=50, x=150, y=270)
        # Etiqueta de Intrucciones
        self.etiqueta1_multi = tki.Label(self.opcion_multi,
                                         text="MULTIPLICACION", bg="navy", fg="white")
        self.etiqueta1_multi.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tki.X)

        self.multi_leer_datos()

        self.boton_multi = tki.Button(
            self.opcion_multi, bg="green", fg="white")
        self.boton_multi["text"] = "RESULTADO"
        self.boton_multi["command"] = self.multi_resultado
        self.boton_multi.place(x=10, y=270)

        self.etiqueta_multi1 = tki.Label(
            self.opcion_multi, textvariable=self.var3, bg="navy", fg="blue")
        self.etiqueta_multi1.pack(padx=5, pady=5, ipadx=5, ipady=5)

    def multi_leer_datos(self):
        self.etiqueta_multiA = tki.Label(
            self.opcion_multi, text="MULTIPLICADOR:", bg="navy", fg="white")
        self.etiqueta_multiA.pack(padx=5, pady=5, ipadx=5, ipady=5)

        self.valorE = tki.Entry(self.opcion_multi)
        self.valorE.pack(padx=5, pady=5, ipadx=5, ipady=5)

        self.etiqueta_multiB = tki.Label(
            self.opcion_multi, text="MULTIPLICADOR:", bg="navy", fg="white")
        self.etiqueta_multiB.pack(padx=5, pady=5, ipadx=5, ipady=5)

        self.valorF = tki.Entry(self.opcion_multi)
        self.valorF.pack(padx=5, pady=5, ipadx=5, ipady=5)

    def multi_resultado(self):

        self.multiEF = float(self.valorE.get()) * float(self.valorF.get())
        return self.var3.set(self.multiEF)
# DIVISION opcion

    def division(self):
        self.opcion_divide = tki.Toplevel(self)
        self.opcion_divide.title("DIVISION")
        self.opcion_divide.resizable(100, 100)
        self.opcion_divide.geometry('210x300+1125+250')
        self.opcion_divide.configure(background="black")
        # Variable que controla el valor  resultado de division
        self.var4 = tki.StringVar(self)
        # exit from window
        self.boton5_D = tki.Button(self.opcion_divide, bg="navy", fg="white")
        self.boton5_D["text"] = "SALIR"
        self.boton5_D["command"] = self.opcion_divide.destroy
        self.boton5_D.place(width=50, x=150, y=270)
        # Etiqueta de Intrucciones
        self.etiqueta1_divi = tki.Label(self.opcion_divide,
                                        text="DIVISION", bg="orange", fg="white")
        self.etiqueta1_divi.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tki.X)

        self.division_leer_datos()

        self.boton_divi = tki.Button(
            self.opcion_divide, bg="green", fg="white")
        self.boton_divi["text"] = "RESULTADO"
        self.boton_divi["command"] = self.division_resultado
        self.boton_divi.place(x=10, y=270)

        self.etiqueta_divi1 = tki.Label(
            self.opcion_divide, textvariable=self.var4, bg="orange", fg="blue")
        self.etiqueta_divi1.pack(padx=5, pady=5, ipadx=5, ipady=5)

    def division_leer_datos(self):
        self.etiqueta_diviA = tki.Label(
            self.opcion_divide, text="NUMERADOR:", bg="navy", fg="white")
        self.etiqueta_diviA.pack(padx=5, pady=5, ipadx=5, ipady=5)

        self.valorG = tki.Entry(self.opcion_divide)
        self.valorG.pack(padx=5, pady=5, ipadx=5, ipady=5)

        self.etiqueta_diviB = tki.Label(
            self.opcion_divide, text="DENOMINADOR:", bg="navy", fg="white")
        self.etiqueta_diviB.pack(padx=5, pady=5, ipadx=5, ipady=5)

        self.valorH = tki.Entry(self.opcion_divide)
        self.valorH.pack(padx=5, pady=5, ipadx=5, ipady=5)

    def division_resultado(self):

        self.diviGH = float(self.valorG.get()) / float(self.valorH.get())
        return self.var4.set(self.diviGH)


root = tki.Tk()
master = root
myapp = Integral(master=root)
myapp.master.title("Ventana INTEGRAL")
myapp.master.geometry("1200x400+10+10")
myapp.master.resizable(width=False, height=False)
myapp.master.configure(background="black")
myapp.mainloop()

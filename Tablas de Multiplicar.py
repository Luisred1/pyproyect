#!/usr/bin/env python
# -*- coding: utf-8 -*--
"""
   Created 10-may -2020
   @Autor: jlred -Jose Luis Rojas C.
"""
import sys
# from tkinter import ttk
# from tkinter import *
import tkinter
import tkinter as ttk
# from tkinter.ttk import *
# from tkinter import tki, messagebox


class Aplicacion(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.ventana_principal()

    def ventana_principal(self):
        self.boton_ventana_principal = ttk.Button(root, bg="green", fg="white")
        self.boton_ventana_principal["text"] = "MENU"
        self.boton_ventana_principal["command"] = self.inicio
        self.boton_ventana_principal.pack()

        self.boton_salir = ttk.Button(root, bg="yellow", fg="red")
        self.boton_salir["text"] = "EXIT"
        self.boton_salir["command"] = self.master.destroy
        self.boton_salir.pack()

    def inicio(self):
        self.raiz = ttk.Tk()
        self.raiz.geometry('700x400')
        self.raiz.configure(bg='navy')
        self.raiz.resizable(width=False, height=False)
        self.raiz.title('MENU PRINCIPAL')
        self.labeltop = ttk.Label(
            self.raiz, text=" Programa para el desarrollo de proyectos \n Elige la opcion deseada\n MENU ", bg='azure4')
        self.labeltop.place(x=100, y=30)
        # LLAMADA A TABLAS DE MULTIPLICAR
        self.watch4 = ttk.Button(
            self.raiz, text='Tablas', bg="black", fg="gray", command=self.win2)
        self.watch4.place(x=100, y=100)
        self.labeltop_TM = ttk.Label(
            self.raiz, text=" Calculo de tablas matematicas rango ( 1 - 10 )", bg='black', fg="white")
        self.labeltop_TM.place(x=250, y=100)
        # LLAMADA A ORDEN ASCENDENTE
        self.orden_ascendente = ttk.Button(self.raiz, bg="black", fg="gray")
        self.orden_ascendente["text"] = "ASCENDENTE"
        self.orden_ascendente["command"] = self.ascendente
        self.orden_ascendente.place(x=100, y=140)
        self.labeltop_ASC = ttk.Label(
            self.raiz, text=" Lectura de datos y ordenarlos de forma ascendente ", bg='black', fg='white')
        self.labeltop_ASC.place(x=250, y=140)

        self.watch5 = ttk.Button(
            self.raiz, text='SALIR', bg="black", fg="gray", command=self.raiz.destroy)
        # self.watch5.grid(column=0, row=3)
        self.watch5.place(x=100, y=300)
        self.raiz.mainloop()

    def win2(self):
        self.tabla = ttk.Toplevel(self.raiz)
        self.tabla.configure(bg='black')
        self.tabla.title('TABLA')
        self.tabla.geometry('600x600')
        self.labelwin1 = ttk.Label(
            self.tabla, text="Selecciona la tabla a multiplicar 1 al 10", bg='azure4', fg='navy')
        self.labelwin1.grid(column=0, row=1)
        self.labeltop.grid(column=0, row=0)
        self.watch = ttk.Button(self.tabla, text='Tabla', command=self.leer)
        self.watch.grid(column=0, row=2)
        self.watch1 = ttk.Button(
            self.tabla, text='calculo', command=self.calculo)
        self.watch1.grid(column=1, row=3)
        # self.watch1= ttk.Button(self.raiz, text='contenido', command=self.imprime)
        # self.watch1.grid(column=2, row=2)
        self.watch3 = ttk.Button(
            self.tabla, text='biblioteca', command=self.biblioteca)
        self.watch3.grid(column=1, row=4)
        # self.qinfo =Text(self.tabla, width=40, height=10, bg='slate blue')
        # self.qinfo["text"] = (self.tabla, width=40, height=10, bg='slate blue')
        self.qinfo = ttk.Text(self.tabla, width=40, height=10, bg='royal blue')
        self.qinfo.grid(column=0, row=3)

        self.finfo = ttk.Text(self.tabla, width=40, height=10, bg='royal blue')
        self.finfo.grid(column=0, row=4)

        self.tinfo = ttk.Text(self.tabla, width=40,
                              height=10, bg='slate blue1')
        self.tinfo.grid(column=0, row=5)

        self.binfo = ttk.Button(self.tabla, text='Info', command=self.verinfo)
        self.binfo.grid(column=1, row=5)

        self.bsalir = ttk.Button(
            self.tabla, text='Salir', command=self.tabla.destroy)
        self.bsalir.grid(column=2, row=5)

        # self.binfo.focus_set()
        self.raiz.mainloop()

    def leer(self):

        self.combo = ttk.Spinbox(
            self.tabla, values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        # self.combo.current(0)
        self.combo.grid(column=0, row=2)
        # self.combo.bind("<<ComboboxSelected>>", self.leer)
        self.value = self.combo.get()
        # print(self.combo.current(), value)

    def calculo(self):
        self.producto = {}
        self.mult1 = 1
        while self.mult1 <= 10:
            self.resultado = self.mult1 * int(self.combo.get())
            self.producto[self.mult1] = (self.resultado)
            self.mult1 += 1
            # print( "los multiplos son :", self.resultado)
        return self.producto

    def imprime(self):
        print("lectura del dicionario")
        for self.resultado in self.producto:
            print(self.producto[self.resultado])

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

        # Borra el contenido que tenga en un momento dado
        # la caja de texto

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
        self.ventana_ascendente = ttk.Toplevel(self.raiz, bg="black")
        self.ventana_ascendente.title("OPERACIONES CON DATOS ASCENDENTES")
        self.ventana_ascendente.geometry("400x400+120+120")
        self.ventana_ascendente.resizable(100, 100)
        self.e3 = ttk.Label(self.ventana_ascendente, text="BIENVENIDO A REALIZAR CALCULOS\nCON OPERACIONES ASCENDENTES",
                            bg="gray", fg="white", font=("Arial Bold", 10))
        self.e3.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=ttk.X)
        self.boton_salir_datos_ascendentes = ttk.Button(
            self.ventana_ascendente, bg="black", fg="gray")
        self.boton_salir_datos_ascendentes["text"] = "SALIR"
        self.boton_salir_datos_ascendentes["command"] = self.ventana_ascendente.destroy
        self.boton_salir_datos_ascendentes.place(x=200, y=370)

        self.boton_leer_datos_asc = ttk.Button(
            self.ventana_ascendente, bg="black", fg="gray")
        self.boton_leer_datos_asc["text"] = "LEER DATOS"
        self.boton_leer_datos_asc["command"] = self.leer_datos_ascendente
        self.boton_leer_datos_asc.place(x=50, y=70)

        self.boton_proceso_asc = ttk.Button(
            self.ventana_ascendente, bg="black", fg="gray")
        self.boton_proceso_asc["text"] = "LEER  ASCENDENTE"
        self.boton_proceso_asc["command"] = self.proceso_asc
        self.boton_proceso_asc.place(x=50, y=100)

        self.boton_proceso_desc = ttk.Button(
            self.ventana_ascendente, bg="black", fg="gray")
        self.boton_proceso_desc["text"] = "LEER  DESCENDENTE"
        self.boton_proceso_desc["command"] = self.proceso_des
        self.boton_proceso_desc.place(x=50, y=130)

        self.textoinfo1 = ttk.Text(
            self.ventana_ascendente, width=40, height=10, bg="black", fg="white")
        self.textoinfo1.place(x=5, y=160)

        self.boton_presenta_Datos = ttk.Button(
            self.ventana_ascendente, bg="black", fg="white")
        self.boton_presenta_Datos["text"] = "LEER  DATOS"
        self.boton_presenta_Datos["command"] = self.presenta_Datos
        self.boton_presenta_Datos.place(x=50, y=330)

    def leer_datos_ascendente(self):
        self.ventana_leer_datos_asc = ttk.Toplevel(
            self.ventana_ascendente, bg="black")
        self.ventana_leer_datos_asc.title("Lectura de Datos")
        self.ventana_leer_datos_asc.geometry("400x320+140+140")
        self.ventana_leer_datos_asc.resizable(width=False, height=False)

        self.boton_salir_leer_datos_asc = ttk.Button(
            self.ventana_leer_datos_asc, bg="black", fg="gray")
        self.boton_salir_leer_datos_asc["text"] = "SALIR"
        self.boton_salir_leer_datos_asc["command"] = self.ventana_leer_datos_asc.destroy
        self.boton_salir_leer_datos_asc.place(x=300, y=290)

        self.lista1 = []
        # self.lista2 = []
        self.control = 0
        self.valor1 = 0
        self.etiqueta_leer_dato = ttk.Label(
            self.ventana_leer_datos_asc, text="INTRODUCE DIEZ NUMEROS:", bg="navy", fg="white")
        self.etiqueta_leer_dato.pack(padx=5, pady=5, ipadx=5, ipady=5)
        self.textoinfo = ttk.Text(
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


root = ttk.Tk()
myapp = Aplicacion(master=root)
myapp.master.title("PROYECTOS")
myapp.master.geometry("1000x400+100+100")
myapp.master.configure(bg='navy')
myapp.mainloop()

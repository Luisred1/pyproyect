#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Created 20-jul -2020
   @Autor: jlred -Jose Luis Rojas C.
"""
import sys
import tkinter as tki
from tkinter import messagebox


class Agenda(tki.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.abrir()

    def abrir(self):
        self.marco = tki.Frame(
            root, borderwidth=2, relief="raised")
        self.e3 = tki.Label(
            text="BIENVENIDO AL MENU MATEMATICO", bg="gray", fg="white", font=("Arial Bold", 20))
        self.e3.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tki.X)
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
        self.quit = tki.Button(root, text="QUIT", bg="red", fg="white",
                               command=self.master.destroy)
        self.quit.place(width=70, x=400, y=100)

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
        self.boton7["command"] = self.calculo
        self.boton7.place(width=100, x=10, y=100)

        self.boton8 = tki.Button(self.opcion, bg="purple", fg="white")
        self.boton8["text"] = "BIBLIOTECA"
        self.boton8["command"] = self.biblioteca
        self.boton8.place(width=100, x=10, y=130)

        self.qinfo = tki.Text(self.opcion, width=40,
                              height=10, bg='royal blue')
        self.qinfo.place(x=5, y=160)
        # Obtener informacion de la ventana de tablas de multiplicacion

    def leerTM(self):
        self.combo1 = tki.Spinbox(
            self.opcion, values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.combo1.place(x=20, y=70)
        self.value = self.combo1.get()

    def calculo(self):
        self.producto = {}
        self.mult1 = 1
        while self.mult1 <= 10:
            self.resultado = self.mult1 * int(self.combo1.get())
            self.producto[self.mult1] = (self.resultado)
            self.mult1 += 1
        return self.producto

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
myapp = Agenda(master=root)
myapp.master.title("Bienvenido al menu de la agenda matematica")
# myapp.master.maxsize(1200, 800)
# myapp.master.resizable("100x100")
myapp.master.geometry("1320x600+20+30")
myapp.master.configure(background="black")
myapp.mainloop()

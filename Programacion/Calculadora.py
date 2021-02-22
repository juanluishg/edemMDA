# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 20:16:42 2021

@author: JuanLu
"""

###RETO - Calculadora
import PySimpleGUI as sg  

class calculadora:
    
    a = 0
    b = 0
    ans = 0
    
    def __init__(self, a, b):
        #self.a = int(input("Dame el primer numero: "))
        #self.b = int(input("Dame el segundo numero: "))
        self.a = a
        self.b = b

    def suma(self):
        self.ans = self.a + self.b
        return self.ans
    
    def resta(self):
        self.ans = self.a - self.b
        return self.ans
    
    def division(self):
        self.ans = self.a / self.b
        return self.ans
    
    def modulo(self):
        self.ans = self.a % self.b
        return self.ans
    
    def multiplicacion(self):
        self.ans = self.a * self.b
        return self.ans
    
    
class init_calc:
    op = ""
    c = None
    def __init__(self, c, op):
        #self.op = input("¿Que operación quieres realizar?(Suma/Resta/Multiplicacion/Division/Modulo)")
        self.op = op
        self.c = c
    def calc(self):
        if self.op == "Suma":
            print(self.c.suma())
            return self.c.suma()
        elif self.op == "Resta":
            print(self.c.resta())
            return self.c.resta()
        elif self.op == "Multiplicacion":
            print(self.c.multiplicacion())
            return self.c.multiplicacion()
        elif self.op == "Division":
            print(self.c.division())
            return self.c.division()
        elif self.op == "Modulo":
            print(self.c.modulo())
            return self.c.modulo()
        else:
            print("Operación " + self.op + " desconocida")
            
            
c = None

layaout = [ [sg.Text("Escribe el primer número")],
            [sg.Input(key="num1"), sg.Button("Ans1")],
            [sg.Text("Escribe el segundo número")],
            [sg.Input(key="num2"), sg.Button("Ans2")],
            [sg.Text(size=(40,1), key='-OUTPUT-')],
            [sg.Button("Suma"),
             sg.Button("Resta"),
             sg.Button("Division"),
             sg.Button("Multiplicacion"),
             sg.Button("Modulo")],
            [sg.Button("Cerrar", button_color=("white", "red"))]]

window = sg.Window('Calculadora', layaout, icon="./figures/calc.ico")

while True:
    event, values = window.read()
        
    if event == "Ans1":
        if c != None:
            window["num1"].update(c.ans)
        else:
            window["num1"].update(0)
            
    elif event == "Ans2":
        if c != None:
            window["num2"].update(c.ans)
        else:
            window["num2"].update(0)
        
    elif event == "Cerrar" or event == sg.WINDOW_CLOSED:
        break

    else:
        c = calculadora(int(values["num1"]), int(values["num2"]))
        res = init_calc(c, event)

        window['-OUTPUT-'].update('El Resultado es: ' + str(res.calc()), text_color='yellow')

window.close()
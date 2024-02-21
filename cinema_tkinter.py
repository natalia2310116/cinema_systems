import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

NUMEROOPCIONES = 4 #recordar crear función que verifica que el número ingresado sea uno de los esperados



logScreenText = ""

cantidadBoletasBarbieNoGeneral = 0

peliculaCliente = []

ubicaciónCliente = []

comboCliente = []

numeroVentas = 0

tablaResultados = [peliculaCliente, ubicaciónCliente, comboCliente]

window = Tk()
window.title("CinemAAA")
window.geometry("300x200")
    
title = tk.Label(window, text="Bienvenido a CinemaAAA")
title.pack()

mainframe = ttk.Frame(window)
mainframe.pack()


def main():

    logScreen = Text(mainframe,height="6")
    logScreen.grid(row=0, column=0)

    logScreen.insert(1.0, logScreenText)
    logScreen.configure(state="disabled")

    buttonStartProgram = Button(mainframe, text= "Comprar boletas", command=lambda: elegir_pelicula()) 
    buttonStartProgram.grid(row= 3, column=0)


        
def createTopLevelWindow(title, labelText):
    top = Toplevel()
    top.title(title)
    top.geometry("400x400")

    mainLabel = tk.Label(top, text= labelText)
    mainLabel.pack()

    return top


def createButton(top, buttonText, command, row, column):

    button = tk.Button(top, text= buttonText, command= command)
    button.grid(row= row, column= column)



def buttonClicked(listName, list, option, nextFunction, top):

    global logScreenText


    list.append(option)
    newLogScreenText = f"{listName}: {option}\n\n"
    logScreenText = logScreenText + newLogScreenText
    main()

    top.destroy()

    nextFunction()

def elegir_pelicula():

    top = createTopLevelWindow("Elegir pelicula", "¿Qué pelicula desea ver?")

    framePelicula = tk.Frame(top)    
    framePelicula.pack()

    createButton(framePelicula, "Flash", lambda :buttonClicked("Pelicula", peliculaCliente, "Flash", elegir_ubicacion, top), 0, 0)
    createButton(framePelicula, "Indiana Jones", lambda :buttonClicked("Pelicula", peliculaCliente, "Indiana Jones", elegir_ubicacion, top), 0, 1)
    createButton(framePelicula, "Barbie", lambda: buttonClicked("Pelicula", peliculaCliente, "Barbie", elegir_ubicacion, top), 0, 3)
    createButton(framePelicula, "Openheimer", lambda :buttonClicked("pelicula", peliculaCliente, "Openheimer", elegir_ubicacion, top), 0, 4)



def elegir_ubicacion():

    top = createTopLevelWindow("Elegir ubicación", "¿Qué ubicación vas a elegir?")


    mainFrame = tk.Frame(top)
    mainFrame.pack()

    createButton(mainFrame, "General", lambda: buttonClicked("Ubicación", ubicaciónCliente, "General", elegir_Combo, top), 0, 0)
    createButton(mainFrame, "Preferencial", lambda: buttonClicked("Ubicación", ubicaciónCliente, "Preferencial", elegir_Combo, top), 0, 1)
    createButton(mainFrame, "VIP", lambda: buttonClicked("Ubicación", ubicaciónCliente, "VIP", elegir_Combo, top), 0, 2)

def elegir_Combo():    
        
    top = Toplevel()
    top.title("Elegir combo")
    top.geometry("400x400")

    LCombo = tk.Label(top, text= "¿Qué combo vas a elegir?")
    LCombo.pack()

    mainFrame = tk.Frame(top)
    mainFrame.pack()

    createButton(mainFrame, "Personal", lambda: buttonClicked("Combo", comboCliente,"Personal", comprarOtraBoleta, top), 0, 0)
    createButton(mainFrame, "Pareja", lambda: buttonClicked("Combo", comboCliente, "Pareja", comprarOtraBoleta, top), 0, 1)
    createButton(mainFrame, "Familiar", lambda: buttonClicked("Combo", comboCliente, "Familiar", comprarOtraBoleta, top), 0, 2)
    createButton(mainFrame, "SIN COMBO", lambda: buttonClicked("Combo", comboCliente, "SIN COMBO", comprarOtraBoleta, top), 0, 3)

def comprarOtraBoleta():
    global logScreenText
    global numeroVentas
    respuesta = messagebox.askquestion("Nueva boleta", "¿Deseas comprar otra boleta?")

    if(respuesta == "yes"):
        numeroVentas += 1
        logScreenText = ""
        main()
    else:
        messagebox.showinfo("CinemaAAA", "¡Gracias por ser cliente de CinemaAAA")
        estadisticas()
        

def calcular_boletas_barbie_ubicacion_no_general():
    numeroBoletas = 0
    for i in range(len(tablaResultados[0])):
        if(tablaResultados[0][i] == "Barbie"):    
            if(tablaResultados[1][i] != "General"):
                    numeroBoletas += 1
    return numeroBoletas

def calcular_porcentage_ventas_no_combo():
    global numeroVentas
    global comboCliente
    numeroSinCombo = 0

    for i in range(len(comboCliente)):
        if(comboCliente[i] == "SIN COMBO"):
            numeroSinCombo += 1
    porcentage = (numeroSinCombo/numeroVentas)*100
    if(porcentage == None):
        porcentage = 0
    return porcentage
    
def estadisticas():
    print(peliculaCliente)
    print(comboCliente)
    print(ubicaciónCliente)
    global numeroVentas
    numeroVentas += 1
    numeroBoletasBarbieNoGeneral = calcular_boletas_barbie_ubicacion_no_general()
    porcentage = calcular_porcentage_ventas_no_combo()
    messagebox.showinfo("Estadísticas", f"Número de ventas: {numeroVentas}\n\nEl número de ventas para la película Barbie en ubicación distinta a la general fue de {numeroBoletasBarbieNoGeneral}\n\nEl porcentaje de ventas sin combo fue de {porcentage}%")



main()
window.mainloop()

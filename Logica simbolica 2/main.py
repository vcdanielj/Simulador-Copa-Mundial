from modulos.manejador_db import *
from modulos.constantes import *
from tkinter import *

class ventana(Tk):
	def __init__(self):
		lbl = Label(self, text = "Hola")
		lbl.grid(row = 0, column = 0)

if __name__ == "__main__":
	ventana = ventana()
	ventana.title("Hola mundo")

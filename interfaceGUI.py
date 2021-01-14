import tkinter
from tkinter import Tk
from tkinter import filedialog as fd
from tkinter import messagebox

#Interface Gráfica
gui = tkinter.Tk()
Tk().withdraw() # Não queremos abrir a janela full da GUI
uploaded_file = fd.askopenfilename() # Opção para carregar um arquivo.
messagebox.showinfo("Aviso", "arquivo carregado")


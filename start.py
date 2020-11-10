import tkinter as tk

#from tkinter import *

#przypisanie do app obiektu TK - okna głowniego aplikacji
app = tk.Tk()

app.title("Moja apka")

#wielkosc okienka
app.geometry("600x600")
#kolor tla dla okienka
#app.configure(background="black")
#minimalna wielkosc okienka
app.minsize(300,300)

#etykieta z tekstem
label = tk.Label(app, text="Hello World!") # Create a text label
label.pack(padx=20, pady=20) # Pack it into the window

#zdarzenie wywolywane po kliknieci na przycisk
def HelloWorld():
    print("kliknieto przycisk")

#utworzenie przycisku
ok = tk.Button(app, text="OK", width=20, command=HelloWorld)
ok.pack()

#formatka do wprowadzania tekstu
e1 = tk.Entry(app)
e1.pack()

#wyswietla tekst w konsoli nie w okienku
print('hello world')

#konieczne zeby program nie zamknal sie natchmiast i bylo widac okienko
app.mainloop()
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
label = tk.Label(app, text="Wpisz adres IP:")
label.grid(row=1) # Create a text label
#label.pack(padx=20, pady=20) # Pack it into the window

#formatka do wprowadzania tekstu
adresIP = tk.Entry(app)
adresIP.grid(row=1, column=1)
adresIP.insert(10,"192.168.1.100")

#zdarzenie wywolywane po kliknieci na przycisk
def HelloWorld():
    print("kliknieto przycisk")

#utworzenie przycisku
ok = tk.Button(app, text="OK", width=20, command=HelloWorld)
ok.grid(row=1,column=2)

root = tk.Tk()
scrollbar = root.Scrollbar(root)
scrollbar.pack( side = "RIGHT", fill = "Y" )

mylist = tk.Listbox(root, yscrollcommand = scrollbar.set )
for line in range(100):
   mylist.insert(END, "This is line number " + str(line))

mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )


#wyswietla tekst w konsoli nie w okienku
print('hello world')

#konieczne zeby program nie zamknal sie natchmiast i bylo widac okienko
app.mainloop()
from tkinter import *
from tkinter import ttk

win = Tk()

wrapper1 = LabelFrame(win)
wrapper2 = LabelFrame(win)

mycanvas = Canvas(wrapper2)
mycanvas.pack(side=LEFT, fill="both", expand="yes")

yscrollbar = ttk.Scrollbar(wrapper2,orient="vertical",command=mycanvas.yview)
yscrollbar.pack(side=LEFT, fill="y")

mycanvas.configure(yscrollcommand=yscrollbar.set)

mycanvas.bind('<Configure>',lambda e: mycanvas.configure(scrollregion=mycanvas.bbox('all')))

myframe = Frame(mycanvas)
mycanvas.create_window((0,0), window=myframe, anchor="nw")

wrapper1.pack(fill="both", expand="yes", padx=10, pady=10)
wrapper2.pack(fill="both", expand="yes", padx=10, pady=10)

for i in range(50):
    Button(myframe, text="My Button - "+str(i)).pack()

tv=ttk.Treeview(wrapper1, columns=(1,2,3), show="headings", height="5")
tv.pack()

tv.heading(1, text="Name")
tv.heading(2, text="Age")
tv.heading(3, text="Emaol")


win.geometry("700x500")
win.resizable(False,False)
win.title("Scroller")
win.mainloop()

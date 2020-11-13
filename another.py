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

tv=ttk.Treeview(wrapper1, columns=(1,2,3,4,5,6,7,8), show="headings", height="5")
tv.pack(expand=YES, fill=BOTH)

tv.heading(1, text="SSID")
tv.column(1, minwidth=50, width=300, stretch=NO) 
tv.heading(2, text="IP")
tv.column(2, minwidth=50, width=200, stretch=NO) 
tv.heading(3, text="APC")
tv.column(3, minwidth=50, width=80, stretch=NO) 
tv.heading(4, text="KANAŁ")
tv.column(4, minwidth=50, width=80, stretch=NO) 
tv.heading(5, text="SZYBKOŚĆ")
tv.column(5, minwidth=50, width=80, stretch=NO) 
tv.heading(6, text="PING")
tv.column(6, minwidth=50, width=80, stretch=NO) 
tv.heading(7, text="JaMAX")
tv.column(7, minwidth=50, width=80, stretch=NO) 
tv.heading(8, text="PaMAX")
tv.column(8, minwidth=50, width=80, stretch=NO) 



win.geometry("1100x500")
win.resizable(False,False)
win.title("Scroller")
win.mainloop()

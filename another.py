from tkinter import *
from tkinter import ttk

import requests
import json

from config import *

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

tv=ttk.Treeview(wrapper1)
tv["columns"]=(1,2,3,4,5,6,7,8)

tv.heading("#0", text="SSID")
tv.column("#0", minwidth=80, width=150, stretch=YES, anchor=W) 
tv.heading(1, text="IP")
tv.column(1, minwidth=120,  width=120, stretch=NO, anchor=W) 
tv.heading(2, text="APC")
tv.column(2, minwidth=120, width=120, stretch=NO, anchor=CENTER) 
tv.heading(3, text="KANAŁ")
tv.column(3, minwidth=40, width=60, stretch=NO, anchor=CENTER) 
tv.heading(4, text="SZYBKOŚĆ")
tv.column(4, minwidth=40, width=70, stretch=NO, anchor=CENTER) 
tv.heading(5, text="PING")
tv.column(5, minwidth=40, width=60, stretch=NO, anchor=CENTER) 
tv.heading(6, text="CCQ")
tv.column(6, minwidth=40, width=60, stretch=NO, anchor=CENTER) 
tv.heading(7, text="AirMAX")
tv.column(7, minwidth=40, width=60, stretch=NO, anchor=CENTER) 
tv.heading(8, text="PLATFORMA")
tv.column(8, minwidth=100, width=100, stretch=YES, anchor=W) 
#tv.heading(9, text="UPTIME")
#tv.column(9, minwidth=80, width=100, stretch=YES, anchor=W) 

dane=[
    ["AP04","10.100.100.87","23","5400","9/78","65","23","35"],
    ["AP01","10.100.100.2","34","5420","9/78","12","78","23"],
    ["AP06","10.100.100.2","12","5280","9/78","34","34","12"],
    ["AP34","10.100.100.2","53","5660","9/78","23","83","54"],
    ["AP02","10.100.100.2","12","5180","9/78","76","35","12"]
]

nr=0
for linia in dane:
    tv.insert(parent="", index='end', iid=nr, text=linia[0], values=(linia[1],linia[2],linia[3],linia[4],linia[5],linia[6],linia[7]))    
    nr+=1

#tv.insert(parent="", index='end', iid=1, text="Parent", values=("AP04","10.100.100.2","23","5400","9/78","65","23","35"))
#tv.insert(parent="", index='end', iid=0, text="Parent", values=("AP01","10.100.100.2","34","5420","9/78","12","78","23"))
#tv.insert(parent="", index='end', iid=2, text="Parent", values=("AP06","10.100.100.2","12","5280","9/78","34","34","12"))
##tv.insert(parent="", index='end', iid=3, text="Parent", values=("AP34","10.100.100.2","53","5660","9/78","23","83","54"))
#tv.insert(parent="", index='end', iid=4, text="Parent", values=("AP02","10.100.100.2","12","5180","9/78","76","35","12"))

tv.move("4","1",'end')
tv.move("3","4",'end')
tv.move("2","4",'end')
tv.pack(expand=YES, fill=BOTH)




headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

login_data = {
    'username': LOGIN,
    'password': PASSWORD,
    'uri': 'sta.cgi',
}

with requests.Session() as s:
    url = 'http://10.100.100.87/login.cgi'
    r = s.get(url, headers=headers)
    r = s.post(url, data=login_data, headers=headers)
    r1 = s.get('http://10.100.100.87/sta.cgi', headers=headers)
    r1.encoding='utf8'
    res=json.loads(r1.text)
    
    for linia in res:
        #print(json.loads(linia))
        #print(linia['signals'])
        remote=''
        if 'remote' in linia:
            #print(linia['remote']['platform'])
            remote=linia['remote']['platform']
        tv.insert(parent="0", index='end', iid=nr, text=linia['name'], values=(linia['lastip'],linia['mac'],linia['signal'],str(int(linia['tx']))+"/"+str(int(linia['rx'])),linia['tx_latency'],linia['ccq'],linia['airmax']['quality'],remote))    
        nr+=1

'''
print(res['name'])
print(res['mac'])
print(res['lastip'])
print(res['signal'])
print(r1.text) 
'''


win.geometry("1100x500")
win.resizable(True,True)
win.minsize(700,500)
win.title("Nowa Fajna Apka")
win.mainloop()

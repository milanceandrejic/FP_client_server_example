
import time
from tkinter import *
import tkinter
import threading
import socket

tk = tkinter.Tk()

c = tkinter.Canvas(tk, bg="yellow", height=250, width=300)
coord = 50, 50, 250, 250
arc = c.create_arc(coord, start=0, extent=180, fill="red")
linija = c.create_arc(coord, start=0, extent=0)
global i
global koef
c.pack()

def animacija():
    i = 0
    koef = 1
    while True:
        i += koef
        c.itemconfig(linija, start=i)
        c.update()
        time.sleep(0.01)

        if i>=180 and odg.get(0)=="Vidimo se!":
            odg.insert(0,"Animacija zaustavljena")
            c.delete(linija)
            for ugao in range(180):
                c.itemconfig(arc, extent=180-ugao)
                c.update()
            c.delete(arc)
        elif i >= 180:
            i = 0


b1 = tkinter.Button(tk, background='blue', text='ime', foreground='black', width=30)
b1.pack()
tb = tkinter.Entry(tk, width=30)
tb.pack()

def sel():
    if var.get() == 1:
        zaserver = 'vr:'
    elif var.get() == 3:
        zaserver = 'kr:'
    else:
        zaserver = 'salon:'
        zaserver += automobili.get(ACTIVE) + ':'
    return zaserver

var = IntVar()
r1 = Radiobutton(tk, variable=var, text='Vreme', value=1, command=sel)
r1.pack()
r2 = Radiobutton(tk, variable=var, text='SALON AUTOMOBILA', value=2, command=sel)
r2.pack()

automobili = Listbox(tk, selectmode=SINGLE, height=3)
automobili.insert(0, 'BMW')
automobili.insert(0, 'AUDI')
automobili.insert(0, 'MERCEDES')
automobili.pack()

r3 = Radiobutton(tk, variable=var, text='Kraj', value=3, command=sel)
r3.pack()
var.set(1)

def posaljiServeru():
    if tb.get() != "":
        ime = tb.get() + ":"
    else:
        ime = "KLIJENT:"
    poruka = ime + sel()
    s = socket.socket()
    host = socket.gethostname()
    port = 9000
    s.connect((host, port))
    s.send(poruka.encode())
    odsrv = s.recv(1024).decode()
    odg.insert(0, odsrv)
    s.close()

b2 = tkinter.Button(tk, background='blue', text='Posalji zahtev serveru', foreground='black', width=30,
                    command=posaljiServeru)
b2.pack()

odlab = Label(tk, text='Odgovori sa servera')
odlab.pack()

odg = Listbox(tk, selectmode=SINGLE, height=10, width=30)
odg.pack()

animTh = threading.Thread(target=animacija)
animTh.start()

tk.mainloop()

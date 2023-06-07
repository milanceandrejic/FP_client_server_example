from tkinter import *
import tkinter
import threading
import socket
from time import *

global odg

salon = {}

tk = tkinter.Tk()

odg = Listbox(tk, selectmode=SINGLE, height=40, width=30)
odg.pack()

def server():

    s = socket.socket()
    host = socket.gethostname()
    port = 9000
    s.bind((host, port))
    s.listen(5)
    odg.insert(0, 'SERVER:waiting...')
    while True:
        conn, addr = s.accept()
        poruka = conn.recv(1024).decode()
        odg.insert(0, poruka)
        odservera = ''
        niz = poruka.split(":")

        if niz[1] == 'vr':
            odservera = "Vreme je " + strftime("%H:%M:%S", localtime())
        elif niz[1] == 'kr':
            odservera = "Vidimo se!"
        elif niz[1] == 'salon':
            key = niz[2]
            print(key)
            if key in salon.keys():
                salon[key] = salon[key] + 1
            else:
                salon[key] = 1
            odservera = niz[0] + " " + str(salon)
            print(odservera)

        conn.send(odservera.encode())
        odg.insert(0, "SERVER:waiting...")
        conn.close()

th = threading.Thread(target=server)
th.start()

t2 = threading.Thread(target=tk.mainloop()).start()

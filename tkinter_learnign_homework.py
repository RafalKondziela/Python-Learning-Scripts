from tkinter import *
from string import *


def doDuzych():
    duze = poleText.get()
    duze = duze.upper()
    Label(okno, text="Duze litery: ").grid(row=2, column=0)
    Label(okno, text = str(duze)).grid(row=2, column=1)



okno = Tk()

Label(okno, text="Podaj tekst : ").grid(row=0)

poleText = Entry(okno)
poleText.grid(row=0, column=1)

przyciskDuzeLitery = Button(okno, text='Duże Litery', command=doDuzych)
przyciskDuzeLitery.grid(row=1)

mainloop()

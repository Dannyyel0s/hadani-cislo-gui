import tkinter as tk
import random
from turtle import back

tajne_cislo = random.randint(1, 20)
pokusy = 0


def tvuj_tip():
    global pokusy
    tip = int(vstup.get())
    pokusy += 1

    if tip == tajne_cislo:
        vysledek["text"] = f"Uhodl jsi číslo za {pokusy} pokusů!"
        tlacitko["state"] = "disabled"
    elif pokusy == 5:
        vysledek["text"] = f"Prohrál jsi. Bylo to {tajne_cislo}"
        tlacitko["state"] = "disabled"
    elif tip < tajne_cislo:
        vysledek["text"] = "Číslo je větší."
    else:
       vysledek["text"] = "Číslo je menší."

okno = tk.Tk()
okno.title("Hádej číslo")
okno.geometry("600x400")

popis = tk.Label(okno, text="Hádej číslo od 1 do 20:")
popis.pack()

vstup = tk.Entry(okno)
vstup.pack()

tlacitko = tk.Button(okno, text="Tipni", command=tvuj_tip)
tlacitko.pack()

vysledek = tk.Label(okno, text="")
vysledek.pack()

okno.mainloop()
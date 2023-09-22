import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class Sklep:
    def __init__(self, master):
        self.master = master
        self.master.title("Gra sklep")

        self.produkty = {
            "Chleb": 3,
            "Mleko": 2,
            "Jaja": 5
        }

        self.zakupy = {}

        ttk.Label(self.master, text="Produkty w sklepie").grid(
            column=0, row=0, pady=5
        )

        for index, product in enumerate(self.produkty):
            ttk.Label(self.master, text=f"{product}: {self.produkty[product]} zł").grid(
                column=0, row=index + 1, pady=5, padx=5
            )

            self.zakupy[product] = tk.IntVar()
            ttk.Entry(self.master, textvariable=self.zakupy[product]).grid(
                column=1, row=index + 1, pady=5, padx=5
            )

        ttk.Button(self.master, text="Złóż zamówienie", command=self.zloz_zamowienie).grid(
            column=0, row=len(self.produkty) + 1, padx=5, pady=5, columnspan=2
        )

    def zloz_zamowienie(self):
        suma = 0
        for product in self.produkty:
            ilosc = self.zakupy[product].get()
            cena = self.produkty[product] * ilosc
            suma += cena

        tk.messagebox.showinfo("Podsumowanie zamówienia", f"Koszt: {suma} zł")


okno = tk.Tk()
sklep = Sklep(okno)
okno.mainloop()

# pip freeze > requinments.txt
# pip install -r requinments.txt
# pip install pyinstaller
# pyinstaller tkinter5-sklep.py

import tkinter as tk


def show_text():
    text = entry.get()
    print(f"Wprowadzony tekst: {text}")


app= tk.Tk()
app.title("Pole wprowadzania")

entry = tk.Entry(app)
entry.pack()

button = tk.Button(app, text="Pokaż tekst", command=show_text)
button.pack(side=tk.BOTTOM)  # "bottom" -> tk.BOTTOM, enumy

app.mainloop()
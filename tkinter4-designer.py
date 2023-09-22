import tkinter as tk
import tkinter.font as tkFont


class App:
    def __init__(self, root):
        # setting title
        root.title("undefined")
        # setting window size
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_573 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_573["font"] = ft
        GLabel_573["fg"] = "#333333"
        GLabel_573["justify"] = "center"
        GLabel_573["text"] = "label"
        GLabel_573.place(x=260, y=140, width=70, height=25)

        GCheckBox_199 = tk.Checkbutton(root)
        ft = tkFont.Font(family='Times', size=10)
        GCheckBox_199["font"] = ft
        GCheckBox_199["fg"] = "#333333"
        GCheckBox_199["justify"] = "center"
        GCheckBox_199["text"] = "CheckBox"
        GCheckBox_199.place(x=130, y=80, width=70, height=25)
        GCheckBox_199["offvalue"] = "0"
        GCheckBox_199["onvalue"] = "1"
        GCheckBox_199["command"] = self.GCheckBox_199_command

        GButton_993 = tk.Button(root)
        GButton_993["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_993["font"] = ft
        GButton_993["fg"] = "#000000"
        GButton_993["justify"] = "center"
        GButton_993["text"] = "Button"
        GButton_993.place(x=160, y=220, width=70, height=25)
        GButton_993["command"] = self.GButton_993_command

        GLineEdit_949 = tk.Entry(root)
        GLineEdit_949["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GLineEdit_949["font"] = ft
        GLineEdit_949["fg"] = "#333333"
        GLineEdit_949["justify"] = "center"
        GLineEdit_949["text"] = "Entry"
        GLineEdit_949.place(x=180, y=320, width=70, height=25)

        GMessage_890 = tk.Message(root)
        ft = tkFont.Font(family='Times', size=10)
        GMessage_890["font"] = ft
        GMessage_890["fg"] = "#333333"
        GMessage_890["justify"] = "center"
        GMessage_890["text"] = "Message"
        GMessage_890.place(x=310, y=200, width=80, height=25)

        GListBox_55 = tk.Listbox(root)
        GListBox_55["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GListBox_55["font"] = ft
        GListBox_55["fg"] = "#333333"
        GListBox_55["justify"] = "center"
        GListBox_55.place(x=440, y=60, width=80, height=25)

    def GCheckBox_199_command(self):
        print("command2")

    def GButton_993_command(self):
        print("command")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
# visualtk.com

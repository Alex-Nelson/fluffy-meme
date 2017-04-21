from tkinter import *


def sel(var, label):
    selection = "You selected the answer " + str(var.get())
    label.config(text=selection)


def display_question(win):

    # code for background image
    # background_image=Tk.PhotoImage(file="reference to image")

    # Text of question
    text = Text(win)
    text.insert(INSERT, "Consider the following code segment.\n\n")
    text.insert(INSERT, "ArrayList<String> list = new ArrayList<String>();\n\n")
    text.insert(INSERT, "list.add('P');\n")
    text.insert(INSERT, "list.add('Q');\n")
    text.insert(INSERT, "list.add('R');\n")
    text.insert(INSERT, "list.set(2, 's');\n")
    text.insert(INSERT, "list.set(2, 'T');\n")
    text.insert(INSERT, "list.add('u');\n")
    text.insert(INSERT, "System.out.println(list);\n\n")

    text.insert(END, "What is printed as a result of executing the code segment?\n")
    text.pack()


def ans_buttons(win, label, var):

    var.set('Welcome!')

    # Radio buttons for the answers
    R1 = Radiobutton(win, text="[P, Q, R, s, T]", variable=var, value="[P, Q, R, s, T]",
                     command=lambda: sel(var, label)).pack(anchor=W)

    R2 = Radiobutton(win, text="[P, Q, s, T, u]", variable=var, value="[P, Q, s, T, u]",
                     command=lambda: sel(var, label)).pack(anchor=W)

    R3 = Radiobutton(win, text="[P, Q, T, s, u]", variable=var, value="[P, Q, T, s, u]",
                     command=lambda: sel(var, label)).pack(anchor=W)

    R4 = Radiobutton(win, text="[P, T, Q, s, u]", variable=var, value="[P, T, Q, s, u]",
                     command=lambda: sel(var, label)).pack(anchor=W)

    R5 = Radiobutton(win, text="[P, T, s, R, u]", variable=var, value="[P, T, s, R, u]",
                     command=lambda: sel(var, label)).pack(anchor=W)


win = Tk()
label = Label(win, text="Welcome!")
label.pack()
display_question(win)
var = StringVar()
ans_buttons(win, label, var)
win.mainloop()

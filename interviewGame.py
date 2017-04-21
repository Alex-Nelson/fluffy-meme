from tkinter import *


# function to check if the user selected the correct answer
def correct_answer(win, but_num):
    var = StringVar()
    if but_num is 2:
        var.set("Correct!")
        mess = Message(win, textvariable=var, relief=RAISED)
        return True
    else:
        var.set("Incorrect.")
        mess = Message(win, textvariable=var, relief=RAISED)
        return False


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


def ans_buttons(win, label):
    var = StringVar()

    # Radio buttons for the answers
    r1 = Radiobutton(win, text="[P, Q, R, s, T]", variable=var, value=1,
                     command=correct_answer(win, 1))
    r1.pack(anchor=W)
    r1.select()

    r2 = Radiobutton(win, text="[P, Q, s, T, u]", variable=var, value=2,
                     command=correct_answer(win, 2))
    r2.pack(anchor=W)
    r2.deselect()

    r3 = Radiobutton(win, text="[P, Q, T, s, u]", variable=var, value=3,
                     command=correct_answer(win, 3))
    r3.pack(anchor=W)
    r3.deselect()

    r4 = Radiobutton(win, text="[P, T, Q, s, u]", variable=var, value=4,
                     command=correct_answer(win, 4))
    r4.pack(anchor=W)
    r4.deselect()

    r5 = Radiobutton(win, text="[P, T, s, R, u]", variable=var, value=5,
                     command=correct_answer(win, 5))
    r5.pack(anchor=W)
    r5.deselect()


win = Tk()
win.canvas = Canvas(win, width=600, height=600)
label = Label(win)
label.pack()
display_question(win)
background_image = PhotoImage(file="floor0side2.png")
win.canvas.create_image(300, 300, anchor=NE, image=background_image)
ans_buttons(win, label)
win.mainloop()

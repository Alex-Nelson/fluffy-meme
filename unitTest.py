import unittest, interviewGame
from tkinter import *


class TestGame(unittest.TestCase):

    # test get and display a question and answers
    def test_displayQA(self):
        win = Tk()
        label = Label(win)
        label.pack()

        result_q = interviewGame.display_question(win)
        result_a = interviewGame.ans_buttons(win, label)
        win.mainloop()

    # select correct answer
    def test_isCorrect(self):
        win = Tk()
        label = Label(win)
        label.pack()
        result_q = interviewGame.display_question(win)
        result_a = interviewGame.ans_buttons(win, label)
        win.mainloop()


'''   def test_displayBGImage(self):
        #self.assertTrue()

    # get and display a tip
    def test_displayTip(self):
        self.assertTrue()
'''


if __name__ == '__main__':
    unittest.main()

from tkinter import *
import sys
class ticTacToe():
    buttonList = []
    charList = ['X', 'O']
    player = 0
    char = 'X'
    def __init__(self):
        option = Tk()
        option.title("")
        option.geometry('180x75+500+200')
        message = Label(option, text = 'Do you want to play a computer\nor another player?')
        play2 = Button(option, text = 'Player', command = lambda: ticTacToe.start(self, option))
        message.grid(columnspan = 4, sticky = 'W')
        play2.grid(row = 1, column = 0)
        option.mainloop()
    def start(self, option):
        option.destroy()
        root = Tk()
        root.geometry('170x125+500+200')

        self.root = root
        self.root.title('')
        self.label = Label(root, text="\tPlayer X's turn\t")
        self.label.grid(columnspan = 3, sticky = W)
        for i in range(0,9):
            self.buttonList.append(Button(root, text = '  ', padx = 19))
            self.buttonList[i].config(command = lambda m = i: self.playGame(m))
            self.buttonList[i].grid(row = int(i/3) + 1, column = i % 3)
        root.mainloop()
    def playGame(self, i):
        if self.printNumber(i):
            if self.checkWin(self.buttonList):
                self.popUp('Player ' + self.charList[self.player] + " has won!")
                for item in self.buttonList:
                    item.config(state = DISABLED)
            elif self.full(self.buttonList):
                self.popUp("\tTIE\t")
                for item in self.buttonList:
                    item.config(state = DISABLED)
            else:
                self.player = (self.player + 1) % 2
                self.label.config(text = '\tPlayer {}\'s turn\t'.format(self.charList[self.player]))
    def popUp(self, message):
        new = Tk()
        new.geometry('50x50+525+250')
        message = Label(new, text = message)
        retry = Button(new, text = 'Retry', padx = 12, command = lambda: self.restart(new))
        quit = Button(new, text = 'Quit', padx = 12, command = lambda: sys.exit())

        message.grid(columnspan = 4, sticky = 'W')
        quit.grid(row = 1, column = 0)
        retry.grid(row = 1, column = 2)
    def printNumber(self, i):
        if self.buttonList[i]['text'] == '  ':
            self.buttonList[i].config(text = self.charList[self.player], padx = 20)
            return True
        return False
    def restart(self, retry):
        retry.destroy()
        for item in self.buttonList:
            item['text'] = '  '
            item.config(state = NORMAL)
        self.player = 0
        self.label.config(text = '\tPlayer X\'s turn\t')
    def full(self, board):
        for item in board:
            if item['text'] != 'X' and item['text'] != 'O':
                return False
        return True
    def checkWin(self, board):
        char = 'X'
        count = 0
        for count in range(0,1):
            for i in range(0,8,3):
                if (board[i]['text'] == char and
                    board[i + 1]['text'] == char and
                    board[i + 2]['text'] == char):
                    return True
            for i in range(0,3):
                if (board[i]['text'] == char and
                    board[i + 3]['text'] == char and
                    board[i + 6]['text'] == char):
                    return True
            count += 1
            if (board[0]['text'] == char and
                board[4]['text'] == char and
                board[8]['text'] == char):
                return True
            if (board[2]['text'] == char and
                board[4]['text'] == char and
                board[6]['text'] == char):
                return True
            char = 'O'
        return False
z = ticTacToe()



1 of 2,806
BogoSort button attempt
Inbox
x

Calvin Settipane
Attachments
4:26 PM (1 hour ago)
to me, Yindong, Brishti

Hi all,
Heres one of my attempts to add more buttons to the interface. Not working yet and not sure why.

--
Calvin Settipane

Boston College, Class of 2021

Computer Science

Email: settipac@bc.edu

Phone: 401-474-0364

Attachments area

Yindong Sun
Attachments
5:15 PM (13 minutes ago)
to Calvin, me, Brishti

Hi all,

These are the finalized visualizations.

Yin

9 Attachments

from tkinter import *
import time
import random
listLength = 50
height = 600
width = 800
time=0

class SpagehttiSort():
    def __init__(self, mywin):
        self.win = mywin
        self.list = [x for x in range(1, listLength+1)]
        self.barwidth = (width-20)//listLength
        self.height = (height-30)//listLength
        self.left= (width-listLength*self.barwidth)//2
        self.reset()

    def reset(self):
        self.time=0
        # random array
        random.shuffle(self.list)
        self.drawRect(-1)

        # reversed array 
        # self.list = [x for x in range(listLength, 0, -1)]
        # self.drawRect(-1)

        # rotated array
        # self.list = [x for x in range(int(listLength/2), listLength+1)]+[x for x in range(1, int(listLength/2))]
        # self.drawRect(-1)

        # almost sorted array
        # i = random.randint(0,int(listLength/2))
        # j = random.randint(1+int(listLength/2),listLength)
        # temp=self.list[i]
        # self.list[i]=self.list[j]
        # self.list[j]=temp
        # self.drawRect(-1)

    def drawRect(self,move):
        self.win.canvas.delete("line")
        for i in range(len(self.list)):
            color = "white"
            if i == move:
                color = "RED"
            self.win.canvas.create_rectangle(i * self.barwidth+self.left, height-10,
                                  (i+1) * self.barwidth+self.left,
                                  height-10-self.height * self.list[i],
                                  fill=color, tag="line")
            self.win.canvas.create_text(i * self.barwidth+self.left+self.barwidth/2,
                                  height-18-self.height * self.list[i],
                                  text=str(self.list[i]), tag="line")
            self.win.canvas.create_text(400, 10, text=str(self.time),tag="line")
        self.win.canvas.after(100)
        self.win.canvas.update()

    def sort(self):
        for i in range(0,listLength):
            self.time=i+1
            m=max(self.list)
            index=self.list.index(m)
            self.drawRect(index)
            self.list.pop(index)



class SortWin():
    def __init__(self):
        self.win = Tk()
        self.win.title("Spagehtti Sort")  # Set a title

        self.canvas = Canvas(self.win, bg="white", width=width, height=height)
        self.canvas.pack()

        self.frame = Frame(self.win)
        self.frame.pack()
        self.label = Label(self.frame, text="Spagehtti Sort")
        self.label.pack(side=LEFT)
        self.btStep1 = Button(self.frame, text="Begin", command=self.begin)
        self.btStep1.pack(side=LEFT)
        self.btStep2 = Button(self.frame, text="Reset", command=self.reset)
        self.btStep2.pack(side=LEFT)


    def begin(self):
        self.spagehttiSort.sort()

    def reset(self):
        self.spagehttiSort.reset()

    def show(self):
        self.spagehttiSort = SpagehttiSort(self)
        self.win.mainloop()

main = SortWin()
main.show()

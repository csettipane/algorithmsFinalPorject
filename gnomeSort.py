from tkinter import *
import time
import random
listLength = 50
height = 600
width = 800

class GnomeSort():
    def __init__(self, mywin):
        self.win = mywin
        self.list = [x for x in range(1, listLength+1)]
        self.barwidth = (width-20)//listLength
        self.height = (height-30)//listLength
        self.left= (width-listLength*self.barwidth)//2
        self.reset()

    def reset(self):
        # random array
        # random.shuffle(self.list)
        # self.drawRect(-1,-1,-1)

        # reversed array 
        # self.list = [x for x in range(listLength, 0, -1)]
        # self.drawRect(-1,-1,-1)

        # rotated array
        # self.list = [x for x in range(int(listLength/2), listLength+1)]+[x for x in range(1, int(listLength/2))]
        # self.drawRect(-1,-1,-1)

        # almost sorted array
        i = random.randint(0,int(listLength/2))
        j = random.randint(1+int(listLength/2),listLength)
        temp=self.list[i]
        self.list[i]=self.list[j]
        self.list[j]=temp
        self.drawRect(-1,-1,-1)

    def drawRect(self,curr,next, flag):

        self.win.canvas.delete("line")
        for i in range(len(self.list)):
            color = "white"
            if i<flag:
                color="BLUE"
            if i==curr:
                color = "YELLOW"
            if i==next:
                color = "RED"
            self.win.canvas.create_rectangle(i * self.barwidth+self.left, height-10,
                                  (i+1) * self.barwidth+self.left,
                                  height-10-self.height * self.list[i],
                                  fill=color, tag="line")
            self.win.canvas.create_text(i * self.barwidth+self.left+self.barwidth/2,
                                  height-18-self.height * self.list[i],
                                  text=str(self.list[i]), tag="line")
        self.win.canvas.after(100)
        self.win.canvas.update()

    def sort(self):
        index=0
        n=len(self.list)
        self.drawRect(index,index+1, -1)
        while index<n:
            if index==0:
                index = index+1
            if self.list[index]>=self.list[index-1]:
                index+=1
                self.drawRect(index,index+1, -1)
            else:
                temp = self.list[index]
                self.list[index]=self.list[index-1]
                self.list[index-1]=temp
                index-=1
                self.drawRect(index,index+1,-1)
        self.drawRect(-1,-1,len(self.list))
                


class SortWin():
    def __init__(self):
        self.win = Tk()
        self.win.title("Gnome Sort")  # Set a title

        self.canvas = Canvas(self.win, bg="white", width=width, height=height)
        self.canvas.pack()

        self.frame = Frame(self.win)
        self.frame.pack()
        self.label = Label(self.frame, text="Gnome Sort")
        self.label.pack(side=LEFT)
        self.btStep1 = Button(self.frame, text="Begin", command=self.begin)
        self.btStep1.pack(side=LEFT)
        self.btStep2 = Button(self.frame, text="Reset", command=self.reset)
        self.btStep2.pack(side=LEFT)


    def begin(self):
        self.gnomeSort.sort()

    def reset(self):
        self.gnomeSort.reset()

    def show(self):
        self.gnomeSort = GnomeSort(self)
        self.win.mainloop()

main = SortWin()
main.show()

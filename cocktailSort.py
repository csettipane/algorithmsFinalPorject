from tkinter import *
import time
import random
listLength = 50
height = 600
width = 800
time=0

class CocktailSort():
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
        self.drawRect(-1,50, 50)

        # reversed array 
        # self.list = [x for x in range(listLength, 0, -1)]
        # self.drawRect(-1,50, 50)

        # rotated array
        # self.list = [x for x in range(int(listLength/2), listLength+1)]+[x for x in range(1, int(listLength/2))]
        # self.drawRect(-1,50, 50)

        # almost sorted array
        # i = random.randint(0,int(listLength/2))
        # j = random.randint(1+int(listLength/2),listLength)
        # temp=self.list[i]
        # self.list[i]=self.list[j]
        # self.list[j]=temp
        # self.drawRect(-1,50, 50)

    def drawRect(self,start, end, move):

        self.win.canvas.delete("line")
        for i in range(len(self.list)):
            color = "white"
            if i < start or i>end:
                color = "BLUE"
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

        n=len(self.list)
        swapped=True
        start = 0
        end = n-1
        while (swapped==True):
            swapped = False
            for i in range(start,end):
                self.time+=1
                if self.list[i] > self.list[i+1]:
                    temp = self.list[i]
                    self.list[i] = self.list[i+1]
                    self.list[i+1] = temp
                    swapped=True
                    self.drawRect(start, end, i+1)
            if (swapped==False):
                break
            swapped=False
            end = end-1
            self.drawRect(start, end, end-1)
            for j in range (end-1, start-1, -1):
                self.time+=1
                if self.list[j] > self.list[j+1]:
                    temp = self.list[j]
                    self.list[j] = self.list[j+1]
                    self.list[j+1] = temp
                    swapped=True
                    self.drawRect(start, end, j)
            start = start+1
        self.drawRect(50, -1, -1)
                
                


class SortWin():
    def __init__(self):
        self.win = Tk()
        self.win.title("Cocktail Sort")  # Set a title

        self.canvas = Canvas(self.win, bg="white", width=width, height=height)
        self.canvas.pack()

        self.frame = Frame(self.win)
        self.frame.pack()
        self.label = Label(self.frame, text="Cocktail Sort")
        self.label.pack(side=LEFT)
        self.btStep1 = Button(self.frame, text="Begin", command=self.begin)
        self.btStep1.pack(side=LEFT)
        self.btStep2 = Button(self.frame, text="Reset", command=self.reset)
        self.btStep2.pack(side=LEFT)


    def begin(self):
        self.cocktailSort.sort()

    def reset(self):
        self.cocktailSort.reset()

    def show(self):
        self.cocktailSort = CocktailSort(self)
        self.win.mainloop()

main = SortWin()
main.show()
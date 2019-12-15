from tkinter import *
import time
import random
import math
listLength = 50
height = 600
width = 800
time = 0

class MergeSort():
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
        self.drawRect(-1,-1,-1)

        # reversed array 
        # self.list = [x for x in range(listLength, 0, -1)]
        # self.drawRect(-1,-1,-1)

        # rotated array
        # self.list = [x for x in range(int(listLength/2), listLength+1)]+[x for x in range(1, int(listLength/2))]
        # self.drawRect(-1,-1,-1)

        # almost sorted array
        # i = random.randint(0,int(listLength/2))
        # j = random.randint(1+int(listLength/2),listLength)
        # temp=self.list[i]
        # self.list[i]=self.list[j]
        # self.list[j]=temp
        # self.drawRect(-1,-1,-1)

    def drawRect(self,l,r, flag):

        self.win.canvas.delete("line")
        for i in range(len(self.list)):
            color = "white"
            if i<flag:
                color = "BLUE"
            if i==l:
                color = "YELLOW"
            if i==r:
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

    def sort(self,alist,length):
        if len(alist)>1:
            mid=len(alist)//2
            left=alist[:mid]
            right=alist[mid:]
            self.time+=1
            self.sort(left,length)
            self.sort(right,length+mid)
            i=0
            j=0
            k=0
            
            while i<len(left) and j<len(right):
                self.time+=1
                self.drawRect(i+length,j+mid+length,length)
                if left[i]<=right[j]:
                    alist[k]=left[i]
                    i+=1
                else:
                    alist[k]=right[j]
                    j+=1
                k+=1
            
            while i<len(left):
                self.time+=1
                alist[k]=left[i]
                i+=1
                k+=1
                self.drawRect(i+length,-1,length)

            while j<len(right):
                self.time+=1
                alist[k]=right[j]
                j+=1
                k+=1
                self.drawRect(-1,j+length+mid,length)
            
            for i in range(0,len(alist)):
                self.list[i+length]=alist[i]
                self.drawRect(-1,-1,i+length+1)
            

class SortWin():
    def __init__(self):
        self.win = Tk()
        self.win.title("Merge Sort")  # Set a title

        self.canvas = Canvas(self.win, bg="white", width=width, height=height)
        self.canvas.pack()

        self.frame = Frame(self.win)
        self.frame.pack()
        self.label = Label(self.frame, text="Merge Sort")
        self.label.pack(side=LEFT)
        self.btStep1 = Button(self.frame, text="Begin", command=self.begin)
        self.btStep1.pack(side=LEFT)
        self.btStep2 = Button(self.frame, text="Reset", command=self.reset)
        self.btStep2.pack(side=LEFT)


    def begin(self):
        self.mergeSort.sort(self.mergeSort.list.copy(), 0)

    def reset(self):
        self.mergeSort.reset()

    def show(self):
        self.mergeSort = MergeSort(self)
        self.win.mainloop()

main = SortWin()
main.show()
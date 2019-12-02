from tkinter import *
import time

tk = Tk()
tk.title("Train Dispatcher")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas = Canvas(tk,width=1500,height=800,bd=0,highlightthickness=0,bg='black')
canvas.pack()
tk.update()

class Track:
    def __init__(self, occupiedBy = None, nextTrack = None, prevTrack = None, signal0 = None, signal1= None,
                 canvas=canvas,pos_x=0,pos_y=0):
        
        self.next = nextTrack
        self.prev = prevTrack
        self.signal0 = signal0
        self.signal1 = signal1
        self.occupiedBy = occupiedBy
        
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,10,fill='white')
        self.canvas.move(self.id,pos_x,pos_y)
        
    def occupied(self, train):
        self.occupiedBy = train
        if self.occupiedBy == None:
            canvas.itemconfig(self.id, fill='white')
        elif self.occupiedBy != None:
            canvas.itemconfig(self.id, fill='red')

    def checkOccupancy(self):
        if self.occupiedBy == None:
            canvas.itemconfig(self.id, fill='white')
        elif self.occupiedBy != None:
            canvas.itemconfig(self.id, fill='red')

class Switch(Track):
    def __init__(self, occupiedBy = None, nextTrack = None, divTrack = None, prevTrack = None, position = "N", direction = 0, signal0 = None, signal1= None,
                 canvas=canvas,pos_x=0,pos_y=0,ID=""):
        
        self.next = nextTrack
        self.prev = prevTrack
        self.div = divTrack
        self.position = position
        self.direction = direction
        self.signal0 = signal0
        self.signal1 = signal1
        self.occupiedBy = occupiedBy
        self.tag = ID

        self.canvas = canvas
        if self.direction == 0:
            self.diverging = canvas.create_polygon(0, 0, 0, 10, 100, 60, 100, 50, fill='grey')
        elif self.direction == 1:
            self.diverging = canvas.create_polygon(0, 50, 0, 60, 100, 10, 100, 0, fill='grey')
        self.straight = canvas.create_rectangle(0,0,100,10,fill='white',tags=self.tag)
        self.canvas.move(self.diverging,pos_x,pos_y)
        self.canvas.move(self.straight,pos_x,pos_y)
        canvas.tag_bind(self.tag, '<ButtonPress-1>', self.actuateSwitch) 
        
    def actuateSwitch(self,evt):
        if self.position == "N":
            self.position = "R"
            canvas.itemconfig(self.straight, fill='grey')
            canvas.itemconfig(self.diverging, fill='white')
            canvas.tag_lower(self.straight)
        elif self.position == "R":
            self.position = "N"
            canvas.itemconfig(self.straight, fill='white')
            canvas.itemconfig(self.diverging, fill='grey')
            canvas.tag_lower(self.diverging)
        return

    def occupied(self, train):
        self.occupiedBy = train
        if self.occupiedBy == None:
            if self.position == "N":
                canvas.itemconfig(self.straight, fill='white')
                canvas.itemconfig(self.diverging, fill='grey')
            elif self.position == "R":
                canvas.itemconfig(self.straight, fill='grey')
                canvas.itemconfig(self.diverging, fill='white')
        elif self.occupiedBy != None:
            if self.position == "N":
                canvas.itemconfig(self.straight, fill='red')
                canvas.itemconfig(self.diverging, fill='grey')
            elif self.position == "R":
                canvas.itemconfig(self.straight, fill='grey')
                canvas.itemconfig(self.diverging, fill='red')
            
    def checkOccupancy(self):
        if self.occupiedBy == None:
            if self.position == "N":
                canvas.itemconfig(self.straight, fill='white')
                canvas.itemconfig(self.diverging, fill='grey')
            elif self.position == "R":
                canvas.itemconfig(self.straight, fill='grey')
                canvas.itemconfig(self.diverging, fill='white')
        elif self.occupiedBy != None:
            if self.position == "N":
                canvas.itemconfig(self.straight, fill='red')
                canvas.itemconfig(self.diverging, fill='grey')
            elif self.position == "R":
                canvas.itemconfig(self.straight, fill='grey')
                canvas.itemconfig(self.diverging, fill='red')
    
class Train:
    def __init__(self,startSeg = None, direction = "East"):
        self.startSeg = startSeg
        startSeg.occupiedBy = self
        self.currentSeg = startSeg
        self.direction = direction
    def movement(self):
        if self.direction == "East":
            if isinstance(self.currentSeg, Switch) and self.currentSeg.direction == 0 and self.currentSeg.position == "R":
                self.nextSeg = self.currentSeg.div
                if self.nextSeg.signal0 == None or (self.nextSeg.signal0 != None and self.nextSeg.signal0.indication == "Clear"):
                    self.currentSeg.occupiedBy = None
                    self.currentSeg = self.nextSeg
                    self.currentSeg.occupiedBy = self
                else:
                    return
            else:
                if self.currentSeg.next != None:
                    self.nextSeg = self.currentSeg.next
                    if self.nextSeg.signal0 == None or (self.nextSeg.signal0 != None and self.nextSeg.signal0.indication == "Clear"):
                        self.currentSeg.occupiedBy = None
                        self.currentSeg = self.nextSeg
                        self.currentSeg.occupiedBy = self
                    else:
                        return
                else:
                    self.currentSeg.occupiedBy = None
        elif self.direction == "West":
            if isinstance(self.currentSeg, Switch) and self.currentSeg.direction == 1 and self.currentSeg.position == "R":
                self.nextSeg = self.currentSeg.div
                if self.nextSeg.signal1 == None or (self.nextSeg.signal1 != None and self.nextSeg.signal1.indication == "Clear"):
                    self.currentSeg.occupiedBy = None
                    self.currentSeg = self.nextSeg
                    self.currentSeg.occupiedBy = self
                else:
                    return
            else:
                if self.currentSeg.prev != None:
                    self.nextSeg = self.currentSeg.prev
                    if self.nextSeg.signal1 == None or (self.nextSeg.signal1 != None and self.nextSeg.signal1.indication == "Clear"):
                        self.currentSeg.occupiedBy = None
                        self.currentSeg = self.nextSeg
                        self.currentSeg.occupiedBy = self
                    else:
                        return          
                else:
                    self.currentSeg.occupiedBy = None

class ABS_Signal:
    def __init__(self, segment = None, direction = 0, indication = "Stop", nextSig = None,
                 canvas=canvas,pos_x=0,pos_y=0,signum=""):
        
        self.segment = segment
        self.direction = direction
        self.nextSig = nextSig
        self.indication = indication
        if self.direction == 0:
            self.segment.signal0 = self
        elif self.direction == 1:
            self.segment.signal1 = self

        self.canvas = canvas
        if self.direction == 1:
            self.head = canvas.create_oval(0,0,10,10,fill='red')
            self.post = canvas.create_polygon(10, -1, 10, 1, 20, 1, 20, -1, fill='white')
            self.canvas.move(self.head,pos_x+110,pos_y-15)
            self.canvas.move(self.post,pos_x+110,pos_y-10)
            self.signum = Label(tk, text=signum, font=("Helvetica",6))
            self.signum.place(x=pos_x+110, y=pos_y-35)
        elif self.direction == 0:
            self.head = canvas.create_oval(0,0,10,10,fill='red')
            self.post = canvas.create_polygon(0, -1, 0, 1, -10, 1, -10, -1, fill='white')
            self.canvas.move(self.head,pos_x-10,pos_y+15)
            self.canvas.move(self.post,pos_x-10,pos_y+20)
            self.signum = Label(tk, text=signum, font=("Helvetica",6))
            self.signum.place(x=pos_x-20, y=pos_y+30)

    def block_occupancy(self):
        if self.nextSig != None:
            self.status = 0
            self.currentSeg = self.segment
            self.cond = True
            while self.cond == True:
                if self.currentSeg.occupiedBy != None and self.currentSeg != self.nextSig.segment:
                    self.status = 1
                    self.cond = False
                elif self.currentSeg == self.nextSig.segment:
                    self.cond = False
                else:
                    if self.direction == 0:
                        self.nextSeg = self.currentSeg.next
                    elif self.direction == 1:
                        self.nextSeg = self.currentSeg.prev
                self.currentSeg = self.nextSeg
            if self.status == 1:
                self.indication = "Stop"
                canvas.itemconfig(self.head, fill='red')
            elif self.status == 0:
                self.indication = "Clear"
                canvas.itemconfig(self.head, fill='green')
                
class Controlled_Signal:
    def __init__(self, segment = None, direction = 0, indication = "Stop", nextSig = None, divSig = None,
                 canvas=canvas,pos_x=0,pos_y=0,signum="",tag=""):
        
        self.segment = segment
        self.direction = direction
        self.nextSig = nextSig
        self.divSig = divSig
        self.indication = indication
        self.tag = signum
        if self.direction == 0:
            self.segment.signal0 = self
        elif self.direction == 1:
            self.segment.signal1 = self

        self.canvas = canvas
        if self.direction == 1:
            self.head = canvas.create_oval(0,0,10,10,fill='red',tags=self.tag)
            self.post = canvas.create_polygon(10, -1, 10, 1, 20, 1, 20, -1, fill='white')
            self.canvas.move(self.head,pos_x+110,pos_y-15)
            self.canvas.move(self.post,pos_x+110,pos_y-10)
            self.signum = Label(tk, text=signum, font=("Helvetica",6))
            self.signum.place(x=pos_x+110, y=pos_y-35)
        elif self.direction == 0:
            self.head = canvas.create_oval(0,0,10,10,fill='red',tags=self.tag)
            self.post = canvas.create_polygon(0, -1, 0, 1, -10, 1, -10, -1, fill='white')
            self.canvas.move(self.head,pos_x-10,pos_y+15)
            self.canvas.move(self.post,pos_x-10,pos_y+20)
            self.signum = Label(tk, text=signum, font=("Helvetica",6))
            self.signum.place(x=pos_x-20, y=pos_y+30)
        canvas.tag_bind(self.tag, '<ButtonPress-1>', self.setRoute) 
        
    def block_occupancy(self):
        if self.nextSig != None:
            self.status = 0
            self.currentSeg = self.segment
            self.cond = True
            while self.cond == True:
                if isinstance(self.currentSeg, Switch) and self.direction == self.currentSeg.direction and self.currentSeg.position == "R":
                    self.nextSeg = self.segment.div
                    if self.currentSeg.occupiedBy != None and (self.currentSeg != self.nextSig.segment and self.currentSeg != self.divSig.segment):
                        self.status = 1
                        self.cond = False
                    elif self.currentSeg == self.nextSig.segment or self.currentSeg == self.divSig.segment:
                        self.cond = False
                    self.currentSeg = self.nextSeg
                else:
                    if self.direction == 0:
                        self.nextSeg = self.currentSeg.next
                    elif self.direction == 1:
                        self.nextSeg = self.currentSeg.prev
                    if self.currentSeg.occupiedBy != None and (self.currentSeg != self.nextSig.segment and self.currentSeg != self.divSig.segment):
                        self.status = 1
                        self.cond = False
                    elif self.currentSeg == self.nextSig.segment or self.currentSeg == self.divSig.segment:
                        self.cond = False
                    self.currentSeg = self.nextSeg
            if self.status == 1:
                self.indication = "Stop"
                canvas.itemconfig(self.head, fill='red')
            elif self.status == 0:
                self.indication = "Stop, Route Pending"
                canvas.itemconfig(self.head, fill='red')

    def setRoute(self,evt):
        self.indication = "Clear"
        self.canvas.itemconfig(self.head, fill='green')
        return

class End_Signal:
    def __init__(self, segment = None, direction = 0, indication = "Stop",
                 canvas=canvas,pos_x=0,pos_y=0,signum=""):

        self.segment = segment
        self.direction = direction
        self.indication = indication
        if self.direction == 0:
            self.segment.signal0 = self
        elif self.direction == 1:
            self.segment.signal1 = self

        self.canvas = canvas
        if self.direction == 1:
            self.head = canvas.create_oval(0,0,10,10,fill='red')
            self.post = canvas.create_polygon(10, -1, 10, 1, 20, 1, 20, -1, fill='white')
            self.canvas.move(self.head,pos_x+110,pos_y-15)
            self.canvas.move(self.post,pos_x+110,pos_y-10)
            self.signum = Label(tk, text=signum, font=("Helvetica",6))
            self.signum.place(x=pos_x+110, y=pos_y-35)
        elif self.direction == 0:
            self.head = canvas.create_oval(0,0,10,10,fill='red')
            self.post = canvas.create_polygon(0, -1, 0, 1, -10, 1, -10, -1, fill='white')
            self.canvas.move(self.head,pos_x-10,pos_y+15)
            self.canvas.move(self.post,pos_x-10,pos_y+20)
            self.signum = Label(tk, text=signum, font=("Helvetica",6))
            self.signum.place(x=pos_x-20, y=pos_y+30)
        
    def block_occupancy(self):
        self.status = 0
        if self.segment.occupiedBy != None:
            self.status = 1
        if self.status == 1:
            self.indication = "Stop"
            canvas.itemconfig(self.head, fill='red')
        elif self.status == 0:
            self.indication = "Clear"
            canvas.itemconfig(self.head, fill='green')
            
def globalMovement(trains,tracks,signals):
    cond = True
    while cond == True:
        num_initial = len(trains)
        num_inactive = 0
        for tr in trains:
            if tr.direction == "East" and tr.currentSeg.next != None:
                tr.movement()
            elif tr.direction == "West" and tr.currentSeg.prev != None:
                tr.movement()
            else:
                tr.movement()
                num_inactive += 1
            if num_inactive == num_initial:
                cond = False
        for sig in signals:
            sig.block_occupancy()
        for seg in tracks:
            seg.checkOccupancy()
        tk.update_idletasks()
        tk.update()
        time.sleep(1)
    tk.mainloop()



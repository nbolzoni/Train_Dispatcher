# Import tkinter for gui and time for train movement and refreshing functions.
"""
from tkinter import *
import time
"""

# Create gui interface
"""
tk = Tk()
tk.title("Train Dispatcher")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas = Canvas(tk,width=1500,height=800,bd=0,highlightthickness=0,bg='black')
canvas.pack()
tk.update()
"""

class Track:
    def __init__(): # Initialize each track segment and relevant attributes
        pass
    def occupied(): # Determines what initial display color the segment should use depending on train presence
        pass
    def checkOccupancy(self): # Refreshes the color depending on train presence
        pass
    
class Switch(Track):
    def __init__(): # Initialize each track switch segment and relevant attributes
        pass
    def actuateSwitch(): # Changes the switch position to "normal" or "diverging" if user clicks the switch
        pass
    def occupied(): # Determines what initial display color the segment should use depending on train presence
        pass
    def checkOccupancy(): # Refreshes the color depending on train presence
        pass
    
class Train:
    def __init__(): # Initialize each train and its relevant attributes
        pass
    def movement(): # Determines how the train "moves" from east to west or west to east based on signal status and switch position
        pass

class ABS_Signal:
    def __init__(): # Initialize each track automatic signal and relevant attributes
        pass
    def block_occupancy(): # Checks if track is clear to the next signal and grants clearance to proceed if so
        pass
                
class Controlled_Signal:
    def __init__(): # Initialize each "manually" controlled signal and relevant attributes
        pass
    def block_occupancy(): # Checks if track is clear to the next signal also considering switch position, does not grant automatic clearance
        pass
    def setRoute(): # Grants manual clearance for train movement through switches and protected track
        pass
    
class End_Signal: 
    def __init__(): # Initialize each track automatic signal at boundary of route and relevant attributes
        pass
    def block_occupancy(): # Checks if the end segment is clear and grants clearance to proceed if so
        pass
            
def globalMovement(): # Runs the functions above by taking the input of lists of trains, tracks, and signals and refreshing the GUI every second
    pass



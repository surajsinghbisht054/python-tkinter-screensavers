#!/usr/bin/python

# ---------------- READ ME ---------------------------------------------
# This Script is Created Only For Practise And Educational Purpose Only
# This is an Example Of Tkinter Canvas Graphics
# This Script Is Created For http://bitforestinfo.blogspot.in
# This Script is Written By
#
#
##################################################
######## Please Don't Remove Author Name #########
############### Thanks ###########################
##################################################
#
#
__author__='''

######################################################
                By S.S.B Group                          
######################################################

    Suraj Singh
    Admin
    S.S.B Group
    surajsinghbisht054@gmail.com
    http://bitforestinfo.blogspot.in/

    Note: We Feel Proud To Be Indian
######################################################
'''
print __author__


# ============ CONFIGURATIONS =====================
SCREENSAVER_BACKGROUND_COLOR="black"
TRANSPARENCY_LEVEL = 0.75
COLOR_CHOICE = ['blue',"red","yellow","white","skyblue","green"]
SCREEN_SAVER_CLOSING_EVENTS = ['<Any-KeyPress>', '<Any-Button>', '<Motion>']
PIPE_WIDTH = 10
WAITING_TIME_LAP = 0.09
RESTARTING_POINT = 100
LOOK_LIKE_THREAD = True
# =================================================

# *************** Importing Module ****************
try:
    import Tkinter
    import random
    import time
except:
    import tkinter as Tkinter
    import random
    import time


# Create Canvas Class
class Pipes(Tkinter.Canvas):
    def __init__(self, *args, **kwargs):
        Tkinter.Canvas.__init__(self, *args, **kwargs)
        # Starting Coordinates
        self.coordinates=[0,0,0,0]
        # Create Line Function
        self.create_pipe()

    # Create A Line
    def create_pipe(self):
        self.p = self.create_line(0,0,0,0, fill=random.choice(COLOR_CHOICE),smooth=LOOK_LIKE_THREAD ,width=PIPE_WIDTH)
        return

    # update Canvas Configurations
    def update_screen(self):
        self.coordinates.append(random.randint(0,self.winfo_screenwidth()))
        self.coordinates.append(random.randint(0,self.winfo_screenheight()))
        self.coords(self.p, *self.coordinates)
        time.sleep(WAITING_TIME_LAP)
        if len(self.coordinates)>RESTARTING_POINT:
            self.coordinates=[0,0,0,0]
            color = random.choice(COLOR_CHOICE)
            self.itemconfigure(self.p, fill=color)
        return

# Main Functions
def main():
    root=Tkinter.Tk(className="Pipes screenSaver By Bitforestinfo")
    screen = Pipes(root, bg=SCREENSAVER_BACKGROUND_COLOR)
    screen.pack(expand="yes",fill="both")
    # Tkinter Window Configurations
    root.wait_visibility(screen)
    root.wm_attributes('-alpha',TRANSPARENCY_LEVEL)
    root.wm_attributes("-topmost", True)
    root.overrideredirect(1)
    root.attributes('-fullscreen', True)
    # Window Exit Functions
    def out(event):
        root.destroy()
        return
    # Event Bindings
    for seq in SCREEN_SAVER_CLOSING_EVENTS:
        root.bind_all(seq, out)

    # Update Loop
    while True:
        root.update()
        root.update_idletasks()
        screen.update_screen()
    return


#============ Trigger ========================  
if __name__=='__main__':
    main()

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
NUMBER_OF_STARS = 80
RADIUS = 10
STAR_COLOR = "white"
UNIVERS_COLOR = "black"
TRANSPARENCY_LEVEL = 1
SCREEN_SAVER_CLOSING_EVENTS = ['<Any-KeyPress>', '<Any-Button>']

SPEED_GEARS = [i/10.0 for i in range(-10,-2)]+[i/10.0 for i in range(2,10)]

# =====================================================

# import module
import Tkinter
import time
import random


# Canvas class
class Sky(Tkinter.Canvas):
	def __init__(self, *args, **kwargs):
		Tkinter.Canvas.__init__(self, *args, **kwargs)
		self.stars=[]
		self.create_stars()

		# Function For Creating Stars
	def create_stars(self):
		for i in range(NUMBER_OF_STARS):
			self.stars.append(Stars(self))
		return

		# Function For Updating Stars Coordinates
	def update_screen(self):
		for i in self.stars:
			i.update()
		return
# 
#
# Stars Class Object
class Stars:
	def __init__(self, parent):
		self.parent = parent
		self.moving_start()
		self.create_small_circle()
	
	# Setup Stars Functions	
	def moving_start(self):
		self.x1 = self.parent.winfo_width()/2
		self.y1 = self.parent.winfo_height()/2
		self.velocity_x = random.choice(SPEED_GEARS)
		self.velocity_y = random.choice(SPEED_GEARS)
		return

	# Move Circle
	def moving_stop(self):
		self.parent.coords(self.star, self.x1,self.y1,self.x1+RADIUS,self.y1+RADIUS)
		self.moving_start()
		return

	# Create Small Circle
	def create_small_circle(self):
		x1=self.x1#self.parent.winfo_screenwidth()/2
		y1=self.y1#self.parent.winfo_screenheight()/2
		x2,y2=x1+RADIUS, y1+RADIUS
		self.star = self.parent.create_oval(x1,y1,x2,y2, fill=STAR_COLOR)
		return

	# update circle coordinates
	def update(self):
		self.parent.move(self.star, self.velocity_x, self.velocity_y)
		x,y = self.parent.coords(self.star)[:2]
		if x<0 or x>1500:
			self.moving_stop()
		elif y<0 or y>1000:
			self.moving_stop()
		return

# main function
def main():
	# create window object
	root=Tkinter.Tk()
	# create canvas 
	screen = Sky(root,bg=UNIVERS_COLOR)
	screen.pack(expand="yes",fill="both")

	# Tkinter Window Configurations
	root.wait_visibility(screen)
	root.wm_attributes('-alpha',TRANSPARENCY_LEVEL)
	root.wm_attributes("-topmost", True)
	root.overrideredirect(1)
	root.attributes('-fullscreen', True)
    # Window Exit Functions

    # Windows Destroy Function
	def out(event):
		root.destroy()
		return

    # Event Bindings
	for seq in SCREEN_SAVER_CLOSING_EVENTS:
		root.bind_all(seq, out)

	while True:
		root.update()
		root.update_idletasks()
		screen.update_screen()

# main trigger function
if __name__ == '__main__':
	main()
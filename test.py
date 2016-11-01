import tkinter as tk
import winsound

root = tk.Tk()

#background pokemon image
background_image = tk.PhotoImage(file = 'Pokemon-banner.gif')

#class for home window
class PyKeMon(tk.Frame):

	Home = tk.Label()

	#default constructor
	def __init__ (self, master=None):
	    tk.Frame.__init__(self,master)
	    self.grid()
	    self.createWidgets()

	#create all initial widgets, background image, theme song
	def createWidgets(self):
		self.background_label = tk.Label(root, image=background_image)
		self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
		self.Home.grid(row=1, column=1, sticky = 'W')

		winsound.PlaySound('Pokemon',winsound.SND_ASYNC)

PyKeMon = PyKeMon(root)
root.wm_title("Welcome to PyKeMon!")
root.geometry("1000x800")

root.mainloop()
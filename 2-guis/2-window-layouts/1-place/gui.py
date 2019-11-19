from tkinter import *

class Gui(Tk):

  # initialise window
  def __init__(self):
    super().__init__()

    # set window attributes
    self.configure(bg="#eee",
                   height=250, 
                   width=500)
    self.title("Newsletter")
      
    self.add_heading_label()
    self.add_subheader()


  def add_heading_label(self):
    # create   
    self.heading_label = Label()
    self.heading_label.place(x=0, y=0)
    
    # style
    self.heading_label.configure(font="Arial 24",
                                 text="RECEIVE OUR NEWSLETTER")

  def add_subheader(self):
    # create
    self.subheader = Subheader()
    self.subheader.place(x=1, y=1)
    
    # style
    self.subheader.configure(font="Arial 12",
                             text="Please enter your email below to receive our newsletter.")
   

    # add window components by

    # ...assigning any event handlers to the component

  # handle events
  # (callback functions to handle events will go here)
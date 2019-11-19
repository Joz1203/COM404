from tkinter import *
from tkinter import messagebox

class Gui(Tk):
    
    def __init__(self):
        super().__init__()
        
        # set window attributes
        self.title("Tickets")
        self.configure(padx=50, pady=50)
        
        # add components
        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_tickets_entry()
        self.__add_buy_button()
        
    def __add_heading_label(self):
        self.heading_label = Label()
        self.heading_label.grid(row=0, column=0, columnspan=2)
        self.heading_label.configure(   font="Arial 18",
                                        text="Entrance Ticket")

    def __add_instruction_label(self):
        self.instruction_label = Label()
        self.instruction_label.grid(row=1, column=0, columnspan=2, sticky=W)
        self.instruction_label.configure(   font="Arial 12",
                                            text="How many tickets are needed?")
        
    def __add_tickets_entry(self):
        self.tickets_entry = Entry()
        self.tickets_entry.grid(row=2, column=0, columnspan=2)
        self.tickets_entry.configure(width=40)
        
    def __add_buy_button(self):
        self.buy_button = Button()
        self.buy_button.grid(row=3, column=0, columnspan=2, sticky=N+E+S+W)
        self.buy_button.configure(text="Buy")

# events
        self.buy_button.bind("<ButtonRelease-1>", self.__buy_button_clicked)
        
    def __buy_button_clicked(self, event):
        number_tickets = int(self.tickets_entry.get())

        if number_tickets == 1: 
            messagebox.showinfo("Purchased!", "You have purchased 1 ticket!")
        elif number_tickets > 1 and number_tickets <= 9:
            messagebox.showinfo("Purchased!", "You have purchased "+ str(number_tickets)+ " tickets!")
        else: 
            messagebox.showinfo("Error!", "You have entered an invalid number of tickets!")
            
            
#importing the important stuff


import tkinter as tk
import tkinter.font as font
from functools import partial
from tkinter import messagebox
from tkinter import ttk

def main():
    #creates the window
    window = tk.Tk()
    window.geometry('700x800')
    window.title('Toub Game')

    #mainloop for the window
    window.mainloop()

    #fonts 
    font1 = font.Font('Title', font = (24, 'Arial'))
    font2 = font.Font('Game', Font = (18, 'Arial'))

if __name__ == "__main__":
    main()




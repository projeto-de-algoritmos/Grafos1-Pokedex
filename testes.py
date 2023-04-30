from tkinter import *
 
# create a root window.
top = Tk()
 
# create listbox object
listbox = Listbox(top, height = 10,
                  width = 15,
                  bg = "grey",
                  activestyle = 'dotbox',
                  font = "Helvetica",
                  fg = "yellow")
 
# Define the size of the window.
top.geometry("300x250") 
 
# Define a label for the list. 
label = Label(top, text = " FOOD ITEMS")
 
# insert elements by their
# index and names.
listbox.insert(1, "Nachos")
listbox.insert(2, "Sandwich")
listbox.insert(3, "Burger")
listbox.insert(4, "Pizza")
listbox.insert(5, "Burrito")
 
# pack the widgets
label.pack()
listbox.pack()
 
 
# Display until User
# exits themselves.
top.mainloop()

'''def teste():
    entry1 = Entry(janela) 
    janela.create_window(200, 140, window=entry1)
    print(entry1)

janela = Tk()
janela.title("Pokedex customizada!")
texto = Label(janela, text="Bem vindo a pokedex customizada!!")
texto.grid(column=0, row=0, padx=10, pady=10)

janela.geometry('400x400')
  
botao1 = Button(janela, text="Inserir", command=teste)
botao1.grid(column=0, row=1, padx=10, pady=10)

botao2 = Button(janela, text="Sair", command=exit)
botao2.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()'''

'''import tkinter as tk


if __name__ == '__main__':

   '''

'''import tkinter as tk
from tkinter.ttk import *

class Passwordchecker(tk.Frame):
   def __init__(self, parent):
       tk.Frame.__init__(self, parent)
       self.parent = parent
       self.initialize_user_interface()

   def initialize_user_interface(self):
       self.parent.geometry("400x400")
       self.parent.title("Pokeirmanos")
       self.entry=tk.Entry(self.parent)
       self.entry.pack()
       self.button=tk.Button(self.parent,text="testa", command=self.PassCheck)
       self.button.pack()
       self.label=tk.Label(self.parent,text="Fala um pokemon ae")
       self.label.pack()

   def PassCheck(self):
       password = self.entry.get()
       if len(password)>=9 and len(password)<=12:
          self.label.config(text="Acertou miseravi")
       else:
          self.label.config(text="ERRROOUUU")
 
# creates a Tk() object
master = tk.Tk()
 
# sets the geometry of main
# root window
master.geometry("200x200")
 
 
# function to open a new window
# on a button click
def openNewWindow():
     
    # Toplevel object which will
    # be treated as a new window
    #newWindow = tk.Toplevel(master)
    root = tk.Tk()
    run = Passwordchecker(root)
    root.mainloop()
 
 
label = Label(master,
              text ="This is the main window")
 
label.pack(pady = 10)
 
# a button widget which will open a
# new window on button click
btn = Button(master,
             text ="Click to open a new window",
             command = openNewWindow)
btn.pack(pady = 10)
 
# mainloop, runs infinitely
tk.mainloop()'''
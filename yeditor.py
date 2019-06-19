#!/usr/bin/python3

#save file
def savefile():
    filename = filedialog.asksaveasfilename()
    text_file = text.get(0.0,'end')
    f = open(filename,'w')
    f.write(text_file)

#open file
def openfile():
    filename = filedialog.askopenfile()
    filename = filename.name
    f = open(filename,'r')
    text_file = f.read()
    text.insert(0.0,text_file)

#new window
def newwindow():
    system('python3 /yeditor.py')
    
from os import system
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

#create page
root = tk.Tk()
root.geometry('900x500')
root.title('YEditor')

#create text eitor
text = tk.Text(root,width=59,height=28,wrap='word',bg='black',fg='blue',font=('Tahoma','18'))
text.grid(row=0,column=0)

#create scrollbar
scrollbar = ttk.Scrollbar(root,orient='vertical',command=text.yview)
scrollbar.grid(row=0,column=1,sticky='ns')
text.config(yscrollcommand=scrollbar.set)

#create menu
menubar = tk.Menu(root,bg='black',fg='blue')
root.config(menu=menubar)

file_menu = tk.Menu(menubar)
edit_menu = tk.Menu(menubar)
view_menu = tk.Menu(menubar)
options_menu = tk.Menu(menubar)

menubar.add_cascade(label='File',menu=file_menu)
menubar.add_cascade(label='Edit',menu=edit_menu)
menubar.add_cascade(label='View',menu=view_menu)
menubar.add_cascade(label='Options',menu=options_menu)

#file menu
file_menu.add_command(label='Save file',command=savefile)
file_menu.add_command(label='Open file',command=openfile)
file_menu.add_command(label='New window',command=newwindow)

root.mainloop()
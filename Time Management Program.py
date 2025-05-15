import tkinter as tk 
from tkinter import *
from tkinter import ttk
root = tk.Tk()
root.geometry("1000x500")
newFile = ""
month = ["January", "Febuary", "March" , "April", "May", "June", "July", "August", "September","October", "November", "December"]
dayButtons = []
tasks = ["coaching cycles","collaborative planning","professional learning", "instructional leadership/learning walks", "testing/data", "other duties"]
entries = []
def Days_Num():
    global month
    global selected_month
    selected_month = cb.get()
    if selected_month in ["January", "March" , "May" , "July" , "August" , "October" , "December"]:
        day = 31
    elif selected_month in ["April" , "June" , "September" , "November"]:
        day = 30
    else:
        day = 28
    return day

#Calendar Page
def Screen1():
    global selected_month
    selected_month = cb.get()
    global newFile
    rows = 5
    columns = 7 
    for b in dayButtons:
        b.grid_forget()
    for i in range(rows):
        for j in range(columns):
            date = i*7+j+1 
            if date > Days_Num():
                break
            else:
                button = tk.Button(screen1, text =f"{date}", font = ("Arial", 20), command=switch)
                dayButtons.append(button)
                button.grid(row=i, column=j, padx=5, pady=5, sticky="nsew")
    for i in range(rows):
       root.grid_rowconfigure(i, weight=1)
    for j in range(columns):
      root.grid_columnconfigure(j, weight=1)
    newFile = open(f"./{selected_month}-{date}.txt", "w+")


#Day Schedule
def Screen2():
    global entries
    rows = 4
    columns = 4
    global tasks
    for i in range(rows):
        for j in range(columns):
            entries.append (ttk.Combobox(screen2,values = tasks))
            entries[i*4+j].set("Select A Task")
            entries[i*4+j].grid(row=i, column=j, padx=5, pady=5, sticky="nsew")
    backbutton = tk.Button (screen2, text= "Back", command = switch2)
    savebutton = tk.Button (screen2, text= "Save", command = SaveEntries)
    backbutton.grid(row= 5, column= 0)
    savebutton.grid(row = 5, column = 3)
    for i in range(rows):
       root.grid_rowconfigure(i, weight=1)
    for j in range(columns):
      root.grid_columnconfigure(j, weight=1)

def SaveEntries():
    global newFile
    global entries
    for item in entries:
       newFile.write(str(item.get()) + '\n')
    newFile.flush()

def FileCreator():
    global newFile
    global month
    global selected_month
    selected_month = cb.get()






# make an input box that appends into task list which is called into dropdowns



#Page Switching Code
#functions to unload the current screen and switch to a new one
def switch():
    screen2.pack_forget()
    Screen2()
    screen1.pack_forget()
    screen2.pack()
def switch2():
    screen1.pack_forget()
    Screen1()
    screen2.pack_forget()
    screen1.pack()

def date_selection():
    lbl.config(text=cb.get())

# Combobox       
cb = ttk.Combobox(root, values=month)
cb.set("Select a month")
cb.pack()
selected_month = cb.get()

# Button to display selection  
Button(root, text="Show Selection", command=switch2).pack()
# Label to show selected value  
lbl = Label(root, text=" ")
lbl.pack()
#root window
#each of these Frames are completely blank screens
#we can develop them separately and switch between the two as needed
screen1 = tk.Frame(root)
#Time table page 
screen2 = tk.Frame(root)

#Calls the functions, starts them working on their respective pages
# Screen1() 
# Screen2() 
Days_Num()
#Call switch two to build the first page and load it
root.mainloop() 
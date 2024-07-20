from tkinter import *

#window
window = Tk()
window.title("Tkinter Python")
window.minsize(width=600,height=600)

#label
label = Label(text="my label")
label.config(bg="purple")
label.config(fg="white")
label.config(padx=10,pady=10) #buyutme
label.pack()


def button_clicked():
    #print("clicked")
    print(text.get("1.0",END)) #TEXT İCİN İNDEX İSTER 

#button
button = Button(text="button",command=button_clicked)
button.config(padx=10,pady=10)
button.pack()

#entry
entry = Entry(width=20)
entry.pack()

#multitext
text = Text(width=30,height=10)
text.pack()
text.focus() #odaklamak icin

#scale
def scale_selected(value):
    print(value) # we dont need 'get'
scale = Scale(from_=0,to=50,command=scale_selected)
scale.pack()

#spinbox
def spinbox_selected():
    print(spinbox.get())
spinbox = Spinbox(from_=0,to=50,width=20,command=spinbox_selected)
spinbox.pack()

#checkbutton
def checkbutton_selected():
    print(check_state.get())

check_state = IntVar()
checkbutton = Checkbutton(text="check",variable=check_state,command=checkbutton_selected) #check_state önceden tanımlanmış olmalı
checkbutton.pack()

#radio button
def radio_selected():
    print(radio_checked_state.get())

radio_checked_state = IntVar()
radio_button = Radiobutton(text="1. option",value=10,variable=radio_checked_state,command=radio_selected)
radio_button2 = Radiobutton(text="2. option",value=20,variable=radio_checked_state,command=radio_selected)
radio_button.pack()
radio_button2.pack()

#listbox
def listbox_selected(event):
    print(listbox.get(listbox.curselection())) #guncel ne secildiyse onu verecek
listbox = Listbox() # there is no' command= 'direct
namelist = ["Nilay", "ABC", "KFJ" , "hskFSJ"]
for i in range(len(namelist)):
    listbox.insert(i,namelist[i])
listbox.bind('<<ListboxSelect>>',listbox_selected) # for connect
listbox.pack()

window.mainloop()
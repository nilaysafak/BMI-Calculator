import tkinter


#window
window = tkinter.Tk()
window.title("Python Tkinter")
window.minsize(width=450,height=350)

#label
my_label = tkinter.Label(text="This is my label" , font=('Arial', 20 , 'italic'))
my_label.pack() #or .place(x=0,y=0) the best choice
#my_label.config(text="this is not my label") bu labeli değiştirmek ve güncellemek içindir
#my_label.grid(row=0,column=0)
def click_button():
    click = my_entry.get()
    print(click)

#button 
my_button = tkinter.Button(text="This is button", command=click_button) #commandın fonksiyonu yukarda oluşturulmuş olmalı
my_button.pack() # or .place(x=225-63, y=150-14)
#my_button.grid(row=1,column=1)
#entry
my_entry = tkinter.Entry(width=20)
my_entry.pack() #or .place()
#my_entry.grid(row=2,column=2)
window.mainloop()
 #flaticons.com
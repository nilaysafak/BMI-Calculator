from tkinter import *

#window

window = Tk()
window.title("BMI Calculator")
window.minsize(width=300,height=300)


#weight

label = Label(text="Enter You Weight (kg)")
entry = Entry(width=20)
label.config(padx=7,pady=7)
label.pack()
entry.pack()


#height

label2 = Label(text="Enter Your Height (cm)")
entry2 = Entry(width=20)

label2.pack()
entry2.pack()



sonuc = -1  #We are using an invalid BMI value as the initial value.

def button_clicked():
    try:
        global sonuc
        x=float(entry.get())
        y=float(entry2.get())
        sonuc = x / (y / 100)**2
        label_sonuc.config(text=f"BMI: {sonuc:.2f}")
    except ValueError:
        label_sonuc.config(text="Please enter a valid number.")
    

#button

button = Button(text="Calculate",command=button_clicked)
button.pack()

#sonuc
label_sonuc = Label(text="")
label_sonuc.pack()



def tanimlama():
    if sonuc == -1:
        label_tanim.config(text="No calculation has been made yet. ")
        return 
    
    if 0 < sonuc < 18.5:
        label_tanim.config(text="You are underweight")
    elif 18.5 <= sonuc <= 24.9:
        label_tanim.config(text="You are normal weight")
    elif 25 <= sonuc <= 29.9:
        label_tanim.config(text="You are overweight")
    elif 30 <= sonuc <= 34.9:
        label_tanim.config(text="Obesity (class 1)")
    elif 35 <= sonuc <= 39.9:
        label_tanim.config(text="Obesity (class 2)")
    elif sonuc >= 40:
        label_tanim.config(text="Extreme Obesity")


tanimla_buton = Button(text="Define Status",command=tanimlama)
tanimla_buton.pack()

label_tanim = Label(text="")
label_tanim.pack()



window.mainloop()
from tkinter import *

#window
mwindow = Tk()
mwindow.title('Weight Converter')
mwindow.configure(bg="light green")

#function for conversion
def conv():
    
    pound = float(val.get())*2.20462
    ounce = float(val.get())*35.274
    grams = float(val.get())*1000 
    pr1.delete(1.0, END)
    pr1.insert(END, pound)
    pr2.delete(1.0, END)
    pr2.insert(END, ounce)
    pr3.delete(1.0, END)
    pr3.insert(END,grams)

#part1
show1 = Label(mwindow, text='Weight in kilograms:',bg="light green")
show1.grid(row=0,column=0)

val = StringVar()
u_in = Entry(mwindow,fg="black" , bg="white", width=15,textvariable=val)
u_in.grid(row=0,column=1)

convbutton = Button(mwindow, text='Convert',fg='white',bg='black',width=6, command =conv)
convbutton.grid(row=1,column=1)

#part2
pd = Label(mwindow, text='Pounds',bg="light green")
pd.grid(row=3,column=0)
pr1 = Text(mwindow, height = 1, width=20,fg="dark blue",bg="grey")
pr1.grid(row=3,column=1)
oc = Label(mwindow, text='Ounce',bg="light green")
oc.grid(row=4,column=0)
pr2 = Text(mwindow, height = 1, width=20,fg="dark blue",bg="grey")
pr2.grid(row=4,column=1)
gr = Label(mwindow, text='Grams',bg="light green")
gr.grid(row=2,column=0)
pr3 = Text(mwindow, height = 1, width=20,fg="dark blue",bg="grey")
pr3.grid(row=2,column=1)
mwindow.mainloop()
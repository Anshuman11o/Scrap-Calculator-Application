from tkinter import *

window=Tk()
window.title("Ferrum sheet circle and scrap calculator")
window.geometry("350x200")
window.configure(bg="green")

constant =304.8

def calculator():
    width_of_sheet =float(e1.get())*constant
    length_of_sheet =float(e2.get())*constant
    area_of_sheet =float(width_of_sheet*length_of_sheet)
    side_of_square=float(e3.get()) + float(e4.get())
    area_of_square =float(pow(side_of_square,2))
    number_of_squares =int((area_of_sheet/area_of_square))
    t4.delete("1.0", END)
    t4.insert(END,number_of_squares)
    
    radius_of_circle =float(e3.get())*0.1
    area_of_circle =float(pow(radius_of_circle/2,2)*(22/7))
    new_area_of_square =float(pow(side_of_square*0.1,2))
    scrap_area =float(new_area_of_square) - float(area_of_circle)
    t2.delete("1.0", END)
    t2.insert(END,scrap_area)

    new_area_of_sheet =float(width_of_sheet*0.1)*float(length_of_sheet*0.1)
    scrap_percentage =float(scrap_area/new_area_of_sheet)*100
    t3.delete("1.0", END)
    t3.insert(END,scrap_percentage)



l1 = Label(window,text ="Sheet width (in feet)=", bg="green")
l1.grid(row=0, column=0)

e1_value=StringVar()
e1 = Entry(window,textvariable = e1_value)
e1.grid(row=0, column=1)

l2 = Label(window,text ="Sheet length (in feet)=", bg="green")
l2.grid(row=1, column=0)

e2_value=StringVar()
e2 = Entry(window,textvariable = e2_value)
e2.grid(row=1, column=1)

l3 = Label(window,text ="Cricle diameter (in mm)=", bg="green")
l3.grid(row=2, column=0)

e3_value=StringVar()
e3 = Entry(window,textvariable = e3_value)
e3.grid(row=2, column=1)

l4 = Label(window,text ="Space (in mm)=", bg="green")
l4.grid(row=3, column=0)

e4_value=StringVar()
e4 = Entry(window,textvariable = e4_value)
e4.grid(row=3, column=1)

b1 = Button(window, text= "Calculate", command= calculator, bg="yellow")
b1.grid(row=4,column=1)

l5 = Label(window,text ="Scrap area (in cm square)=", bg="green")
l5.grid(row=5, column=0)

l5 = Label(window,text ="Scrap Percentage =", bg="green")
l5.grid(row=6, column=0)

t2=Text(window,height=1,width=20)
t2.grid(row=5,column=1)

t3=Text(window,height=1,width=20)
t3.grid(row=6,column=1)

l6 = Label(window,text ="Number of circles formed =", bg="green")
l6.grid(row=7, column=0)

t4=Text(window,height=1,width=20)
t4.grid(row=7,column=1)


window.mainloop()
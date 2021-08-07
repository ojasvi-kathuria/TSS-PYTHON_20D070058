from tkinter import *

expression= ""

def clear():
    global expression 
    expression = " "
    equation.set(" ")

  

def pressequal():

    try:
        
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = " "

    except:
        equation.set("error")
        expression = " "
        
   

def press(key):

    global expression
    expression += str(key)
    equation.set(expression)

#main window

root = Tk()
root.title("My Calculator")
root.geometry("350x250")
root.configure(bg='light blue')

#create buttons and entry
equation= StringVar()

lbl = Label(root, text='enter value')
lbl.grid(row=1)
expression_box= Entry(root, textvariable=equation).grid(row=1, column= 2, columnspan=5)



button1= Button(root, text ='1', bg= 'light green', fg= 'black', command=lambda: press(1), height = 2, width =7)
button1.grid(row=2, column=1)

button2= Button(root, text ='2', bg= 'light green', fg= 'black', command=lambda: press(2), height = 2, width =7)
button2.grid(row=2, column=2)

button3= Button(root, text ='3', bg= 'light green', fg= 'black', command=lambda: press(3), height = 2, width =7)
button3.grid(row=2, column=3)

button4= Button(root, text ='4', bg= 'light green', fg= 'black', command=lambda: press(4), height = 2, width =7)
button4.grid(row=3, column=1)

button5= Button(root, text ='5', bg= 'light green', fg= 'black', command=lambda: press(5), height = 2, width =7)
button5.grid(row=3, column=2)

button6= Button(root, text ='6', bg= 'light green', fg= 'black', command=lambda: press(6), height = 2, width =7)
button6.grid(row=3, column=3)

button7= Button(root, text ='7', bg= 'light green', fg= 'black', command=lambda: press(1), height = 2, width =7)
button7.grid(row=4, column=1)

button8= Button(root, text ='8', bg= 'light green', fg= 'black', command=lambda: press(8), height = 2, width =7)
button8.grid(row=4, column=2)

button9= Button(root, text ='9', bg= 'light green', fg= 'black', command=lambda: press(9), height = 2, width =7)
button9.grid(row=4, column=3)

button0= Button(root, text ='0', bg= 'light green', fg= 'black', command=lambda: press(0), height = 2, width =7)
button0.grid(row=5, column=1)

plus= Button(root, text ='+', bg= 'light green', fg= 'black', command=lambda: press("+"), height = 2, width =7)
plus.grid(row=2, column=4)

minus= Button(root, text ='-', bg= 'light green', fg= 'black', command=lambda: press("-"), height = 2, width =7)
minus.grid(row=3, column=4)

multiply= Button(root, text ='*', bg= 'light green', fg= 'black', command=lambda: press("*"), height = 2, width =7)
multiply.grid(row=4, column=4)

divide= Button(root, text ='/', bg= 'light green', fg= 'black', command=lambda: press("/"), height = 2, width =7)
divide.grid(row=5, column=4)

point= Button(root, text ='.', bg= 'light green', fg= 'black', command=lambda: press("."), height = 2, width =7)
point.grid(row=6, column=1)

buttonclr= Button(root, text ='clear', bg= 'light green', fg= 'black', command = clear,  height = 2, width =7)
buttonclr.grid(row=5, column=2)

equals= Button(root, text ='=', bg= 'light green', fg= 'black', command= pressequal, height = 2, width =7)
equals.grid(row=5, column=3)

root.mainloop()
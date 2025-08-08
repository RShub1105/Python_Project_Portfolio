import tkinter as tk
window = tk.Tk()
window.title("Calculator")
window.geometry("300x400")

expression = ""

def press(key):
    global expression
    expression += str(key)
    input_text.set(expression)
def clear():
    global expression
    expression = ""
    input_text.set("")
def equal():
    global expression
    try:
        result=str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = "" 
    
input_text = tk.StringVar()
input_frame = tk.Entry(window,textvariable=input_text,font=('Arial',20),bd=10,insertwidth=2,width=14,borderwidth=4)
input_frame.grid(row=0,column=0,columnspan=4)
    

buttons = [
    ('7',1,0),('8',1,1),('9',1,2),('+',1,3),
    ('4',2,0),('5',2,1),('6',2,2),('-',2,3),
    ('1',3,0),('2',3,1),('3',3,2),('*',3,3),
    ('0',4,0),('C',4,1),('=',4,2),('/',4,3),
]
for (text,row,col)in buttons:
    action = lambda x = text:press(x)if x not in ['C','=']else (clear()if x=='C'else equal())
    tk.Button(window,text=text,padx=20,pady=20,font=('Arial',12),command=action).grid(row=row,column=col)
window.mainloop()
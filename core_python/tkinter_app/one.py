import tkinter as tk 
import random
root = tk.Tk()
main_frame = tk.Frame(root)
var = tk.StringVar()
ch = [ "hello world" , "HI Pyton", "Mar Java", "Mit Java", "Lut Java" ]
var.set("Hello world I am a Label")
label = tk.Label(main_frame,textvariable=var,
        bg="black",fg="white",font=("Times New Roman",24,"bold"))
label.pack()
def change_label():
    var.set(random.choice(ch))
b1 = tk.Button(main_frame,text="click",command=change_label,
        font=("Arial",15,'bold'),bg="pink",fg="red")

b1.pack()

expr = tk.StringVar()
e1 = tk.Entry(root,textvariable=expr,font=("Arial",20,'bold'),
        bg='gray',fg='white')

main_frame.pack()

button = tk.Button(root,text="!!EXIT!!",command=root.destroy,
        font=("Arial",15,'bold'),bg="pink",fg="red")
button.pack()
def slove():
    expr.set(eval(expr.get()))
result_button= tk.Button(root,text="!!Result!!",command=slove,
        font=("Arial",15,'bold'),bg="pink",fg="red")
def clear():
    expr.set("")
clr_button= tk.Button(root,text="!!clear!!",command=clear,
        font=("Arial",15,'bold'),bg="pink",fg="red")
e1.pack()
result_button.pack()
clr_button.pack(anchor='sw')
root.title("My Appliction")
root.wm_minsize(400,400)
root.wm_maxsize(500,500)
root.geometry("+500+200")
root.mainloop()

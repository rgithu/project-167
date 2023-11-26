from tkinter import *
root = Tk();
from tkinter import ttk

root.title("Canvas Basic")
root.geometry("600x600")
root.configure(background="#dfe7f0")

canvas = Canvas(root,width=600,height=500,bg="#ffffff",highlightbackground="lightgray")
canvas.pack()

label_choose_color = Label(root,text="Choose Color: ",fg="#000000",font=("Ink Free",11,"bold"))
label_choose_color.place(relx=0.1,rely=0.9,anchor=CENTER)

fillcolor = ['red','orange','yellow','green','blue','purple']

color_dropdown = ttk.Combobox(root,state='readonly',values=fillcolor,width=10)
color_dropdown.place(relx=0.26,rely=0.9,anchor=CENTER)

startx = Label(root,text="startx:",fg="#000000",font=("Ink Free",11,"bold"))
startx.place(relx=0.41,rely=0.9,anchor=CENTER)

coordinate_value = ['10','50','100','200','300','400','500','600','800','900']

startx_dropdown = ttk.Combobox(root,state='readonly',values=coordinate_value,width=10)
startx_dropdown.place(relx=0.54,rely=0.9,anchor=CENTER)

starty = Label(root,text="starty:",fg="#000000",font=("Ink Free",11,"bold"))
starty.place(relx=0.67,rely=0.9,anchor=CENTER)

starty_dropdown = ttk.Combobox(root,state='readonly',values=coordinate_value,width=10)
starty_dropdown.place(relx=0.8,rely=0.9,anchor=CENTER)

endx = Label(root,text="endx:",fg="#000000",font=("Ink Free",11,"bold"))
endx.place(relx=0.1,rely=0.95,anchor=CENTER)

endx_dropdown = ttk.Combobox(root,state='readonly',values=coordinate_value,width=10)
endx_dropdown.place(relx=0.26,rely=0.95,anchor=CENTER)

endy = Label(root,text="endy:",fg="#000000",font=("Ink Free",11,"bold"))
endy.place(relx=0.4,rely=0.95,anchor=CENTER)

endy_dropdown = ttk.Combobox(root,state='readonly',values=coordinate_value,width=10)
endy_dropdown.place(relx=0.56,rely=0.95,anchor=CENTER)

root.mainloop();
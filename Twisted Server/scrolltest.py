from tkinter import *
from tkinter import ttk

root = Tk()
l = Listbox(root, height=20)
l.grid(column=0, row=0, sticky=(N,W,E,S))
s = ttk.Scrollbar(root, orient=VERTICAL, command=l.yview)
s.grid(column=1, row=0, sticky=(N,S))
l['yscrollcommand'] = s.set
ttk.Sizegrip().grid(column=1, row=1, sticky=(S,E))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
myimg = Image.open('test.gif')
myimg = myimg.resize((100, 100), Image.ANTIALIAS)
newImg = ImageTk.PhotoImage(myimg)
content = Label(tk, image=newImg)
content.place(x=0, y=0);
for i in range(1,101):
    l.insert('end', 'Line %d of 100' % i)
root.mainloop()

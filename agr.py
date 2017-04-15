from tkinter import *
from tkinter.ttk import Treeview

root = Tk()
root.resizable(width=False, height=False)
root.maxsize(400,400)
root.minsize(400,400)

for x in range(60):
    Grid.columnconfigure(root, x, weight=1)

for y in range(30):
    Grid.rowconfigure(root, y, weight=1)


#frame= Frame(root,width=200,height=200)
#frame.pack(side=BOTTOM)
fert={'Cotton'}
conditions={'Cotton':("25°","HIGH","Black","100-200","Flat"),"Rice":("35°","HIGH","Alluvial","150","Slope"),"Wheat":("45°","LOW","Red","50cm","Flat")}
label1=Label(root,text="ENTER CROP HERE",fg="#006400")
label2=Label(root,text="FERTILIZERS")
label3=Label(root,text="HEALTHY")
label4=Label(root,text="HAZARDOUS")

entry_1 = Entry(root)
tv = Treeview(root)
lb = Listbox(root)
scrollbar = Scrollbar(root)
tv2= Treeview(root)

label1.grid(row=0,column=1)
entry_1.grid(row=1,column=1)



tv['columns'] = ('temperature', 'light', 'soil','rainfall','land')
#tv['columns'] = ('starttime', 'endtime', 'status')
tv.heading("#0", text='Crop', anchor="center")
tv.column("#0", anchor=W,width=60)
tv.heading('temperature', text='Temperature')
tv.column('temperature', anchor='center', width=95)
tv.heading('light', text='Light')
tv.column('light', anchor='center', width=65)
tv.heading('soil', text='Soil')
tv.column('soil', anchor='center', width=50)
tv.heading('rainfall', text='Rainfall')
tv.column('rainfall', anchor='center', width=75)
tv.heading('land', text='Land',anchor=W)
tv.column('land', anchor=W, width=75)
#tv.grid(row=10,column=0,sticky = (N,S,W,E))
tv.config(height=1)


#tv.tag_configure('test',background='red')
tv.grid(row=10,columnspan=3)
tv.grid_rowconfigure(10,weight=1)

label2.grid(row=13,column=1)

"""
lb.grid(row=15,column=1)
lb.config(height=10)
for i in range(100):
    lb.insert(END, i)
lb.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=lb.yview)

"""

tv2['columns'] = ('area','n','p','k')
#tv['columns'] = ('starttime', 'endtime', 'status')
tv2.heading("#0", text='Crop', anchor='center')
tv2.column("#0", anchor="center",width=80)
tv2.heading('area', text='Quantity')
tv2.column('area', anchor='center', width=80)
tv2.heading('n', text='Nitrogen')
tv2.column('n', anchor='center', width=80)
tv2.heading('p', text='Phosphorous')
tv2.column('p', anchor='center', width=80)
tv2.heading('k', text='Potassium')
tv2.column('k', anchor='center', width=80)
tv2.config(height=1)
tv2.grid(row=15,column=0,columnspan=3)
tv2.grid_rowconfigure(15,weight=1)

"""
       # self.treeview = tv
       # self.grid_rowconfigure(0, weight = 1)
       # self.grid_columnconfigure(0, weight = 1)
"""

root.grid_columnconfigure(0, weight=3)
root.grid_columnconfigure(1, weight=3)
root.grid_columnconfigure(2, weight=3)
#root.grid_rowconfigure(0,weight=4)
#root.grid_rowconfigure(1,weight=1)


def acceptr():
    if entry_1.get() in conditions.keys():
            tv.insert('', 0, text=entry_1.get(), values=conditions.get(entry_1.get()), tags=('test',))
    else:
        print("Invalid")

def clear():
    entry_1.delete(0,END)
    for i in tv.get_children():
        tv.delete(i)
    for j in tv2.get_children():
        tv2.delete(j)



button1=Button(root,text="PRINT",fg="black",command=acceptr)

button1.grid(row=2,column=0,sticky=E,columnspan=1)
button2=Button(root,text="CLEAR",fg="black",command=clear)
button2.grid(row=2,column=2,sticky=W,columnspan=1)
button1.config(width=15)
button2.config(width=15)



root.mainloop()
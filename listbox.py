def submit ():
    food= []
    for index in listbox.curselection():
        food.insert(index,listbox.get(index))
    print("You have ordered:")
    for index in food:
        print(index)
def add():
    listbox.insert(listbox.size(),entrybox.get())
    listbox.config(height=listbox.size())
def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size())

from tkinter import*
window = Tk()
listbox=Listbox(window, bg= "white", font=("arial",35), width= 10, selectmode=MULTIPLE)
listbox.pack()
listbox.insert(1,"pizza")
listbox.insert(2,"pasta")
listbox.insert(3,"garlic bread")
listbox.config(height=listbox.size())
entrybox = Entry(window)
entrybox.pack()
submitButton = Button(window, text="submit", command=submit)
submitButton.pack()
addButton=Button(window,text="add", command=add)
addButton.pack()
deleteButton=Button(window, text="delete", command=delete)
deleteButton.pack()
window.mainloop()
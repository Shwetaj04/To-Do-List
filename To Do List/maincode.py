import tkinter as tk
from tkinter import *

root=Tk()
root.title("To Do List")
root.geometry("400x650")
root.resizable(False,False)


task_list=[]

def addTask():
    task=task_entry.get()
    task_entry.delete(0,END)

    if task:
        with open("tasklist.txt",'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END,task)


def deleteTask():
    global task_list
    task=str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt",'w') as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")

        listbox.delete(ANCHOR)



def openTaskFile():
    try:
        global task_list
        with open("tasklist.txt","r") as taskfile:
            tasks= taskfile.readlines()

        for task in tasks:
            if task !="\n":
                task_list.append(task)
                listbox.insert(END,task)

    except:     
        file=open("tasklist.txt",'w')
        file.close()      



#icon
image_icon=PhotoImage(file="notepad.png")
root.iconphoto(False,image_icon)

# Create a top blue strip (Frame)
top_bar = tk.Frame(root, bg="#0B039B", height=60)
top_bar.pack(side="top", fill="x")

dockimage=PhotoImage(file="logo.png")
Label(root,image=dockimage,bg="#0B039B").place(x=10,y=25)


noteimage=PhotoImage(file="notepad.png")
Label(root,image=noteimage,bg="#0B039B").place(x=340,y=25)

heading=Label(root,text="ALL TASKS",font='arial 20 bold',fg="white",bg="#0B039B")
heading.place(x=120,y=20)

#main
frame=Frame(root,width=400,height=50,bg='white')
frame.place(x=0,y=180)

taskk=StringVar()
task_entry=Entry(frame,width=18,font="arial 20",bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()


button=Button(frame,text="ADD",font="arial 15 bold",width=6,bg="#5a95ff",fg="#fff",bd=0,command=addTask)
button.place(x=300,y=0)

#listbox
frame1=Frame(root,bd=3,width=700,height=280,bg="#0B039B")
frame1.pack(pady=(160,0))

listbox=Listbox(frame1,font=('arial',12),width=40,height=16,bg="#0B039B",fg='white',cursor="hand2",selectbackground="#5a95ff")
listbox.pack(side=LEFT ,fill=BOTH ,padx=2)
scrollbar=Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()


#delete
Delete_icon=PhotoImage(file="delete.png")
Button(root,image=Delete_icon,bd=0,command=deleteTask).pack(side=BOTTOM,pady=13)


root.mainloop()
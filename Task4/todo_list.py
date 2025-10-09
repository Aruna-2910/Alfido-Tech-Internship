import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import os
TASK_FILE = "tasks.txt"
def load_tasks():
    tasks = []
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE,"r") as f:
            for line in f:
                name,status=line.strip().split("|")[:2]
                tasks.append((name,status))
    return tasks
def save_tasks():
    with open(TASK_FILE,"w") as f:
        for name,status in tasks:
            f.write(f"{name}|{status}\n")

def add_task():
    task_name = entry.get().strip()
    if not task_name:
        messagebox.showwarning("warning", "Task cannot be empty!")
        return
    time = datetime.now().strftime("%H:%M:%p")
    tasks.append((f"{task_name}(added at {time})","Pending"))
    update_listbox()
    entry.delete(0, tk.END)
    save_tasks()
def delete_task():
    try:
        index = listbox.curselection()[0]
        del tasks[index]
        update_listbox()
        save_tasks()
    except:
        messagebox.showwarning("Warning","Please select a task to delete!")
def mark_done():
    try:
        index = listbox.curselection()[0]
        name,_ = tasks[index]
        tasks[index]= (name + "","Done")
        update_listbox()
        save_tasks()
    except:
        messagebox.showwarning("Warning","Please select a task to mark done!")
def clear_all():
        if messagebox.askyesno("Confirm","Clear all tasks"):
            tasks.clear()
            update_listbox()
            save_tasks()
            
def update_listbox():
    listbox.delete(0,tk.END)
    for name,status in tasks:
            color = "green" if status == "Done" else "black"
            listbox.insert(tk.END, name)
            listbox.itemconfig(tk.END,fg=color)
root = tk.Tk()
root.title("To-Do List App")
root.geometry("500x450")
root.config(bg="#FFC0CB")
task = load_tasks()
title = tk.Label(root,text="#f0f0f0")
tasks = load_tasks()
title = tk.Label(root,text="My To-Do List",font=("Helvetica",18,"bold"),bg="#f0f0f0",fg="#2c3e50")
title.pack(pady=10)
frame = tk.Frame(root)
frame.pack(pady=5)
entry = tk.Entry(frame,width=35,font=("Arial",12))
entry.grid(row=0,column=0,padx=5)
add_btn = tk.Button(frame,text="Add Task",width=12,command=add_task,bg="#ADD8E6")
add_btn.grid(row=0,column=1,padx=5)
listbox = tk.Listbox(root,width=60,height=15,font=("#27ae60"),fg="white")
add_btn.grid(row=0,column=1,padx=5)
listbox = tk.Listbox(root,width=60,height=15,font=("Arial",12))
listbox.pack(pady=10)
btn_frame = tk.Frame(root,bg="#f0f0f0")
btn_frame.pack()
done_btn = tk.Button(btn_frame,text="Mark Done",width=14,command=mark_done,bg="#FFA500")
done_btn.grid(row=0,column=0,padx=5,pady=5)
delete_btn = tk.Button(btn_frame,text="Delete Task",width=14,command=delete_task,bg="#c0392b",fg="white")
delete_btn.grid(row=0,column=1,padx=5,pady=5)
clear_btn = tk.Button(btn_frame,text= "Clear All",width=14 ,command=clear_all,bg="#7f8c8d",fg="white")
clear_btn.grid(row=0,column=2,padx=5,pady=5)
update_listbox()
root.mainloop()                     
                     

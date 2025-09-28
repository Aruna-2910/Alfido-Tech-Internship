import tkinter as tk
from tkinter import messagebox
import os

HISTORY_FILE = "history.txt"

def save_history(entry):
    with open(HISTORY_FILE, "a") as file:
        file.write(entry + "\n")

def show_history():
    if not os.path.exists(HISTORY_FILE):
        messagebox.showinfo("History ","No history file found")
        return
    with open(HISTORY_FILE, "r") as file:
        lines = file.readlines()
    if not lines:
        messagebox.showinfo("History","No history yet")
    else:
        history_str = "\n".join(lines)
        messagebox.showinfo("History",history_str)

def click(key):
    if key == "=":
        try:
            result = str(eval(entry.get()))
            save_history(f"{entry.get()} = {result}")
            entry.delete(0,tk.END)
            entry.insert(tk.END,result)
        except Exception as e:
            messagebox.showerror("Error",str(e))
    elif key == "C":
        entry.delete(0,tk.END)
    elif key == "H":
        show_history()
    elif key == "Q":
        root.destroy()
    else:
        entry.insert(tk.END,key)

root = tk.Tk()
root.title("Calculator")
root.geometry("280x400")
root.resizable(False,False)

entry = tk.Entry(root,width=14,font=("Arial",20),borderwidth=3,relief="sunken",justify="right")
entry.grid(row=0,column=0,columnspan=4,padx=6,pady=12)

buttons =[
    ("7",1,0),("8",1,1),("9",1,2),("/",1,3),
    ("4",2,0),("5",2,1),("6",2,2),("*",2,3),
    ("1",3,0),("2",3,1),("3",3,2),("-",3,3),
    ("0",4,0),(".",4,1),("=",4,2),("+",4,3),
    ("C",5,0),("H",5,1),("Q",5,2)
]
for (text,row,col) in buttons:
    color = "lightgreen" if text.isdigit() or text == "." else"lightblue"
    if text in ["C","=","H","Q"]:
        color = "lightcoral"
    tk.Button(root,text=text,width=4,height=2,bg=color,font=("Arial",15),
              command=lambda t=text:click(t)).grid(row=row,column=col,padx=3,pady=3)

root.mainloop()
    































        

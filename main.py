import tkinter.messagebox
from customtkinter import *
import customtkinter
import tkinter
from CTkListbox import *
import pickle

# Initializing the CustomTKinter Application
root = customtkinter.CTk()
root.geometry("400x550")
set_appearance_mode("dark")
root.title("TO DO LIST By @Ayushi")

tasklist = []

# Funcationalities Defined 
def Add_Task():
    task = Entry_task.get()
    if task !="":
        Active_Listbox_task.insert(customtkinter.END,task)
        Save_Task()
        Entry_task.delete(0,customtkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!",message="You must enter a task.")
    

def Delete_Task():
    try:
        task_index = Active_Listbox_task.curselection()
        Active_Listbox_task.delete(task_index)
        Save_Task()
    except:
        tkinter.messagebox.showwarning(title="Warning!",message="You must select a task.")

def Preview_Task():
    try:
        month = Combo_Button.get()
        tasks = pickle.load(open(f"{month}_tasks.dat","rb"))
        Active_Listbox_task.delete(0,customtkinter.END)
        for task in tasks:
            Active_Listbox_task.insert(customtkinter.END,task)
    except FileNotFoundError:
        tkinter.messagebox.showwarning(title="Warning!",message="Cannot find tasks.dat")
    
def Save_Task():
    month = Combo_Button.get()
    num_task = Active_Listbox_task.size()
    content = [Active_Listbox_task.get(i) for i in range(num_task)]
    with open(f"{month}_tasks.dat","wb") as file:
        pickle.dump(content,file)

def clicker(value):
    pass
# Create Listbox for ach month
Listboxes = []

for i in range(12):
    Listbox_task = CTkListbox(master=root,height=300,width=400,fg_color="#222222")
    Listboxes.append(Listbox_task)

# January is the active month
Active_Listbox_task = Listboxes[0]

def switch_frame(month):
    for Listbox_task in Listboxes:
        Listbox_task.pack_forget()

    index = my_values.index(month)
    Listboxes[index].pack(fill="both",expand=True)
    global Active_Listbox_task
    Active_Listbox_task = Listboxes[index]

    Preview_Task(month)

#Create GUI of file
frame = customtkinter.CTkFrame(master=root)
frame.pack()

my_values = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
Combo_Button = customtkinter.CTkComboBox(frame,values=my_values,command=clicker,fg_color="#222222")
Combo_Button.pack()

Active_Listbox_task.pack(fill="both", expand=True)

Entry_task = customtkinter.CTkEntry(master=frame,height=40,width=400,fg_color="#222222",placeholder_text="Enter a task here")
Entry_task.pack(padx=5,pady=5)

Button_Add_task = customtkinter.CTkButton(master=frame,text="Add Task",command=Add_Task,corner_radius=30,fg_color="#bc9aff",hover_color="#7b66ff")
Button_Add_task.pack()

Button_Delete_task = customtkinter.CTkButton(master=frame,text="Delete Task",command=Delete_Task,corner_radius=30,fg_color="#bc9aff",hover_color="#7b66ff")
Button_Delete_task.pack(padx=5,pady=5)

Button_Preview_task = customtkinter.CTkButton(master=frame,text="Preview Task",command=Preview_Task,corner_radius=30,fg_color="#bc9aff",hover_color="#7b66ff")
Button_Preview_task.pack(padx=5)

Button_Save_task = customtkinter.CTkButton(master=frame,text="Save Task",command=Save_Task,corner_radius=30,fg_color="#bc9aff",hover_color="#7b66ff")
Button_Save_task.pack(padx=5,pady=5)



root.mainloop()
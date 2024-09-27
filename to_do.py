import customtkinter as cstk

cstk.set_appearance_mode("light")
cstk.set_default_color_theme("dark-blue")

root = cstk.CTk()
root.title("TO DO APPLICATION")
root.configure(fg_color='navajo white') 


# The code which opens the window in the middle of the screen.
window_width = 450
window_height = 450

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (window_width / 2)
y = (screen_height / 2) - (window_height / 2)

root.geometry(f"{window_width}x{window_height}+{int(x)}+{int(y)}")
#..................................................................



###functions for buttons.
tasks = []
#This function adds a task into the list.
def add_task():
    task = entry_ent.get()  
    if task:
        tasks.append(task)
        outputer() 
        clearer()

#this function deletes the task.
def delete_task():
    for_delete_lbl = cstk.CTkLabel(master=root, text="Enter task number to delete:", font=("Arial", 15))
    for_delete_lbl.place(x=40, y=380)

    for_delete_ent = cstk.CTkEntry(master=root, width=73)
    for_delete_ent.place(x=235, y=381)

    # Store the current state of tasks
    current_tasks = tasks.copy()

    def confirm_delete():
        task_for_delete = for_delete_ent.get()
        if task_for_delete.isdigit():
            index_to_delete = int(task_for_delete) - 1  
            if 0 <= index_to_delete < len(tasks):
                tasks.pop(index_to_delete)  
                outputer()  
                clear_inputs()

    def cancel_delete():
        global tasks
        tasks = current_tasks.copy()  # Restore tasks from the temporary list
        outputer()  
        clear_inputs()

    def clear_inputs():
        for_delete_lbl.destroy()
        for_delete_ent.destroy()
        del_btn.destroy()
        cancel_btn.destroy()

    del_btn = cstk.CTkButton(master=root, text="Delete", width=20, command=confirm_delete)
    del_btn.place(x=310, y=381)

    cancel_btn = cstk.CTkButton(master=root, text="Cancel", width=20, command=cancel_delete)
    cancel_btn.place(x=362, y=381)

#This function deletes all the tasks from the list.
def delete_all_tasks():
    tasks.clear()  
    outputer() 

#this function closes the program.
def exit():
    root.destroy()
###................................................



###Additional functions. like outputer and entry clearer.
#this function outputs the list what user entered.
txt_output = cstk.CTkTextbox(root, height=200, width=220)
txt_output.place(x=200, y=150)

def outputer():
    txt_output.delete("1.0", cstk.END)  
    x = 1  
    for item in tasks:
        txt_output.insert(cstk.END, f"{x}) {item}\n")
        x += 1

#this function clears the entry where user enters tasks.
def clearer():
    entry_ent.delete(0, cstk.END)
###......................................................



# Labels and entry for tasks.
title_lbl = cstk.CTkLabel(master=root, 
                          text="The TO-DO List" "\n" "~~~~~~~~~~~~~~",
                          text_color="tan4",
                          font=("Satisfy", 40),
)
title_lbl.pack(pady=20)

ent_lbl = cstk.CTkLabel(master=root, text = "Enter the task:", font=("Arial",20))
ent_lbl.place(x = 40, y = 150)

entry_ent = cstk.CTkEntry(master=root)
entry_ent.place(x = 37, y = 175)
#...............................................................................


#Buttons
add_btn = cstk.CTkButton(master=root, text = "Add Task", command=add_task)
add_btn.place(x = 37, y = 210)

delete_btn = cstk.CTkButton(master=root, text = "Delete The Task", command=delete_task)
delete_btn.place(x = 37 , y = 245)

delete_all_btn = cstk.CTkButton(master=root, text = "Delete All Tasks", command=delete_all_tasks)
delete_all_btn.place(x = 37, y = 280)

exit_btn = cstk.CTkButton(master=root, text = "Exit Program", command=exit)
exit_btn.place(x = 37, y = 315)
#.....................................................................


root.mainloop()

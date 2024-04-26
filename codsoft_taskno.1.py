import tkinter as tk

class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")
        
        # Task list
        self.tasks = []
        
        # Entry field for task input
        self.task_entry = tk.Entry(master, width=40)
        self.task_entry.pack(pady=10)
        
        # Button to add tasks
        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.pack()
        
        # Listbox to display tasks
        self.task_listbox = tk.Listbox(master, width=40)
        self.task_listbox.pack(pady=10)
        
        # Button to delete selected task
        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()
        
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
    
    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            del self.tasks[task_index]
            self.task_listbox.delete(task_index)

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

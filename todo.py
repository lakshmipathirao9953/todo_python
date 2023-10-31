import tkinter as tk

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.tasks = []
        self.completed_tasks = []

        self.create_widgets()

    def create_widgets(self):
        self.task_entry = tk.Entry(self.root, width=40)
        self.task_entry.grid(row=0, column=0, padx=5, pady=5)

        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task,fg="red")
        self.add_button.grid(row=0, column=1, padx=5, pady=5)



        self.task_label = tk.Label(self.root, text="To-Do Tasks", font=("Arial", 12, "bold"), fg="Blue", bg="yellow")

       
        self.task_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

       

        self.task_list = tk.Listbox(self.root, width=50, height=15)
        self.task_list.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
        self.task_list.bind('<<ListboxSelect>>', self.on_task_select)

        completed_label = tk.Label(self.root, text="Completed Tasks", font=("Arial", 12, "bold"))
        completed_label.grid(row=2, column=3, padx=5, pady=5)

        self.completed_list = tk.Listbox(self.root, width=50, height=15, fg='green')
        self.completed_list.grid(row=3, column=3, padx=5, pady=5)
        self.completed_list.bind('<<ListboxSelect>>', self.on_completed_task_select)

        self.complete_button = tk.Button(self.root, text="Mark as Completed", command=self.mark_as_completed,fg="red")
        self.complete_button.grid(row=3, column=0, padx=5, pady=5)

        self.remove_button = tk.Button(self.root, text="Remove Task", command=self.remove_task,fg="red")
        self.remove_button.grid(row=3, column=1, padx=5, pady=5)

    def add_task(self):
        task_description = self.task_entry.get()
        if task_description:
            self.tasks.append(task_description)
            self.update_task_list()

    def update_task_list(self):
        self.task_list.delete(0, tk.END)
        for task in self.tasks:
            self.task_list.insert(tk.END, task)

    def mark_as_completed(self):
        selected_task_index = self.task_list.curselection()
        if selected_task_index:
            task = self.tasks.pop(selected_task_index[0])
            self.completed_tasks.append(task)
            self.update_task_list()
            self.update_completed_list()

    def remove_task(self):
        selected_task_index = self.task_list.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.update_task_list()

    def update_completed_list(self):
        self.completed_list.delete(0, tk.END)
        for task in self.completed_tasks:
            self.completed_list.insert(tk.END, task)

    def on_task_select(self, event):
        self.completed_list.selection_clear(0, tk.END)

    def on_completed_task_select(self, event):
        self.task_list.selection_clear(0, tk.END)

def main():
    root = tk.Tk()
    todo_app = ToDoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

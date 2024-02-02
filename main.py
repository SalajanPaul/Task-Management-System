from customtkinter import *
import tkinter as tk
from tkinter import ttk
from CTkMessagebox import CTkMessagebox
from tkcalendar import DateEntry


class Task:
    def __init__(self, name, priority, due_date):
        self.name = name
        self.priority = priority
        self.due_date = due_date


class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Management")

        self.tasks = []

        self.task_name_var = tk.StringVar()
        self.priority_var = tk.StringVar()
        self.due_date_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        CTkLabel(self.root, text="Task Name:").grid(row=0, column=0, sticky="w")
        task_name_entry = tk.Entry(self.root, textvariable=self.task_name_var)
        task_name_entry.grid(row=0, column=1, padx=10, pady=5)

        # Priority Label and Dropdown
        CTkLabel(self.root, text="Priority:").grid(row=1, column=0, sticky="w")
        priority_values = ["Low", "Medium", "High"]
        priority_dropdown = ttk.Combobox(self.root, textvariable=self.priority_var, values=priority_values)
        priority_dropdown.grid(row=1, column=1, padx=10, pady=5)

        # Due Date Label and Calendar
        CTkLabel(self.root, text="Due Date:").grid(row=2, column=0, sticky="w")
        due_date_entry = DateEntry(self.root, textvariable=self.due_date_var, date_pattern="yyyy-mm-dd")
        due_date_entry.grid(row=2, column=1, padx=10, pady=5)

        # Add Task Button
        add_task_button = CTkButton(self.root, text="Add task", command=self.add_task)
        add_task_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        # Task List View
        self.task_list_treeview = ttk.Treeview(self.root, columns=("Priority", "Due Date"))
        self.task_list_treeview.grid(row=4, column=0, columnspan=2, padx=10, pady=5)
        self.task_list_treeview.heading("#0", text="Task Name")
        self.task_list_treeview.heading("Priority", text="Priority")
        self.task_list_treeview.heading("Due Date", text="Due Date")

        # Clear Task Button
        clear_task_button = CTkButton(self.root, text="Clear text", command=self.delete_task)
        clear_task_button.grid(row=5, column=1, padx=10, pady=5, sticky="e")


    def add_task(self):
        name = self.task_name_var.get()
        priority = self.priority_var.get()
        due_date = self.due_date_var.get()

        if name and priority and due_date:
            task = Task(name, priority, due_date)
            self.tasks.append(task)

            self.task_list_treeview.insert("", tk.END, text=task.name, values=(task.priority, task.due_date))

            self.task_name_var.set("")
            self.priority_var.set("")
            self.due_date_var.set("")
        else:
            CTkMessagebox(title="Error", message="Please fill in all fields.", icon="cancel")

    def delete_task(self):
        selected_item = self.task_list_treeview.selection()
        if selected_item:
            task_name = self.task_list_treeview.item(selected_item)["text"]
            for task in self.tasks:
                if task.name == task_name:
                    self.tasks.remove(task)
                    self.task_list_treeview.delete(selected_item)
                    break

    def clear_task(self):
        self.task_name_var.set("")
        self.priority_var.set("")
        self.due_date_var.set("")


if __name__ == "__main__":
    root = CTk()
    app = TaskManagerApp(root)
    root.mainloop()




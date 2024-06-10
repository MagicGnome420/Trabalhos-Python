import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tarefas")
        self.tasks = []
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Digite uma tarefa:")
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=10)
        
        self.add_button = tk.Button(self.root, text="Adicionar Tarefa", command=self.add_task)
        self.add_button.pack(pady=10)
        
        self.listbox = tk.Listbox(self.root)
        self.listbox.pack(pady=10)
        
        self.remove_button = tk.Button(self.root, text="Remover Tarefa", command=self.remove_task)
        self.remove_button.pack(pady=10)

    def add_task(self):
        task = self.entry.get()
        if task != "":
            self.tasks.append(task)
            self.update_tasks_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "Digite uma tarefa.")

    def remove_task(self):
        try:
            task_index = self.listbox.curselection()[0]
            self.tasks.pop(task_index)
            self.update_tasks_listbox()
        except IndexError:
            messagebox.showwarning("Aviso", "Escolha uma tarefa para remover.")

    def update_tasks_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

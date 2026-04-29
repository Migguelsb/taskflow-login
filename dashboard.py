import customtkinter as ctk
from tasks import TaskManager

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class Dashboard(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("TaskFlow - Gerenciador")
        self.geometry("600x500")

        self.manager = TaskManager()

        self.label = ctk.CTkLabel(
            self, text=" 📋 Gerenciador de Tarefas", font=(
                "Arial", 22))
        self.label.pack(pady=10)

        self.task_entry = ctk.CTkEntry(
            self, placeholder_text="Digite uma nova tarefa...", width=300)
        self.task_entry.pack(pady=10)

        self.btn_add = ctk.CTkButton(
            self, text="Adicionar Tarefa", command=self.add_task)
        self.btn_add.pack(pady=5)

        self.tasks_frame = ctk.CTkFrame(self)
        self.tasks_frame.pack(pady=20, fill="both", expand=True)

        self.update_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.manager.add_task(task)
            self.task_entry.delete(0, "end")
            self.update_tasks()

    def delete_task(self, index):
        self.manager.tasks.pop(index)
        self.update_tasks()

    def edit_task(self, index):
        edit_window = ctk.CTkToplevel(self)
        edit_window.title("Editar tarefa")
        edit_window.geometry("300x150")

        edit_window.grab_set()

        entry = ctk.CTkEntry(edit_window, width=200)
        entry.insert(0, self.manager.tasks[index])
        entry.pack(pady=20)

        def salvar():
            novo_texto = entry.get()
            if novo_texto:
                self.manager.tasks[index] = novo_texto
                self.update_tasks()
                edit_window.destroy()

        btn_salvar = ctk.CTkButton(edit_window, text="Salvar", command=salvar)
        btn_salvar.pack(pady=10)

    def update_tasks(self):

        for widget in self.tasks_frame.winfo_children():
            widget.destroy()

        for i, task in enumerate(self.manager.get_tasks()):
            frame = ctk.CTkFrame(self.tasks_frame)
            frame.pack(pady=5, padx=10, fill="x")

            label = ctk.CTkLabel(frame, text=task, anchor="w")
            label.pack(side="left", padx=10)

            btn_edit = ctk.CTkButton(frame, text=" ✏️ Editar", width=70,
                                     command=lambda i=i: self.edit_task(i))
            btn_edit.pack(side="right", padx=5)

            btn_delete = ctk.CTkButton(frame, text="Excluir", width=70,
                                       fg_color="red", hover_color="#cc0000",
                                       command=lambda i=i: self.delete_task(i))
            btn_delete.pack(side="right", padx=5)

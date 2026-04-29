import customtkinter as ctk
from dashboard import Dashboard

class LoginApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Login")
        self.geometry("400x350")

        ctk.set_appearance_mode("dark")

        self.label = ctk.CTkLabel(self, text="Login", font=("Arial", 24))
        self.label.pack(pady=20)

        self.entry_user = ctk.CTkEntry(self, placeholder_text="Usuário")
        self.entry_user.pack(pady=10)

        self.entry_password = ctk.CTkEntry(self, placeholder_text="Senha", show="*")
        self.entry_password.pack(pady=10)

        self.btn = ctk.CTkButton(self, text="Entrar", command=self.login)
        self.btn.pack(pady=15)

        self.result = ctk.CTkLabel(self, text="")
        self.result.pack()

    def login(self):
        user = self.entry_user.get()
        password = self.entry_password.get()

        if user == "admin" and password == "123":
            self.destroy()
            dashboard = Dashboard()
            dashboard.mainloop()
        else:
            self.result.configure(text="Login inválido", text_color="red")
import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x300")
app.title("TELA DE LOGIN")

def login():
   username = entry_username.get()
   password= entry_password.get()

   if username == "admin" and password == "admin":
      messagebox.showinfo("Login", "Login bem-sucedido")
   else:
      messagebox.showerror("Error", "Nome de usuário ou senha incorretos.")

label_title = ctk.CTkLabel(app, text="Login", font=("Arial", 24))
label_title.pack(pady=20)

label_username = ctk.CTkLabel(app, text="Nome do Usuário: ")
label_username.pack(pady=5)
entry_username = ctk.CTkEntry(app, placeholder_text="Digite o seu noem de usuário", show="*")
entry_username.pack(pady=5)

label_password = ctk.CTkLabel(app, text="Senha: ")
label_password.pack(pady=5)
entry_password = ctk.CTkEntry(app, placeholder_text="Digite a sua senha", show="*")
entry_password.pack(pady=5)

button_login = ctk.CTkButton(app, text="Login", command=login)
button_login.pack(pady=20)

app.mainloop()
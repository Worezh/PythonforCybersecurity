import tkinter as tk
from tkinter import messagebox

class LoginApplication(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title("Login Application")
    self.geometry("300x200")

    # Create username label and entry
    self.username_label = tk.Label(self, text="Username:")
    self.username_label.pack()
    self.username_entry = tk.Entry(self)
    self.username_entry.pack()

    # Create password label and entry
    self.password_label = tk.Label(self, text="Password:")
    self.password_label.pack()
    self.password_entry = tk.Entry(self, show="*")
    self.password_entry.pack()

    # Create login button
    self.login_button = tk.Button(self, text="Login", command=self.login)
    self.login_button.pack()

  def login(self):
    username = self.username_entry.get()
    password = self.password_entry.get()
    if username and password:
      # Here you would typically check the username and password against a database
      # For this example, we'll just check against some hardcoded values
      if username == "admin" and password == "password":
        messagebox.showinfo("Login Success", "Welcome, admin!")
      else:
        messagebox.showerror("Login Failed", "Invalid username or password")
    else:
      messagebox.showerror("Login Failed", "Please enter both username and password")

# Create the GUI main window
window = LoginApplication()

# Enter the main event loop
window.mainloop()
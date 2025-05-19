import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
import subprocess
from main import Face_Recognition_System
class LoginSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Login - Smart Attendance System")
        self.root.geometry("400x300")
        self.root.configure(bg="#4c4b51")

        # Labels and Entry Fields
        title = tk.Label(self.root, text="Login", font=("times new roman", 24, "bold"), bg="#4c4b51", fg="white")
        title.pack(pady=20)

        username_label = tk.Label(self.root, text="Username:", font=("times new roman", 14), bg="#4c4b51", fg="white")
        username_label.pack(pady=5)
        self.username_entry = tk.Entry(self.root, font=("times new roman", 14))
        self.username_entry.pack(pady=5)

        password_label = tk.Label(self.root, text="Password:", font=("times new roman", 14), bg="#4c4b51", fg="white")
        password_label.pack(pady=5)
        self.password_entry = tk.Entry(self.root, font=("times new roman", 14), show="*")
        self.password_entry.pack(pady=5)

        login_btn = tk.Button(self.root, text="Login", font=("times new roman", 14, "bold"), bg="green", fg="white", command=self.login)
        login_btn.pack(pady=20)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "" or password == "":
            messagebox.showerror("Error", "All fields are required")
            return

        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="root", database="FACE")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
            result = cursor.fetchone()
            if result:
                messagebox.showinfo("Success", "Login Successful")
                self.root.destroy()
                subprocess.Popen(["python", "main.py"])
            else:
                messagebox.showerror("Error", "Invalid Username or Password")
            conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"Database Error: {str(e)}")

    def open_main_app(self):
        import attendance  # Import your main app module (attendance.py)

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginSystem(root)
    root.mainloop()
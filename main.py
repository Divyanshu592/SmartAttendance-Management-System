from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from tkinter import Canvas
from attendance import Attendance
class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1530x790+0+0')
        self.root.title("Face Recognition System")

        # Background image
        bg_img = Image.open(r"E:\Smart_Attendance_management_system\Image\grey.jpg")
        bg_img = bg_img.resize((1530, 790), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(bg_img)
        bg_label = Label(self.root, image=self.bg_photo)
        bg_label.place(x=0, y=0, width=1530, height=790)

        # Header logo
        header_img = Image.open(r"E:\Smart_Attendance_management_system\Image\logo.png")
        header_img = header_img.resize((500, 130), Image.Resampling.LANCZOS)
        self.logo_photo = ImageTk.PhotoImage(header_img)
        logo_lbl = Label(self.root, image=self.logo_photo, bg="#4c4b51")
        logo_lbl.place(x=515, y=10, width=500, height=130)

        # Function panel frame
        main_frame = Frame(self.root, bg="#2e2e2e", bd=2)
        main_frame.place(x=400, y=160, width=620, height=480)

        # Title label
        title_lbl = Label(main_frame, text="DASHBOARD", font=("Helvetica", 22, "bold"), bg="#2e2e2e", fg="white")
        title_lbl.place(x=270, y=10, width=200, height=60)  
        title_lbl.grid(row=0, column=0, columnspan=5, pady=20)

        # Button config list
        buttons = [
            ("Student Details", r"E:\Smart_Attendance_management_system\Image\boy.jpg", self.student_details),
            ("Face Detect", r"E:\Smart_Attendance_management_system\Image\scan1.jpg", self.face_data),
            ("Attendance", r"E:\Smart_Attendance_management_system\Image\att.jpg",self.Attendance_data),
            ("Train Data", r"E:\Smart_Attendance_management_system\Image\train.jpg", self.train_data),
            # ("Excel Generate", r"E:\Smart_Attendance_management_system\Image\excel.jpg", None),
            ("Exit", r"E:\Smart_Attendance_management_system\Image\exit.jpg", self.exit),
        ]

        # Create buttons in a grid
        for i, (text, img_path, cmd) in enumerate(buttons):
            row = (i // 3) + 1
            col = i % 3
            img = Image.open(img_path)
            img = img.resize((120, 120), Image.Resampling.LANCZOS)
            img_photo = ImageTk.PhotoImage(img)
            setattr(self, f"btn_img_{i}", img_photo)
            btn = Button(main_frame, image=img_photo, cursor="hand2", command=cmd if cmd else None,bg="#2e2e2e", activebackground="#444444",)
            btn.grid(row=row * 2 - 1, column=col, padx=40, pady=10)

            lbl = Button(main_frame, text=text, cursor="hand2", command=cmd if cmd else None,font=("Helvetica", 10, "bold"), bg="#2e2e2e", fg="white",activebackground="#444444", activeforeground="white", relief=FLAT, bd=0)
            lbl.grid(row=row * 2, column=col, pady=5)

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def exit(self):
        exit_confirm = messagebox.askyesno("Exit", "Do you want to exit?", parent=self.root)
        if exit_confirm:
            self.root.destroy()
            
    def Attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()

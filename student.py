import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1530x790+0+0')
        self.root.title("Student Details")
        
        # variables
        
        self.var_dep=tk.StringVar()#done
        self.var_std_name=tk.StringVar()#done
        self.var_roll=tk.StringVar()#done
        self.var_course=tk.StringVar()#done
        self.var_year=tk.StringVar()#done
        self.var_section=tk.StringVar()#done
        self.var_photo_sample = tk.StringVar()
        self.var_section=tk.StringVar()
        
        # background grey image
        img=Image.open(r"Image\grey.jpg") 
        img=img.resize((1530,790),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1530,height=790)
        
        # title student details
        title_lbl=tk.Label(self.root,text="STUDENT DETAILS",font=("times new roman",35,"bold"),bg="#4c4b51",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        main_frame=tk.LabelFrame(bg_img,borderwidth=2,bg="#4c4b51")
        main_frame.place(x=20,y=130,width=1480,height=600)
        
        # left lable frame
        left_frame=tk.LabelFrame(main_frame,bd=8,bg="#4c4b51",relief=RIDGE,fg="red",cursor="hand2",text="Student Details",font=("times new roman",16,"bold"))
        left_frame.place(x=10,y=10,width=750,height=580)
        
        # right frame
        right_frame=tk.LabelFrame(main_frame,bd=8,bg="#4c4b51",relief=RIDGE,fg="red",cursor="hand2",text="History",font=("times new roman",16,"bold"))
        right_frame.place(x=760,y=10,width=710,height=580)
        
        # department
        dep_label = tk.Label(left_frame, text="Department",cursor="hand2", font=("times new roman", 12, "bold"), bg="#4c4b51", fg="white")
        dep_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        
        self.department_combo = ttk.Combobox(left_frame,cursor="hand2",textvariable=self.var_dep, font=("times new roman", 12, "bold"), state="readonly", width=20,background="#4c4b51", foreground="black")
        self.department_combo["values"] = ("Select", "CSE", "ME", "CE", "EE")
        self.department_combo.current(0)
        self.department_combo.grid(row=0, column=1, padx=10, pady=5)

        # NAME
        name_label = tk.Label(left_frame, text="Name", font=("times new roman", 12, "bold"), bg="#4c4b51", fg="white")
        name_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        
        self.name_entry = ttk.Entry(left_frame,cursor="hand2",textvariable=self.var_std_name, font=("times new roman", 12, "bold"), width=22,state='normal')
        self.name_entry.grid(row=1, column=1, padx=10, pady=5)

        # ROLL NO
        roll_label = tk.Label(left_frame, text="Roll No", font=("times new roman", 12, "bold"), bg="#4c4b51", fg="white")
        roll_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        
        self.roll_entry = ttk.Entry(left_frame,cursor="hand2",textvariable=self.var_roll, font=("times new roman", 12, "bold"), width=22)
        self.roll_entry.grid(row=2, column=1, padx=10, pady=5)

        # COURSE
        course_label = tk.Label(left_frame, text="Course", font=("times new roman", 12, "bold"), bg="#4c4b51", fg="white")
        course_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        
        self.course_combo = ttk.Combobox(left_frame,cursor="hand2",textvariable=self.var_course, font=("times new roman", 12, "bold"), state="readonly", width=20)
        self.course_combo["values"] = ("Select", "B.Tech", "M.Tech", "Diploma", "PhD")
        self.course_combo.current(0)
        self.course_combo.grid(row=3, column=1, padx=10, pady=5)

        # YEAR
        year_label = tk.Label(left_frame, text="Year", font=("times new roman", 12, "bold"), bg="#4c4b51", fg="white")
        year_label.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
        self.year_combo = ttk.Combobox(left_frame,cursor="hand2",textvariable=self.var_year, font=("times new roman", 12, "bold"), state="readonly", width=20)
        self.year_combo["values"] = ("Select", "1st", "2nd", "3rd", "4th")
        self.year_combo.current(0)
        self.year_combo.grid(row=4, column=1, padx=10, pady=5)

        # SECTION
        section_label = tk.Label(left_frame, text="Section", cursor="hand2",font=("times new roman", 12, "bold"), bg="#4c4b51", fg="white")
        section_label.grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)
        self.section_combo = ttk.Combobox(left_frame,cursor="hand2",textvariable=self.var_section, font=("times new roman", 12, "bold"), state="readonly", width=20)
        self.section_combo["values"] = ("Select", "A", "B", "C")
        self.section_combo.current(0)
        self.section_combo.grid(row=5, column=1, padx=10, pady=5)
        
        self.photo_sample_var = tk.StringVar(value="No")
        
        #radio button
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(left_frame,text="Take Photo Sample",variable=self.photo_sample_var,cursor="hand2",value="Yes")
        radiobtn1.grid(row=6,column=0)
        
        self.var_radio2=StringVar()
        radiobtn2=ttk.Radiobutton(left_frame,text="No Photo Sample",variable=self.photo_sample_var,cursor="hand2",value="No")
        radiobtn2.grid(row=6,column=1)
        
        # btn_frame
        btn_frame=tk.Frame(left_frame,bd=8,bg="#4c4b51",relief=RIDGE)
        btn_frame.place(x=0,y=250,width=650,height=150)
        
        # save Button
        save_btn=tk.Button(master=btn_frame,text="Save",command=self.add_data,bg="#4c4b51",fg="white",width=34,font=("times new roman",12,"bold"),cursor="hand2")
        save_btn.grid(row=0,column=0)
        
        update_btn=tk.Button(master=btn_frame,text="Update",width=34,bg="#4c4b51",fg="white",font=("times new roman",12,"bold"),cursor="hand2", command=self.update_data)
        update_btn.grid(row=1,column=0)
        
        delete_btn=tk.Button(master=btn_frame,text="Delete",command=self.delete_data,width=34,bg="#4c4b51",fg="white",font=("times new roman",12,"bold"),cursor="hand2")
        delete_btn.grid(row=2,column=0)
        
        reset_btn=tk.Button(master=btn_frame,text="Reset",command=self.reset_data,width=34,bg="#4c4b51",fg="white",font=("times new roman",12,"bold"),cursor="hand2")
        reset_btn.grid(row=3,column=0)
        
        # take photo sample button
        take_photo_btn=tk.Button(master=btn_frame,text="Take Photo Sample",command=self.generate_dataset,width=34,bg="#4c4b51",fg="white",font=("times new roman",12,"bold"),cursor="hand2")
        take_photo_btn.grid(row=0,column=1)
        
        # update photo sample button
        update_photo_btn=tk.Button(master=btn_frame,text="Update Photo Sample",command=self.update_photo_sample,width=34,bg="#4c4b51",fg="white",font=("times new roman",12,"bold"),cursor="hand2")
        update_photo_btn.grid(row=1,column=1)
        
        # exit button
        exit_btn=tk.Button(master=btn_frame,text="Exit",command=self.exit,width=34,bg="#4c4b51",fg="white",font=("times new roman",12,"bold"),cursor="hand2")
        exit_btn.grid(row=2,column=1)
        # made by
        made=tk.Button(master=btn_frame,text="Made By Divyanshu Pandey And Abhay Negi",width=34,bg="#4c4b51",fg="white",font=("times new roman",12,"bold"),cursor="hand2")
        made.grid(row=3,column=1)
        
        # for the right frame
        style = ttk.Style()
        style.theme_use("default")  # Ensure a customizable theme
        style.configure("Treeview",
                background="#4c4b51",
                foreground="white",
                rowheight=25,
                fieldbackground="#4c4b51")

        style.map("Treeview", background=[("selected", "#6c6b71")])
        style.configure("Treeview.Heading", font=("times new roman", 12, "bold"), background="#4c4b51", foreground="white")
        # Add Treeview to display student data inside the right frame
        self.student_table = ttk.Treeview(right_frame, columns=("Department", "Name", "Roll", "Course", "Year", "Section", "Photo Sample"), show="headings")
        
        
        
        # Define headings
        self.student_table.heading("Department", text="Department")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Roll", text="Roll No")
        self.student_table.heading("Course", text="Course")
        self.student_table.heading("Year", text="Year")
        self.student_table.heading("Section", text="Section")
        self.student_table.heading("Photo Sample", text="Photo Sample")

        # Add scrollbars
        scroll_x = Scrollbar(right_frame, orient=HORIZONTAL, command=self.student_table.xview)
        scroll_y = Scrollbar(right_frame, orient=VERTICAL, command=self.student_table.yview)
        self.student_table.configure(xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()
    # function declaration
    def add_data(self):
        if (self.var_dep.get() == "Select" or
            self.var_std_name.get() == "" or
            self.var_roll.get() == "" or
            self.var_course.get() == "Select" or
            self.var_year.get() == "Select" or
            self.var_section.get() == "Select"):
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="root", database="FACE")
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "INSERT INTO student (Department, Name, RollNo, Course, Year, Section, photo_sample) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    (
                        self.var_dep.get(),
                        self.var_std_name.get(),
                        self.var_roll.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_section.get(),
                        self.var_photo_sample.get()
                    )
                )
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details have been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
                
    # fetch data
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="root", database="FACE")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM student")
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()
        
    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        self.var_dep.set(data[0])
        self.var_std_name.set(data[1])
        self.var_roll.set(data[2])
        self.var_course.set(data[3])
        self.var_year.set(data[4])
        self.var_section.set(data[5])
        self.var_photo_sample.set(data[6])
        self.original_roll = data[2]
        # update function
    def update_data(self):
        if (self.var_dep.get() == "Select" or
            self.var_std_name.get() == "" or
            self.var_roll.get() == "" or
            self.var_course.get() == "Select" or
            self.var_year.get() == "Select" or
            self.var_section.get() == "Select"):
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update", "Do you want to update this student details?", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="root", database="FACE")
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "UPDATE student SET Department=%s, Name=%s, RollNo=%s, Course=%s, Year=%s, Section=%s WHERE RollNo=%s",
                        (
                            self.var_dep.get(),
                            self.var_std_name.get(),
                            self.var_roll.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_section.get(),
                            self.original_roll
                        )
                    )
                else:
                    if not Update:
                        return    
                messagebox.showinfo("Success", "Student details have been updated successfully", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
                
                
    def delete_data(self):
        if (self.var_roll.get() == ""):
            messagebox.showerror("Error", "Roll No must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete", "Do you want to delete this student details?", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="root", database="FACE")
                    my_cursor = conn.cursor()
                    sql = "DELETE FROM student WHERE RollNo=%s"
                    val = (self.var_roll.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Student details have been deleted successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
    def reset_data(self):
        self.var_dep.set("Select")
        self.var_std_name.set("")
        self.var_roll.set("")
        self.var_course.set("Select")
        self.var_year.set("Select")
        self.var_section.set("Select")
        self.var_photo_sample.set("No")
        self.var_photo_sample.set("No")
        self.var_radio1.set("")
        self.var_radio2.set("")
        self.original_roll = ""
        
    def exit(self):
        exit = messagebox.askyesno("Exit", "Do you want to exit?", parent=self.root)
        if exit > 0:
            self.root.destroy()
        else:
            return
        
    def generate_dataset(self):
        print(self.var_roll.get())  # This will display the RollNo in the console.
        if (self.var_dep.get() == "Select" or self.var_std_name.get() == "" or self.var_roll.get() == "" or self.var_course.get() == "Select" or self.var_year.get() == "Select" or self.var_section.get() == "Select"):
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="root", database="FACE")
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM student WHERE RollNo=%s", (self.var_roll.get(),))
                myresult = my_cursor.fetchone()
                # id=0
                
                if myresult is None:
                    messagebox.showerror("Error", "Roll No already exists", parent=self.root)
                    return
                my_cursor.execute(
                        "UPDATE student SET Department=%s, Name=%s, RollNo=%s, Course=%s, Year=%s, Section=%s WHERE RollNo=%s",
                        (
                            self.var_dep.get(),
                            self.var_std_name.get(),
                            self.var_roll.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_section.get(),
                            self.var_roll.get()
                        )
                    )
                conn.commit()
                self.fetch_data()
                # self.reset_data()
                conn.close()
                #  using harr cascade   file
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                
                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y + h, x:x + w]
                        return face_cropped
        
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret, my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        
                        file_name_path=f"data/{self.var_roll.get()}_{img_id}.jpg"
                        
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating dataset completed")
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
    def update_photo_sample(self):
        update = messagebox.askyesno("Update Photo Sample", "Are you ready to update the photo sample for this student?", parent=self.root)
        if update:
            try:
            # Initiate the photo capture process (similar to the dataset generation function)
                conn = mysql.connector.connect(host="localhost", user="root", password="root", database="FACE")
                my_cursor = conn.cursor()

            # Check if the student already has a photo sample
                my_cursor.execute("SELECT * FROM student WHERE RollNo=%s", (self.var_roll.get(),))
                student = my_cursor.fetchone()

                if student is None:
                    messagebox.showerror("Error", "Student not found.", parent=self.root)
                    return

            # Start the photo capture
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y + h, x:x + w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = f"data/{self.var_roll.get()}_{img_id}.jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                # Break the loop after capturing a photo (for simplicity, only one photo)
                    if img_id >= 1:
                        break

                cap.release()
                cv2.destroyAllWindows()

            # Update the database with the new photo sample (You may store the file path or use the photo for recognition)
                my_cursor.execute("UPDATE student SET photo_sample=%s WHERE RollNo=%s", (file_name_path, self.var_roll.get()))
                conn.commit()
                conn.close()

            # Inform the user that the photo sample has been updated
                messagebox.showinfo("Success", "Photo sample updated successfully!", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}", parent=self.root)
        else:
            return

 
        
    
if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
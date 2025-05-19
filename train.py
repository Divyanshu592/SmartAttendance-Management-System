import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from PIL import Image,ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np
class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1530x790+0+0')
        self.root.title("Train Image")
        
        # background image
        img=Image.open(r"Image\grey.jpg")
        img=img.resize((1530,790),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1530,height=790)
        
        #title
        title_lbl=tk.Label(self.root,text="TRAIN   DATA   SET",font=("times new roman",35,"bold"),bg="#4c4b51",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        # Button
        b1_1=Button(self.root,text="Student Details",command=self.train_classifier,cursor="hand2")
        b1_1.place(x=710,y=380,width=90,height=23)
        

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,i) for i in os.listdir(data_dir)]
        faces=[]
        ids=[]
        
        for image in path:
            try:
                filename=os.path.basename(image)
                id=int(filename.split('_')[0])
                if "_" not in filename or not filename.endswith(".jpg"):
                    continue  # Skip incorrectly named files
                rollno = filename.split('_')[0]
                if not rollno.isdigit():
                    continue  # Skip if roll number is not numeric
                id = int(rollno)
        
                img = Image.open(image).convert('L')
                imageNp = np.array(img, 'uint8')
                faces.append(imageNp)
                ids.append(id)
                cv2.imshow("Training", imageNp)
                cv2.waitKey(1)
            except Exception as e:
                print(f"Skipping file {image}: {e}")

        ids=np.array(ids)
        
        #train the classifier and save the classifier 
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        messagebox.showinfo("Result","Training datasets completed!!")

if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()
    
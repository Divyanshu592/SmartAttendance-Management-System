import tkinter as tk
from tkinter import *
import mysql.connector
from PIL import Image, ImageTk
from datetime import datetime, date
import cv2
import os
import csv

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1530x790+0+0')
        self.root.title("Face Recognition")

        # background image
        img = Image.open(r"Image\grey.jpg")
        img = img.resize((1530, 790), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, width=1530, height=790)

        # title
        title_lbl = tk.Label(self.root, text="FACE RECOGNITION SYSTEM", font=("times new roman", 35, "bold"), bg="#4c4b51", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Button
        b1_1 = Button(self.root, text="Face Recognize", command=self.face_recog, cursor="hand2")
        b1_1.place(x=710, y=380, width=120, height=35)

    def mark_attendance(self, r, n, c):
        # Create filename based on today's date
        today_str = date.today().strftime("%Y-%m-%d")
        filename = f"Attendance_{today_str}.csv"
        today_display = date.today().strftime("%d/%m/%Y")

        # Check if file exists, if not create with header
        if not os.path.exists(filename):
            with open(filename, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["RollNo", "Name", "Course", "Date", "Time", "Status"])

        # Read existing attendance to avoid duplicates for today
        with open(filename, "r", newline="") as f:
            reader = csv.reader(f)
            existing_entries = list(reader)

        # Check if student already marked today
        for row in existing_entries[1:]:  # skip header
            if len(row) >= 4 and row[0] == str(r) and row[3] == today_display:
                return  # Already recorded for today

        # Mark attendance if not recorded
        now = datetime.now()
        time_string = now.strftime("%H:%M:%S")
        with open(filename, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([r, n, c, today_display, time_string, "Present"])

    def face_recog(self):
        cfg_path = r"E:/Smart_Attendance_management_system/yolov3-face.cfg"
        weights_path = r"E:/Smart_Attendance_management_system/yolov3-wider_16000.weights"

        if not os.path.exists(cfg_path) or not os.path.exists(weights_path):
            raise FileNotFoundError(
                f"Could not find YOLO files:\n  cfg:    {os.path.abspath(cfg_path)}\n  weights:{os.path.abspath(weights_path)}"
            )

        net = cv2.dnn.readNetFromDarknet(cfg_path, weights_path)
        net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
        net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

        layer_names = net.getLayerNames()
        output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read("classifier.xml")

        cap = cv2.VideoCapture(0)
        marked_today = set()

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            h, w = frame.shape[:2]
            blob = cv2.dnn.blobFromImage(frame, 1/255.0, (416, 416), swapRB=True, crop=False)
            net.setInput(blob)
            detections = net.forward(output_layers)

            boxes = []
            confidences = []

            for out in detections:
                for detection in out:
                    confidence = detection[4]
                    if confidence > 0.6:
                        center_x = int(detection[0] * w)
                        center_y = int(detection[1] * h)
                        box_w = int(detection[2] * w)
                        box_h = int(detection[3] * h)
                        x = int(center_x - box_w / 2)
                        y = int(center_y - box_h / 2)
                        boxes.append([x, y, box_w, box_h])
                        confidences.append(float(confidence))

            indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.6, 0.4)

            for i in indices:
                i = i[0] if isinstance(i, (list, tuple)) else i
                x, y, w_box, h_box = boxes[i]
                face_img = frame[y:y+h_box, x:x+w_box]
                gray = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)

                try:
                    id_, pred = recognizer.predict(gray)
                    confidence = int((100 * (1 - pred / 300)))
                except:
                    confidence = 0
                    id_ = "Unknown"

                if confidence > 60:
                    conn = mysql.connector.connect(host="localhost", user="root", password="root", database="FACE")
                    cursor = conn.cursor()
                    cursor.execute("SELECT Name FROM student WHERE RollNo=%s", (id_,))
                    n = cursor.fetchone()
                    n = n[0] if n else "Unknown"

                    cursor.execute("SELECT RollNo FROM student WHERE RollNo=%s", (id_,))
                    r = cursor.fetchone()
                    r = r[0] if r else "Unknown"

                    cursor.execute("SELECT Course FROM student WHERE RollNo=%s", (id_,))
                    c = cursor.fetchone()
                    c = c[0] if c else "Unknown"
                    conn.close()

                    cv2.rectangle(frame, (x, y), (x + w_box, y + h_box), (0, 255, 0), 2)
                    cv2.putText(frame, f"{n}, {r}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

                    key = cv2.waitKey(1) & 0xFF
                    if key == ord('p') and r not in marked_today:
                        self.mark_attendance(r, n, c)
                        marked_today.add(r)
                        cv2.putText(frame, "Attendance Marked", (x, y + h_box + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)

                else:
                    cv2.rectangle(frame, (x, y), (x + w_box, y + h_box), (0, 0, 255), 2)
                    cv2.putText(frame, "Unknown", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

            cv2.imshow("YOLO Face Recognition", frame)

            if cv2.waitKey(1) & 0xFF == 13:  # Enter key to exit
                break

        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()

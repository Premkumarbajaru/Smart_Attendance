import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
import os
import numpy as np
import csv
from datetime import datetime
import pandas as pd
import time

class AttendanceSystem:
    def __init__(self, window):
        self.window = window
        self.window.title("AI Attendance")
        self.window.state("zoomed")
        self.window.configure(bg="#f0f0f0")  # Light background color
        self.detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        self.cap = None
        self.is_camera_on = False
        self.face_id = None
        self.create_widgets()

    def create_widgets(self):
        header = tk.Label(
            self.window,
            text="Attendance Management System using Facial Recognition",
            bg="#1e88e5",  # Blue header background
            fg="white",
            font=('Helvetica', 24, 'bold'),
            padx=20,
            pady=20,
        )
        header.pack(fill=tk.X)

        # Input Fields
        input_frame = tk.Frame(self.window, bg="#f0f0f0")
        input_frame.pack(pady=20)

        tk.Label(input_frame, text="Enrollment Number", fg="#333333", font=('Helvetica', 14, 'bold'), bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=10)
        self.enrollment_txt = tk.Entry(input_frame, width=25, font=('Helvetica', 14))
        self.enrollment_txt.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(input_frame, text="Student Name", fg="#333333", font=('Helvetica', 14, 'bold'), bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=10)
        self.name_txt = tk.Entry(input_frame, width=25, font=('Helvetica', 14))
        self.name_txt.grid(row=1, column=1, padx=10, pady=10)

        # Buttons
        button_frame = tk.Frame(self.window, bg="#f0f0f0")
        button_frame.pack(pady=20)

        self.close_camera_button = tk.Button(
            button_frame,
            text="Close Camera",
            command=self.stop_camera,
            bg="#f44336",  # Red button
            fg="white",
            font=('Helvetica', 14, 'bold'),
            state=tk.DISABLED,
            width=15,
        )
        self.close_camera_button.grid(row=0, column=0, padx=10, pady=10)

        self.take_img_button = tk.Button(
            button_frame,
            text="Take Images",
            command=self.toggle_camera,
            bg="#4caf50",  # Green button
            fg="white",
            font=('Helvetica', 14, 'bold'),
            width=15,
        )
        self.take_img_button.grid(row=0, column=1, padx=10, pady=10)

        self.train_img_button = tk.Button(
            button_frame,
            text="Train Images",
            command=self.train_img,
            bg="#2196f3",  # Blue button
            fg="white",
            font=('Helvetica', 14, 'bold'),
            width=15,
        )
        self.train_img_button.grid(row=0, column=2, padx=10, pady=10)

        self.smart_att_button = tk.Button(
            button_frame,
            text="Smart Attendance",
            command=self.smart_attendance_window,
            bg="#ff5722",  # Orange button
            fg="white",
            font=('Helvetica', 14, 'bold'),
            width=15,
        )
        self.smart_att_button.grid(row=1, column=0, padx=10, pady=10)

        self.manual_att_button = tk.Button(
            button_frame,
            text="Manual Attendance",
            command=self.manual_attendance_window,
            bg="#607d8b",  # Grey button
            fg="white",
            font=('Helvetica', 14, 'bold'),
            width=15,
        )
        self.manual_att_button.grid(row=1, column=1, padx=10, pady=10)

        self.admin_panel_button = tk.Button(
            button_frame,
            text="Admin Panel",
            command=self.admin_panel,
            bg="#9c27b0",  # Purple button
            fg="white",
            font=('Helvetica', 14, 'bold'),
            width=15,
        )
        self.admin_panel_button.grid(row=1, column=2, padx=10, pady=10)

    def toggle_camera(self):
        if not self.validate_inputs():
            return
        if self.is_camera_on:
            self.stop_camera()
        else:
            self.is_camera_on = True
            self.capture_images()
            self.close_camera_button.config(state=tk.NORMAL)  # Enable the Close Camera button

    def capture_images(self):
        self.cap = cv2.VideoCapture(0)
        count = 0
        if not os.path.exists("Training_Images"):
            os.makedirs("Training_Images")

        csv_file_path = "./StudentDetails/StudentDetails.csv"
        if not os.path.exists("./StudentDetails"):
            os.makedirs("./StudentDetails")

        while self.is_camera_on:
            ret, frame = self.cap.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))
            for (x, y, w, h) in faces:
                count += 1
                image_path = f"Training_Images/{self.name_txt.get().strip()}.{self.face_id}.{count}.jpg"
                cv2.imwrite(image_path, gray[y:y+h, x:x+w])
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

                if count >= 2:
                    self.update_student_details_csv(csv_file_path)
                    messagebox.showinfo("Success", "Images Captured and Details Saved Successfully!")
                    return

            cv2.imshow("Capture Images", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cv2.destroyAllWindows()

    def update_student_details_csv(self, csv_file_path):
        enrollment = self.enrollment_txt.get().strip()
        name = self.name_txt.get().strip()
        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([enrollment, name, time.strftime("%Y-%m-%d %H:%M:%S")])

    def validate_inputs(self):
        enrollment = self.enrollment_txt.get().strip()
        name = self.name_txt.get().strip()
        if not enrollment.isdigit() or not name.isalpha():
            messagebox.showerror("Error", "Please enter valid enrollment and name.")
            return False
        self.face_id = int(enrollment)
        return True

    def stop_camera(self):
        if self.cap:
            self.cap.release()
            cv2.destroyAllWindows()
        self.is_camera_on = False
        self.close_camera_button.config(state=tk.DISABLED)

    def train_img(self):
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        faces, ids = self.get_images_and_labels("Training_Images")
        recognizer.train(faces, np.array(ids))
        recognizer.save("Training_Image_Label/trainner.yml")
        messagebox.showinfo("Success", "Model Trained Successfully!")

    def get_images_and_labels(self, path):
        image_paths = [os.path.join(path, f) for f in os.listdir(path)]
        faces = []
        ids = []
        for image_path in image_paths:
            img = Image.open(image_path).convert("L")
            img_np = np.array(img, "uint8")
            id = int(os.path.split(image_path)[-1].split(".")[1])
            faces.append(img_np)
            ids.append(id)
        return faces, ids

    def smart_attendance_window(self):
        self.smart_window = tk.Toplevel(self.window)
        self.smart_window.title("Smart Attendance")
        self.smart_window.geometry("600x400")
        self.smart_window.configure(bg="#f0f0f0")
        tk.Label(self.smart_window, text="Enter Subject", font=('Helvetica', 14), bg="#f0f0f0").pack(pady=20)
        self.subject_entry = tk.Entry(self.smart_window, font=('Helvetica', 14))
        self.subject_entry.pack(pady=10)
        tk.Button(self.smart_window, text="Start Attendance", command=self.start_smart_attendance, font=('Helvetica', 14), bg="#1e88e5", fg="white").pack(pady=10)

    def start_smart_attendance(self):
        subject = self.subject_entry.get().strip()
        if not subject:
            messagebox.showerror("Error", "Please enter a subject.")
            return
        
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read("Training_Image_Label/trainner.yml")
        cap = cv2.VideoCapture(0)
        self.is_camera_on = True
        self.close_camera_button.config(state=tk.NORMAL)  # Enable the Close Camera button
        
        attendance_marked = False

        while self.is_camera_on:
            ret, frame = cap.read()
            if not ret:
                break
            
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))
            for (x, y, w, h) in faces:
                id, confidence = recognizer.predict(gray[y:y + h, x:x + w])
                if confidence < 100:  # Recognition is confident
                    self.mark_attendance(id, subject)
                    messagebox.showinfo("Attendance", f"Attendance marked for ID: {id}.")
                    attendance_marked = True
                    break
            
            if attendance_marked:
                break  # Exit the loop after marking one attendance
            
            cv2.imshow("Smart Attendance", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):  # Option to quit manually
                break

        cap.release()
        cv2.destroyAllWindows()
        self.is_camera_on = False
        self.close_camera_button.config(state=tk.DISABLED)  # Disable the Close Camera button

    def mark_attendance(self, student_id, subject):
        folder = "SmartAttendance"
        if not os.path.exists(folder):
            os.makedirs(folder)
        date_str = datetime.now().strftime("%Y-%m")
        filename = os.path.join(folder, f"{subject}_{date_str}.csv")
        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([student_id, time.strftime("%Y-%m-%d %H:%M:%S")])

    def manual_attendance_window(self):
        manually_window = tk.Toplevel(self.window)
        manually_window.title("Manual Attendance")
        manually_window.geometry("600x400")
        manually_window.configure(bg="#f0f0f0")
        tk.Label(manually_window, text="Enrollment number", font=('Helvetica', 14), bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=10)
        enrollment_entry = tk.Entry(manually_window, font=('Helvetica', 14))
        enrollment_entry.grid(row=0, column=1, padx=10, pady=10)
        tk.Label(manually_window, text="Enter Name", font=('Helvetica', 14), bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=10)
        name_entry = tk.Entry(manually_window, font=('Helvetica', 14))
        name_entry.grid(row=1, column=1, padx=10, pady=10)
        tk.Button(manually_window, text="Submit", font=('Helvetica', 14), bg="#1e88e5", fg="white", command=lambda: self.submit_manual_attendance(enrollment_entry, name_entry)).grid(row=2, column=1, padx=10, pady=10)

    def submit_manual_attendance(self, enrollment_entry, name_entry):
        enrollment = enrollment_entry.get().strip()
        name = name_entry.get().strip()
        if not enrollment or not name:
            messagebox.showerror("Error", "Both fields are required.")
            return
        folder = "ManualAttendance"
        if not os.path.exists(folder):
            os.makedirs(folder)
        with open(os.path.join(folder, "attendance.csv"), mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([enrollment, name, time.strftime("%Y-%m-%d %H:%M:%S")])
        messagebox.showinfo("Success", "Attendance marked successfully!")

    def admin_panel(self):
        self.admin_window = tk.Toplevel(self.window)
        self.admin_window.title("Admin Panel")
        self.admin_window.geometry("800x500")
        self.admin_window.configure(bg="#f0f0f0")
        self.load_registered_students()

    def load_registered_students(self):
        try:
            student_data = pd.read_csv("./StudentDetails/StudentDetails.csv")
            for idx, student in student_data.iterrows():
                tk.Label(self.admin_window, text=f"ID: {student['Enrollment']} - Name: {student['Name']}", font=('Helvetica', 12), bg="#f0f0f0").pack(pady=5)
        except FileNotFoundError:
            messagebox.showerror("Error", "No registered students found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AttendanceSystem(root)
    root.protocol("WM_DELETE_WINDOW", app.stop_camera)
    root.mainloop()
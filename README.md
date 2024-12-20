
# Attendance Management System using Facial Recognition

Welcome to the **Attendance Management System**, a comprehensive solution that leverages facial recognition to automate attendance marking. This project provides both smart (via facial recognition) and manual attendance recording features, along with an admin panel to manage student records efficiently.

---

## Table of Contents
1. [Features](#features)  
2. [Technologies Used](#technologies-used)
3. [Directory Structure](#directorystructure)
4. [Application Workflow](#application-workflow) 
5. [Installation](#installation)
6. [Usage](#Usage)  
7. [Contributing](#Contributing)  
8. [License](#license)  

---

## Features
- **Face Recognition**: Automatically recognize students' faces and mark their attendance.
- **Image Capture**: Capture and save images for training the recognition model.
- **Manual Attendance**: Option to manually fill attendance records.
- **CSV Export**: Generate attendance reports in CSV format.
- **Database Integration**: Store attendance records in a MySQL database.  

---

## Technologies Used
- **Python**: Core language for implementation.  
- **Tkinter**: For creating the graphical user interface.  
- **OpenCV**: For face detection and recognition.  
- **Pandas**: For handling CSV files and data analysis.  
- **Pillow**: For image processing.  

---

## Directory Structure
```plaintext
Attendance Management System using Face Recognition/
│
├── TrainingImage/               # Directory to store training images
├── TrainingImageLabel/          # Directory to save trained model
├── StudentDetails/              # Directory to save student details CSV
├── Attendance/                  # Directory to save attendance records
├── haarcascade_frontalface_default.xml  # Haarcascade file for face detection
├── requirements.txt             # Required Python packages
├── main_Run.py                  # Main application file
├── training.py                  # Script for training the face recognition model
├── testing.py                   # Script for testing face recognition
├── mini_app.py                  # Simple GUI application for capturing images
├── app.py                       # Streamlit app for attendance visualization
└── README.md                    # Project documentation
```


## Application Workflow

#### 1. Take Images  
Capture images of students for training the model.  


![Screenshot 2024-12-10 104509](https://github.com/user-attachments/assets/2dda9520-1d99-4fa8-9df2-21984e2978a5)

#### 2. Train Images  
Train the facial recognition model using the captured images.  

![Screenshot 2024-12-12 145600](https://github.com/user-attachments/assets/385a4e3d-a736-4050-9271-8e484de5ae8f)

#### 3. Smart Attendance  
Automatically record attendance by recognizing faces. 


![Screenshot 2024-12-12 114037](https://github.com/user-attachments/assets/2ad801e2-f75e-4a24-a6c0-d6254681544f)

#### 4. Manual Attendance  
Manually enter attendance when necessary.  


![Screenshot 2024-12-12 145618](https://github.com/user-attachments/assets/a29c0b6d-3f71-4b44-8737-730cc988cdf9)

#### 5. Admin Panel  
View and manage registered student details.


![Screenshot 2024-12-12 114105](https://github.com/user-attachments/assets/e6f5b4f9-2632-4c7f-bf50-1a962ad95aae)

### Closing the Application
The app supports a safe exit via the **Close Camera** button or the window close button.


![Screenshot 2024-12-12 113134](https://github.com/user-attachments/assets/e997b5b6-fba5-4560-993d-c041d4c9636f)

---


## Installation

To run CareCue locally, follow these steps:

1. Clone this repository:
```bash
    https://github.com/Premkumarbajaru/Smart_Attendance.git
```
2. Install dependencies:
```bash
   pip install -r requirements.txt
```
3. Run the Flask application:
```bash
   python main.py
```
### 4. Set Up MySQL Database
- Create a MySQL database to store attendance records.
- Update the database connection details in the code as needed.

### 5. Download Haarcascade
Download the Haarcascade XML file for face detection from the [OpenCV GitHub repository](https://github.com/Premkumarbajaru/Smart_Attendance) and place it in the project directory.


---


## Usage

### 1. Capture Images
- Run `main_Run.py` to open the GUI.
- Enter the student's enrollment number and name.
- Click on **"Take Images"** to capture their face images.

### 2. Train the Model
- After capturing images, click on **"Train Images"** to train the face recognition model.

### 3. Automatic Attendance
- Select **"Automatic Attendance"** to start the face recognition process using the webcam.

### 4. Manual Attendance
- Use the **"Manually Fill Attendance"** option to manually fill attendance records.

### 5. View Registered Students
- Access the admin panel to view the list of registered students and their details.

---


## Contributing

Contributions are welcome! Please feel free to fork this repository and submit pull requests to suggest new features, enhancements, or bug fixes.

## License

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.
---

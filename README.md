
# Attendance Management System using Facial Recognition

Welcome to the **Attendance Management System**, a comprehensive solution that leverages facial recognition to automate attendance marking. This project provides both smart (via facial recognition) and manual attendance recording features, along with an admin panel to manage student records efficiently.

---

## Table of Contents
1. [Features](#features)  
2. [Technologies Used](#technologies-used)
3. [Directory Structure](#DirectoryStructure)
4. [Application Workflow](#application-workflow) 
5. [Installation](#installation)  
6. [Contributing](#Contributing)  
7. [License](#license)  

---

## Features
- **Real-time Facial Recognition**: Use your webcam to automatically record attendance.  
- **GUI Interface**: User-friendly graphical interface for seamless interaction.  
- **Smart Attendance**: Automatically recognize and mark attendance based on stored facial data.  
- **Manual Attendance**: Enter attendance details manually for additional flexibility.  
- **Admin Panel**: Manage and view student data directly from the application.  

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

## Contributing

Contributions are welcome! Please feel free to fork this repository and submit pull requests to suggest new features, enhancements, or bug fixes.

## License

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.
---

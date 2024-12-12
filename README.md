
# Attendance Management System using Facial Recognition

Welcome to the **Attendance Management System**, a comprehensive solution that leverages facial recognition to automate attendance marking. This project provides both smart (via facial recognition) and manual attendance recording features, along with an admin panel to manage student records efficiently.

---

## Table of Contents
1. [Features](#features)  
2. [Technologies Used](#technologies-used)
3. [Application Workflow](#application-workflow) 
4. [Installation](#installation)  
5. [Usage Guide](#usage-guide)  
6. [License](#license)  

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
### Application Workflow

#### 1. Take Images  
Capture images of students for training the model.  
![Take Images](path_to_image/take_images.png)

#### 2. Train Images  
Train the facial recognition model using the captured images.  
![Train Images](path_to_image/train_images.png)

#### 3. Smart Attendance  
Automatically record attendance by recognizing faces.  
![Smart Attendance](path_to_image/smart_attendance.png)

#### 4. Manual Attendance  
Manually enter attendance when necessary.  
![Manual Attendance](path_to_image/manual_attendance.png)

#### 5. Admin Panel  
View and manage registered student details.  
![Admin Panel](path_to_image/admin_panel.png)

### Closing the Application
The app supports a safe exit via the **Close Camera** button or the window close button.

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

This project is licensed under the Apache License 2.0 - see the [LICENSE] file for details.
---

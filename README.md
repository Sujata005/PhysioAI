# PhysioAI System

PhysioAI is an advanced AI-powered physiotherapy assistant designed to provide real-time posture monitoring and corrective feedback. Built using computer vision and deep learning, the system helps users perform rehabilitation exercises with precision, ensuring safety and effectiveness in a home-based setting.

## 🚀 Overview

The PhysioAI system addresses the challenges of remote physiotherapy by using a standard webcam to track body movements. It calculates joint angles and compares them against clinically recommended ranges to provide instant visual feedback, helping prevent injury and improve recovery outcomes.

## ✨ Key Features

* **Real-Time Pose Estimation:** Utilises MediaPipe to track 33 essential body landmarks.
* **Anatomical Angle Calculation:** Processes joint movements in real-time to ensure exercises are performed within correct physiological limits.
* **Color-Coded Feedback:** * 🟢 **Green:** Correct posture and alignment.
    * 🔴 **Red:** Postural deviation detected; immediate correction required.
* **Modular Exercise Library:**
    * **Arms Module:** Tracks shoulder, elbow, and wrist coordination.
    * **Legs Module:** Focuses on hip, knee, and ankle stability.
    * **Shoulders Module:** Monitors complex shoulder articulation and range of motion.
* **Automatic Repetition Counting:** Validates and counts successful reps only when the full range of motion is achieved.

## 🛠️ Tech Stack

* **Language:** Python
* **Web Framework:** Flask
* **Computer Vision:** OpenCV, MediaPipe
* **Frontend:** HTML5, CSS3, JavaScript
* **Deployment:** Designed for local and cloud-based environments (AWS EC2)

## 🏗️ System Architecture

1.  **Input Layer:** Captures video stream from the user's webcam.
2.  **Processing Layer:** * Extracts coordinates of body landmarks.
    * Calculates Euclidean distances and joint angles.
3.  **Logic Layer:** Compares real-time data against predefined exercise thresholds.
4.  **Output Layer:** Streams the processed video back to the web interface with visual overlays and real-time status updates.

## ⚙️ Installation

1. **Clone the repository:**
   ```
   git clone [https://github.com/yourusername/physioai.git](https://github.com/yourusername/physioai.git)
   cd physioai

2. **Install required dependencies:**
   ``` pip install flask opencv-python mediapipe numpy ``` 

3. **Run the application:**
   ``` python app.py ``` 

4. **Access the application:**
Open your browser and go to ``` http://127.0.0.1:5000 ```

## 📊 Performance
- **Accuracy:** Achieved 93-95% accuracy in posture detection across various exercise modules.

- **Latency:** Optimised for low-latency feedback on standard CPU hardware.

## 📄 License
This project was developed as part of a Bachelor of Technology in Computer Science & Engineering at Graphic Era Hill University.

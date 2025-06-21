
# 🧠 PhysioAI – Real-Time Posture Monitoring Web App

![PhysioAI Demo](https://img.shields.io/badge/Status-Active-green?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)

PhysioAI is a web-based physiotherapy assistant that provides **real-time posture monitoring** using computer vision. It is designed to guide users through physical therapy exercises, giving instant feedback and counting repetitions using webcam input.

> 🧬 Built using Python, Flask, MediaPipe, OpenCV, HTML/CSS, and JavaScript.

---

## 🚀 Features

- 🎥 **Live Webcam Feed** for real-time video processing
- 🦾 **Pose Detection with MediaPipe** for accurate body tracking
- 📊 **Exercise Counters** for arms, legs, and shoulders
- ⚠️ **Posture Alerts** for incorrect form
- 💻 **Responsive UI** for desktop and mobile
- 🧩 Modular design with separate exercise pages

---

## 🛠️ Technologies Used

- **Backend:** Flask (Python)
- **Pose Estimation:** MediaPipe
- **Computer Vision:** OpenCV
- **Frontend:** HTML, CSS, JavaScript
- **Webcam Integration:** OpenCV + MediaPipe

---

## 🧪 How to Run Locally

```bash
# Clone the repository
git clone https://github.com/your-username/PhysioAI.git
cd PhysioAI

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py

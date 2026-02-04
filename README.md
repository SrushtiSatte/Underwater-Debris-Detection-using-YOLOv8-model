# 🌊 Underwater Debris Detection using YOLOv8

A complete **AI-powered web application** for detecting underwater debris using **YOLO deep learning models**, integrated with a **modern web UI and live Gradio demo**.

---

## 🚀 Project Overview

Marine pollution is a growing environmental concern. This project uses **computer vision and deep learning** to automatically detect underwater debris such as plastic, metal, and waste materials from underwater images and videos.

The system combines:

* **YOLOv8 Object Detection Model**
* **Gradio-based ML interface**
* **Interactive Web UI using HTML, CSS & Bootstrap**
* **Real-time image inference**

---

## 🧠 Key Features

* 🔍 Real-time underwater debris detection
* ⚡ High-speed inference using YOLOv8
* 🌐 Web-based user interface
* 📸 Image upload & instant prediction
* 📊 Model comparison visualization
* 🖥 Integrated Gradio live demo

---

## 🛠 Tech Stack

### Machine Learning

* Python
* YOLOv8 (Ultralytics)
* PyTorch
* OpenCV
* Gradio

### Frontend

* HTML
* CSS
* Bootstrap
* JavaScript

---

## 📂 Project Structure

```
project-root/
│
├── index.html
│
├── ml_app/
│   ├── app.py
│   └── models/
│       └── 60_epochs_denoised.pt
│
└── requirements.txt
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/underwater-debris-detection.git
cd underwater-debris-detection
```

---

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

OR manually:

```bash
pip install ultralytics gradio torch torchvision opencv-python roboflow
```

---

## ▶️ How To Run

### Step 1 — Start ML Server

```bash
cd ml_app
python app.py
```

Gradio will run at:

```
http://127.0.0.1:7860
```

---

### Step 2 — Open Web UI

Open `index.html` in browser.

Now scroll to **Live Demo section** — your Gradio UI will load inside iframe.

---

## 🌐 Live Demo Integration

Your website automatically loads the ML interface using:

```html
<iframe src="http://127.0.0.1:7860"></iframe>
```

This enables **real-time prediction directly inside the website UI**.

---

## 📊 Model Used

* YOLOv8 (Ultralytics)
* Custom trained model
* Trained for **60 epochs**
* Optimized for **underwater debris detection**

---

## 🧪 Use Cases

* Marine cleanup automation
* Underwater robotics
* Ocean pollution monitoring
* Environmental research

---

## 📸 Screenshots

* Web UI
* Model detection results
* Gradio live interface

![Web UI](img/ui1.png)
![Gradio Live Demo](img/ui2.png)

---

## 📜 License

This project is for **educational and research purposes only**.

---

## ⭐ Support

If you like this project:

* ⭐ Star this repo
* 🍴 Fork it
* 🧠 Learn & build more AI projects

---

🔥 **Built with Passion for Clean Oceans & AI Innovation** 🌊🤖

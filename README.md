# 🌊 Underwater Debris Detection using YOLOv8

An **AI-powered web application** for detecting underwater debris using a **YOLOv8 deep learning model**, combined with a **modern frontend UI** and a **live Gradio demo hosted separately**.

---

## 🚀 Project Overview

Marine pollution is a serious environmental challenge. This project applies **computer vision and deep learning** to automatically detect underwater debris such as plastic, metal, and waste materials from images.

The system consists of:

* **YOLOv8 Object Detection Model**
* **Gradio-based ML inference app**
* **Responsive Web UI (HTML, CSS, JS, Bootstrap)**
* **Live model inference via iframe integration**

---

## 🧠 Key Features

* 🔍 Real-time underwater debris detection
* ⚡ Fast inference using YOLOv8
* 🌐 Web-based interactive UI
* 📸 Image upload and instant prediction
* 🖥 Live Gradio demo integration
* ☁ Public deployment using HuggingFace Spaces

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

## 📂 Updated Project Structure

```
Underwater-Debris-Detection-using-YOLO-model/
│
├── frontend/
│   ├── index.html
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── main.js
│   └── img/
│       ├── ui1.png
│       └── ui2.png
│
├── ml_app/
│   ├── app.py
│   └── models/
│       └── 60_epochs_denoised.pt
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup (Local)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/Underwater-Debris-Detection-using-YOLO-model.git
cd Underwater-Debris-Detection-using-YOLO-model
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

## ▶️ Running the Project Locally

### Step 1 — Start the ML Application

```bash
cd ml_app
python app.py
```

Gradio will start at:

```
http://127.0.0.1:7860
```

---

### Step 2 — Run the Frontend

```bash
cd frontend
python -m http.server 5500
```

Open in browser:

```
http://localhost:5500
```

The **Live Demo section** will display the Gradio interface via iframe.

---

## 🌐 Live Demo (Public Deployment)

The trained YOLOv8 model is deployed using **HuggingFace Spaces**, and the frontend embeds it using an iframe.

```html
<iframe 
  src="https://huggingface.co/spaces/SrushtiSatte/underwater_debris_detection_yolov8?embed=true"
  width="100%"
  height="600"
></iframe>
```

This allows users to **try the model directly from the website without running it locally**.

---

## 📊 Model Details

* YOLOv8 (Ultralytics)
* Custom-trained underwater debris dataset
* Trained for **60 epochs**
* Optimized for underwater visibility challenges

---

## 🧪 Use Cases

* Marine cleanup automation
* Underwater robotics
* Ocean pollution monitoring
* Environmental research & analysis

---

## 📸 Screenshots

### Web Interface

![Web UI](frontend/img/ui1.png)

### Live Gradio Demo

![Gradio Live Demo](frontend/img/ui2.png)

---

## 📜 License

This project is intended for **educational and research purposes only**.

---

## ⭐ Support

If you find this project useful:

* ⭐ Star this repository
* 🍴 Fork and experiment
* 🤖 Build more AI-powered solutions
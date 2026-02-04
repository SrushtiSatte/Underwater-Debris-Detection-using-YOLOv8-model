import gradio as gr
from ultralytics import YOLO
import cv2
import numpy as np

# Load your trained model
model = YOLO("models/60_epochs_denoised.pt")   # change name if needed

def detect(image):
    results = model(image)
    res_img = results[0].plot()
    return res_img

demo = gr.Interface(
    fn=detect,
    inputs=gr.Image(type="numpy", label="Upload Underwater Image"),
    outputs=gr.Image(type="numpy", label="Detected Output"),
    title="Underwater Debris Detection - YOLOv8",
    description="Upload underwater images and detect marine debris using YOLOv8"
)

demo.launch(inbrowser=True, server_name="127.0.0.1", server_port=7860)

# Underwater Debris Detection using YOLOv8 model

A small website and notebook demo for underwater debris detection using YOLOv8 and a Gradio UI.

This repository includes:

- A static website (`index.html`) with a Live Demo iframe that can show a locally-run Gradio app.
- A notebook `Train_Underwater_Waste_Detection_YoloV8 (3).ipynb` that contains data download, training, inference, a notebook Gradio demo, and a simple Flask endpoint for programmatic use.
- A lightweight YOLOv8 model (`yolov8n.pt`) for quick testing.

Quick setup (Windows)

1. Open PowerShell in the project root.
2. Create & activate a virtual environment (recommended):
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
3. Install required packages:
   ```powershell
   pip install gradio ultralytics pillow numpy flask flask-cors
   ```

Run the Gradio demo (recommended)

- Notebook (recommended for first run):
  1. Open `Train_Underwater_Waste_Detection_YoloV8 (3).ipynb` in Jupyter or VS Code.
  2. Run the cell that prints `Found candidate .pt files...` (this sets `model_path`).
  3. Run the cell titled **Launch an in-notebook Gradio demo**. It will try ports 7860–7862 and open the UI in your browser automatically.

- Outside the notebook (optional):
  If you prefer a script-based launcher, create a small script to import the same `iface` and call `iface.launch(server_name='127.0.0.1', server_port=7860, inbrowser=True)`.

Using your own trained model

- Place your `.pt` file in the repository (e.g., project root or a `models/` folder).
- Re-run the cell that auto-detects `.pt` files; the notebook will select the most recent `.pt` and use it for inference.

Flask endpoint (programmatic access)

- The notebook contains a Flask app exposing `POST /process-image` which accepts a form file named `image` and returns a processed PNG.
- To test locally (after running the Flask cell):
  ```powershell
  curl -F "image=@path\to\image.jpg" http://127.0.0.1:5500/process-image -o result.png
  ```

Colab and Roboflow notes

- Cells that mount Google Drive are guarded so they won't fail on Windows; run them when using Google Colab.
- `roboflow.login()` requires an API key and network access—provide credentials in Colab or set env vars locally if you use Roboflow.

Troubleshooting

- Ports in use: If `7860` or `5500` are in use, change the port when launching or stop the conflicting process.
- Browser not opening: open `http://127.0.0.1:7860` manually; the notebook also embeds an iframe when the server starts.
- Model load errors: ensure the `.pt` file is present and compatible with the installed `ultralytics` version.

Contributing

Contributions are welcome: add tests, training scripts, or a `run_gradio.py` and `flask_app.py` for a cleaner standalone run.

License

This project is provided as-is for educational/demo purposes.
# 🖼️ ASCII Art Studio

A high-performance, lightweight web application that transforms photos into stylized ASCII art.

[![Live Demo](https://img.shields.io/badge/Live_Demo-Vercel-black?style=for-the-badge&logo=vercel&logoColor=white)](https://ascii-art-generator-sand.vercel.app/)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0.3-000000?style=flat-square&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![OpenCV](https://img.shields.io/badge/OpenCV-Headless-5C3EE8?style=flat-square&logo=opencv&logoColor=white)](https://opencv.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Fast_Matrix-013243?style=flat-square&logo=numpy&logoColor=white)](https://numpy.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

🔗 **Live Deployment:** [https://ascii-art-generator-sand.vercel.app/](https://ascii-art-generator-sand.vercel.app/)

> Pure algorithmic computer vision. 100% Local processing. Zero GPU required.

---

## ✨ Features

- ⚡ **Sub-50ms Processing**: Powered by NumPy vector quantization and OpenCV matrix operations.
- 🎨 **Multiple Glyph Palettes**:
  - **Standard**: Classic 10-level brightness density ramp (` .:-=+*#%@`).
  - **Detailed**: 70-character high-fidelity shade ramp.
  - **Block Shades**: Modern block gradients (` ░▒▓█`).
  - **Matrix Binary**: Minimalist cyberpunk cyber-art (` 01`).
  - **Minimal**: Extreme contrast duo-tone (` .#`).
- 🌈 **Full RGB Color Mode**: Renders colored HTML spans mapping the exact chromatic values of original pixels.
- 🎛️ **Live Parameter Controls**:
  - Real-time resolution slider (30 to 220 character grid width).
  - Dynamic contrast enhancement (0.5x to 2.0x).
  - Monospace font aspect ratio compensation (1:0.55).
  - Instant brightness inversion toggle.
- 💾 **Multi-Format Export**:
  - **Plain Text (`.txt`)**: Raw characters ready for terminals and text editors.
  - **Image (`.png` / `.jpg`)**: Pixel-perfect canvas export at native font resolution with preserved background and color.
  - **One-Click Clipboard Copy**: Instant copy for sharing.

---

## 📐 How It Works

Traditional raster images are converted to ASCII using a 5-stage mathematical pipeline:

```text
[ Input Photo ]
       │
       ▼
1. Aspect Ratio Correction  ──► (Compensates for 0.55 monospace font height/width skew)
       │
       ▼
2. Grayscale & Contrast     ──► (Luminance Y = 0.299R + 0.587G + 0.114B with contrast scaling)
       │
       ▼
3. Vector Quantization      ──► (NumPy maps 0–255 pixel values to sorted character density indices)
       │
       ▼
4. Style / Color Passes     ──► (Assign glyphs from selected ramp & encode RGB spans)
       │
       ▼
[ Output Formats ]          ──► (.txt, HTML viewport, or Canvas-rendered .png / .jpg)
```

---

## 🚀 Quick Start (Local Setup)

### 1. Clone the Repository
```bash
git clone https://github.com/MuhammadAsad29/ASCII-Art-Generator.git
cd ASCII-Art-Generator
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
python app.py
```

Open your browser and navigate to:
```text
http://localhost:5000
```

---

## ☁️ Deployment (Vercel)

This repository is fully configured for **Vercel Serverless Python**:

1. Push your code to GitHub.
2. Sign in to [Vercel](https://vercel.com) using your GitHub account.
3. Click **Add New...** &rarr; **Project** and import `ASCII-Art-Generator`.
4. Click **Deploy** (no extra configuration or credit card needed).

---

## 📂 Project Architecture

```text
ASCII Art Generator/
├── ascii_engine.py      # Core computer vision pipeline & character quantization
├── app.py               # Flask REST API endpoints and web server
├── vercel.json          # Vercel serverless deployment routing config
├── Procfile             # Production process definition for Gunicorn deployment
├── requirements.txt     # Optimized headless production dependencies
├── .gitignore           # Git ignore configuration
├── README.md            # Project documentation
└── templates/
    └── index.html       # Single-page reactive UI (HTML5, Vanilla CSS & Canvas)
```

---

## 🛠️ Tech Stack

- **Backend**: Flask 3.0, Gunicorn, Vercel Serverless Python
- **Image Processing**: OpenCV Headless, NumPy, Pillow
- **Frontend**: Vanilla HTML5, Modern CSS3 (Dark Mode), HTML5 Canvas API

---

## 📄 License

This project is licensed under the MIT License.

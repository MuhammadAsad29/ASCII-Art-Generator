<div align="center">

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
  - Monospace font aspect ratio compensation ($1:0.55$).
  - Instant brightness inversion toggle.
- 💾 **Multi-Format Export**:
  - **Plain Text (`.txt`)**: Raw characters ready for terminals and text editors.
  - **Image (`.png` / `.jpg`)**: Pixel-perfect canvas export at native font resolution with preserved background and color.
  - **One-Click Clipboard Copy**: Instant copy for sharing.

---

## 📐 How It Works

Traditional raster images are converted to ASCII using a 5-stage mathematical pipeline:

```
[ Input Photo ]
       │
       ▼
1. Aspect Ratio Correction  ──► (Compensates for 0.55 monospace font height/width skew)
       │
       ▼
2. Grayscale & Contrast     ──► (Luminance Y = 0.299R + 0.587G + 0.114B with CLAHE/scaling)
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

```
http://localhost:5000
```

---

## ☁️ Zero-Cost Cloud Deployment (Render.com)

This repository is pre-configured for **100% free cloud deployment** without needing a credit card:

1. Push your code to GitHub.
2. Sign in to [Render.com](https://render.com) using your GitHub account.
3. Click **New +** $\rightarrow$ **Web Service**.
4. Connect your `ASCII-Art-Generator` repository.
5. Set the following build configurations:
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Instance Type**: **Free ($0/month)**
6. Click **Deploy Web Service**.

> **Note**: Uses `opencv-python-headless` to eliminate missing Linux graphics library errors (`libGL.so`) on cloud containers.

---

## 📂 Project Architecture

```
ASCII Art Generator/
├── ascii_engine.py      # Core computer vision pipeline & character quantization
├── app.py               # Flask REST API endpoints and web server
├── Procfile             # Production process definition for Gunicorn deployment
├── requirements.txt     # Optimized headless production dependencies
├── .gitignore           # Git ignore configuration
└── templates/
    └── index.html       # Single-page reactive UI (HTML5, Vanilla CSS & Canvas)
```

---

## 🛠️ Tech Stack

- **Backend**: [Flask 3.0](https://flask.palletsprojects.com/), [Gunicorn](https://gunicorn.org/)
- **Image Processing**: [OpenCV Headless](https://pypi.org/project/opencv-python-headless/), [NumPy](https://numpy.org/), [Pillow](https://python-pillow.org/)
- **Frontend**: Vanilla HTML5, Modern CSS3 (Dark Mode / Glassmorphism), HTML5 Canvas API

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

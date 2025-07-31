Sure! Here's the **updated `README.md`** with clear instructions to download all **three required model files**, including the exact GitHub links under the `model/` section:

---

```markdown
# 🎨 PaintBack

**AI-Powered Color for the Moments that Matter.**  
*Because every memory deserves a splash of color.*

PaintBack brings your grayscale photos back to life using artificial intelligence. With just one click, you can transform your black-and-white images into vibrant memories—either by uploading a photo or using your webcam.

---

## 📸 Demo



---

## 🚀 Features

✅ Upload grayscale photos and get colorized results  
✅ Real-time webcam colorization using AI    
✅ Download the colorized image  
  

---
## 📂 File Structure

```

.
├── colorization.py
├── model/
│   ├── colorization\_deploy\_v2.prototxt
│   ├── colorization\_release\_v2.caffemodel
│   └── pts\_in\_hull.npy
├── requirements.txt
├── README.md

````

---

## 🧠 How It Works

This app uses a pretrained deep learning model from [OpenCV’s colorization project](https://github.com/richzhang/colorization) trained on the ImageNet dataset. The core technique includes:

- Converting grayscale to LAB color space
- Inferring ab channels using a deep neural network
- Merging the original L (lightness) with predicted ab (color) channels
- Outputting a BGR color image

---

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/jyothikaveeramalla/Image-colorization.git
cd Image-colorization
````

### 2. Install the requirements

```bash
pip install -r requirements.txt
```

---

## 📥 Download Model Files

You’ll need to manually download three model files and place them inside a `model/` directory.

### 📁 Create this folder structure:

```
colorization/
└── model/
    ├── colorization_deploy_v2.prototxt
    ├── colorization_release_v2.caffemodel
    └── pts_in_hull.npy
```

### 📎 Download links:

* [`colorization_deploy_v2.prototxt`](https://github.com/richzhang/colorization/blob/master/models/colorization_deploy_v2.prototxt)
* [`colorization_release_v2.caffemodel`](https://github.com/richzhang/colorization/blob/master/models/colorization_release_v2.caffemodel)
* [`pts_in_hull.npy`](https://github.com/richzhang/colorization/blob/master/resources/pts_in_hull.npy)

You can either:

* **Right-click → Save as** the files directly from GitHub, or
* **Clone the model repo**:

  ```bash
  git clone https://github.com/richzhang/colorization
  ```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 📜 License

This project is open-source under the [MIT License](LICENSE).

---

## ✨ Credits

Built with 💖 by Jyothika (https://github.com/jyothikaveeramalla)
Colorization Model by [Richard Zhang et al.](https://github.com/richzhang/colorization)

---

> “PaintBack - Because every black and white photo deserves its color story.”

```




## 🎨 PaintBack

**AI-Powered Color for the Moments that Matter.**  
*Because every memory deserves a splash of color.*

---

## ✨ Features

- Upload and colorize grayscale images
- Live webcam colorization using AI
- Download the colorized output
- Simple, interactive Streamlit interface
- AI model from OpenCV's deep colorization project

---

## 🧠 How It Works

PaintBack uses a deep learning model trained on the ImageNet dataset to colorize black-and-white images:

1. Grayscale image is converted to LAB color space.
2. A deep neural network predicts the `ab` color components.
3. The `L` (lightness) channel from the original image is merged with predicted `ab` to reconstruct a color image.
4. The LAB image is converted back to RGB/BGR for display.

---

## 🛠️ Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/jyothikaveerramalla/Image_colorization.git
   cd Image_colourization
````

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## 📥 Download Model Files

Create a folder named `model/` in the root directory and download the following three files:

* [`colorization_deploy_v2.prototxt`](https://github.com/richzhang/colorization/blob/master/models/colorization_deploy_v2.prototxt)
* [`colorization_release_v2.caffemodel`](https://github.com/richzhang/colorization/blob/master/models/colorization_release_v2.caffemodel)
* [`pts_in_hull.npy`](https://github.com/richzhang/colorization/blob/master/resources/pts_in_hull.npy)

Save them inside the `model/` directory:

```
colorization.py/
└── model/
    ├── colorization_deploy_v2.prototxt
    ├── colorization_release_v2.caffemodel
    └── pts_in_hull.npy
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Then open your browser to: `http://localhost:8501/`

---

## 👏 Credits

* Built with ❤️ using [OpenCV Colorization Models](https://github.com/richzhang/colorization)
* UI powered by Streamlit
* Developed by Jyothika(https://github.com/jyothikaveeramalla)

```

```

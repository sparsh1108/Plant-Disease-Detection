This project implements an **AI-powered Plant Disease Detection System** using **Transfer Learning** with **MobileNetV2**.

The model classifies plant leaf images into **38 different disease and healthy classes** from the PlantVillage dataset.

The project demonstrates the complete deep learning workflow including:

- Transfer Learning
- Feature Extraction
- Fine-Tuning
- Data Preprocessing
- Performance Evaluation
- Confusion Matrix
- Classification Report

---



**Dataset:** PlantVillage Dataset

- 🌿 38 Classes
- 🍅 Tomato Diseases
- 🥔 Potato Diseases
- 🌶 Pepper Diseases
- 🍎 Apple Diseases
- 🍇 Grape Diseases
- 🌽 Corn Diseases
- Healthy Plant Leaves

---

## 🧠 Model Architecture

```text
Input Image (224×224×3)
            │
            ▼
      MobileNetV2
(ImageNet Pretrained)
            │
            ▼
 GlobalAveragePooling2D
            │
            ▼
 Dense (256, ReLU)
            │
         Dropout
            │
            ▼
 Dense (128, ReLU)
            │
         Dropout
            │
            ▼
 Dense (38, Softmax)
```

---

## 🚀 Techniques Used

- ✅ Transfer Learning
- ✅ Feature Extraction
- ✅ Fine-Tuning
- ✅ EarlyStopping
- ✅ ModelCheckpoint
- ✅ Image Preprocessing
- ✅ TensorFlow Dataset API
- ✅ Classification Report
- ✅ Confusion Matrix

---

## 📊 Model Performance

| Metric | Value |
|---------|------:|
| Validation Accuracy | **97.98%** |
| Validation Loss | **0.059** |
| Classes | **38** |



## 📋 Classification Report

```text
Validation Accuracy : 97.98%

Precision : 98%

Recall : 98%

F1 Score : 98%
```

---

## 🛠 Tech Stack

- Python
- TensorFlow
- Keras
- NumPy
- Matplotlib
- Scikit-Learn
- OpenCV

---


## 🎯 Future Improvements

- Deploy using Streamlit
- Convert model to TensorFlow Lite
- Real-time disease detection
- Mobile application
- Explainable AI using Grad-CAM

---

## 📚 Learning Outcomes

During this project I learned:

- Transfer Learning
- MobileNetV2 Architecture
- Feature Extraction
- Fine-Tuning
- Image Classification
- Deep Learning Optimization
- Evaluation Metrics
- TensorFlow Data Pipeline

---


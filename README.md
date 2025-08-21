# covid19-facemask-detection-yolo
Smart Face Mask Detection with YOLOv8, built for real-time applications in developing countries to ensure COVID-19 safety compliance.


---

## 🧾 Overview
This project applies **YOLOv8 (You Only Look Once)** for real-time **face mask detection**, classifying faces into three categories:
- ✅ **Mask** (properly worn)  
- ❌ **No Mask**  
- ⚠️ **Bad Mask** (improperly worn, e.g., under nose or chin)  

Face mask compliance has been a critical public health concern during the COVID-19 pandemic, particularly in **developing countries like Nigeria**, where monitoring resources are limited.  
This project demonstrates how **AI and computer vision** can be leveraged to provide **low-cost, real-time solutions** that improve safety in public spaces, schools, hospitals, and transport systems.  

---

## ✨ Features
- Trained with a custom dataset (Mask, No Mask, Bad Mask)  
- Real-time detection on images, videos, and webcams  
- Lightweight — suitable for deployment on resource-constrained devices  
- **Flask web app** for live monitoring  

---

## 📂 Dataset
The dataset was custom-curated and annotated with three classes:
- `mask`  
- `no_mask`  
- `bad_mask`  

Dataset is available on [Roboflow](https://roboflow.com/) (or replace with your dataset link).  

---

## 🏋️ Training
yolo detect train data=data/data.yaml model=yolov8n.pt epochs=100 imgsz=640

---

## 📊 Validation
yolo detect val model=models/best.pt data=data/data.yaml

---

##🎯 Inference
# Single image
yolo detect predict model=models/best.pt source=test.jpg  

# Folder of images
yolo detect predict model=models/best.pt source=path/to/images/  

# Webcam
yolo detect predict model=models/best.pt source=0  

---

## ⚙️ Installation
Clone the repository:
```bash
git clone https://github.com/centbueze/covid19-facemask-detection-yolo.git
cd covid19-facemask-detection-yolo
pip install -r requirements.txt

pip install -r requirements.txt

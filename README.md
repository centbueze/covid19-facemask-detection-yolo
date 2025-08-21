# covid19-facemask-detection-yolo
Smart Face Mask Detection with YOLOv8, built for real-time applications in developing countries to ensure COVID-19 safety compliance.


# Face Mask Detection with YOLOv8  
Real-time mask compliance detection for public health in developing regions.  

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
- Extendable to **ESP32-CAM** or **Flask web app** for live monitoring  

---

## 📂 Dataset
The dataset was custom-curated and annotated with three classes:
- `mask`  
- `no_mask`  
- `bad_mask`  

Dataset is available on [Roboflow](https://roboflow.com/) (or replace with your dataset link).  

---

## ⚙️ Installation
Clone the repository:
```bash
git clone https://github.com/centbueze/covid19-facemask-detection-yolo.git
cd covid19-facemask-detection-yolo
pip install -r requirements.txt

pip install -r requirements.txt

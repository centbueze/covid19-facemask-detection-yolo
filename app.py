from flask import Flask, render_template, request, send_from_directory
from ultralytics import YOLO
import os
import cv2
import uuid

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load YOLOv8 model
model = YOLO("C:/Users/user/Desktop/test/ultralytics-cpu/runs/detect/train3/weights/best.pt")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "image" not in request.files:
            return "No image uploaded"
        
        file = request.files["image"]
        if file.filename == "":
            return "No file selected"
        
        # Save image
        filename = str(uuid.uuid4()) + ".jpg"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Run YOLOv8 prediction
        results = model.predict(source=filepath, conf=0.25, verbose=False)
        annotated_img = results[0].plot()

        # Save annotated result
        output_path = os.path.join(app.config['UPLOAD_FOLDER'], "pred_" + filename)
        cv2.imwrite(output_path, annotated_img)

        return render_template("index.html", original=filename, prediction="pred_" + filename)
    
    return render_template("index.html")

@app.route('/static/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True)

from ultralytics import YOLO
from PIL import Image
import os

model = YOLO("yolov8n.pt")

def detect_people(image_path, output_dir="outputs"):
    os.makedirs(output_dir, exist_ok=True)

    results = model(image_path)
    result = results[0]

    person_count = 0

    for box in result.boxes:
        cls_id = int(box.cls[0].item())
        class_name = model.names[cls_id]
        if class_name == "person":
            person_count += 1

    output_path = os.path.join(output_dir, "result.jpg")
    plotted = result.plot()
    Image.fromarray(plotted[..., ::-1]).save(output_path)

    return {
        "person_count": person_count,
        "output_image": output_path
    }
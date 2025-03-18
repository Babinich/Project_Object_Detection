from ultralytics import YOLO

model = YOLO('runs/detect/train/weights/best.pt')

# Validate with a custom dataset
metrics = model.val(data="datasets\yolo_dataset\data_yolo.yaml")
print(metrics.box.map) 
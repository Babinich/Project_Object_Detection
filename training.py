from ultralytics import YOLO

if __name__ == "__main__":
    # Training the model
    model = YOLO("yolo11m.pt")
    results = model.train(
        data="datasets/yolo_dataset/data_yolo.yaml",
        epochs=100,
        imgsz=640,
        device=0,
        patience=10,
        batch=-1
    )
    

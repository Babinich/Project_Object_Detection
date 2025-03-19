import os

# Specify the folder name or path
dataset_coco_path = "datasets/coco_dataset"
dataset_yolo_path = "datasets/yolo_dataset"

images_path = os.path.join(dataset_yolo_path, "images")
annotations_path =  os.path.join(dataset_yolo_path, "labels")

# folders for storying the data splits
first_folder = ["images", "labels", "train", "val"]
second_folder = ["images", "labels"]

# Create the folder
os.makedirs(dataset_coco_path, exist_ok=True)

for folder in first_folder:
    path = os.path.join(dataset_yolo_path, folder)
    os.makedirs(path, exist_ok=True)

for folder in first_folder[2:]:
    path = os.path.join(dataset_yolo_path, folder)
    for subfolder in second_folder:
        extended_path =  os.path.join(path, subfolder)
        os.makedirs(extended_path, exist_ok=True)
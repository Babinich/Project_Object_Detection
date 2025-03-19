# Project: Object Detection - YOLOv11

## Environment Specifications
- Python version: 3.10.11
- pip version: 25.0.1

## Running the Repository:
1. Run `folder_structure.py`
   - Creates missing folders where images and annotations will be saved.
2. Run `coco_annotation.ipynb`
   - Uses `annotations.json` from the TACO dataset and creates a `annotations_coco.json` file in the `datasets/coco_dataset` folder.
3. Run `download.py`
   - Downloads the data using `annotations_coco.json` and saves images in `datasets/yolo_dataset/images`.
4. Run `coco_to_yolo.ipynb`
   - Converts COCO annotations to YOLO format and saves them in `datasets/yolo_dataset/labels`.
5. Run `splitting.py`
   - Splits the dataset into training (`datasets/yolo_dataset/train`) and validation (`datasets/yolo_dataset/val`) sets.
6. Run `training.py`
   - Trains the model and creates a folder called `runs/detect/train`.
7. Run `validation.py`
   - Runs the validation and saves results in `runs/detect/val`.

## Intro
In this project, I utilized the pretrained YOLOv11m model to detect two object classes: glass bottles and drinking cans.
The primary goal was to gain hands-on experience rather than to achieve top-tier results, as the fine-tuning process was carried out using a limited dataset of just 100 images.

## Dataset
For this project, I had the option of either manually labeling and creating my own custom dataset or using an already annotated dataset. After some consideration, I decided to use the TACO dataset. The only required file was `annotations.json` from the TACO dataset, which can be found [here](https://github.com/pedropro/TACO/blob/master/data/annotations.json).

The file was encoded in the COCO format, with annotations for 60 different classes. For this project, I focused on detecting category IDs 12 (drink can) and 6 (glass bottle). I ensured that the dataset was balanced (50 images per label, for a total of 100 images). There were 83 annotations for drink cans and 71 annotations for glass bottles (`coco_annotation.ipynb`). 

After that, I downloaded the selected images using `download.py`. I then converted the COCO annotations to YOLO format using `coco_to_yolo.ipynb`. No major preprocessing was done aside from adjusting the number of decimal places for bounding boxes and the data augmentation performed by YOLOv11m by default.

Finally, I performed a train-validation split with an 80/20 ratio.

## Model
For training, I used the YOLOv11m model (which can be downloaded [here](https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo11m.pt)). The following hyperparameters were set:
- `epochs = 100`
- `imgsz = 640`
- `patience = 10`

The most important hyperparameter is `patience`. It allows for early stopping to avoid wasting resources and overfitting the model.

## Results
Given that the training set consisted of only 80 images, the model was highly prone to overfitting. After just three epochs, both the mAP50 and mAP50-95 began rapidly dropping. The model showed poor generalization, with spiky `val/cls_loss` values. However, as mentioned earlier, the goal was not to achieve high results.

The results of running the model with the best weights (i.e., after two epochs) are saved in the `results` folder. Additionally, this folder contains the model's predictions on the validation set.

### Parameters Across Epochs:
![image](https://github.com/user-attachments/assets/c74ae13c-8b5e-41c5-851b-a7603ed8b90e)


### Labeled Image:
![image](https://github.com/user-attachments/assets/a9a7f8cf-ac2e-4615-a082-e5976fb4c7d6)

### Predictions:
![image](https://github.com/user-attachments/assets/48694fc0-c22f-48ca-a61c-8a0010f1abf5)






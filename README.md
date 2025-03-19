# Project Object Datection - YOLOv11

## Enviroment specification
- Python version: 3.10.11
- pip version: 25.0.1

## Running the repository:
1. Run folder_structure.py
  - Creates missing folders where  images and annotations will be saved at.
2. Run coco_annotation.ipynb
  - Uses annotations.json from taco_dataset and creates a COCO annotations_coco.json in coco_dataset.
3. Run download.py
  - Downloads the data using annotations_coco.json and saves images at "datasets/yolo_dataset/images".
4. Run coco_to_yolo.ipynb
  - Creates annotations for all images and saves them at "datasets/yolo_dataset/labels"
5. Run splitting.py
  - Splits the data into train ("datasets/yolo_dataset/train") and validation ("datasets/yolo_dataset/val") sets.
6. Run training.py
  - Trains the model and creates folder "runs/detect/train"
7. Run validation.py
  - Runs the validation and saves results at "runs/detect/val"


## Intro
In this project, I utilized the pretrained YOLOv11m model to detect two object classes: glass bottles and drinking cans. 
The primary goal was to gain hands-on experience rather than to achieve top-tier results, as the fine-tuning process was carried out using a limited dataset of just 100 images.

## Dataset
In this project I was given an option of choosing between manually labeling and creating my own custom dataset or use an alredy annotated dataset. After some considerations I decided on TACO dataset.
The only needed file was a a file called: "annotions.json" (https://github.com/pedropro/TACO/blob/master/data/annotations.json). 

The file was encoded in COCO format, having all images annotated with 60 different classes. For this project I focused on detection of category ids 12 (drink can) and 6 (glass bottle). 
I made sure that the data set was balanced (50 images per label, together 100 images. 83 annotations for drink cans and 71 annotations for glass bottles) (coco_annotation.ipynb). 
Then I downloaded the chosen images (download.py).
I changed the COCO format to YOLO format (coco_to_yolo.ipynb). No major preprocessign was done besides fixing number of decimal places for bboxes and data augmentation performed by YOLOv11m on default.
After that I did train-validation split with 80/20 ratio.

## Model
For training I used YOLOv11m (https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo11m.pt) for training. For hyperparameters I set:
- epochs = 100
- imgsz = 640
- patience = 10

The most important hyperparameter is patience. It allows for eaaly stopping so we avoid waisting resources and overfitting the model.

## Results 
As the having only 80 images in training, the model was highly prone to overfiting. Just after three eppochs the mAP50 and mAP50-95 started rappidly dropping. The model was poor at generalization 
(spiky val/cls_loss). However, as said previously I did not aim for high results. The results of runnign best weights (model after running two eppochs) is saved at folder results. Additionally,
this folder contains the predictions of the model on validation set. 

# Parameters accross epochs:
![image](https://github.com/user-attachments/assets/c74ae13c-8b5e-41c5-851b-a7603ed8b90e)

# Labaled image
![image](https://github.com/user-attachments/assets/cb536e36-c760-4774-9a31-d01e8adcab9e)

# Predicttions







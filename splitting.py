import os
from sklearn.model_selection import train_test_split
import shutil

path_yolo = "datasets/yolo_dataset"

images_path = os.path.join(path_yolo, "images")
annotations_path =  os.path.join(path_yolo, "labels")

# Read images and annotations
images = [os.path.join(images_path, x) for x in os.listdir(images_path)]
annotations = [os.path.join(annotations_path, x) for x in os.listdir(annotations_path) if x[-3:] == "txt"]

images.sort()
annotations.sort()

len(annotations), len(os.listdir(images_path))

# Split the dataset into train-valid-test splits 
train_images, val_images, train_annotations, val_annotations = train_test_split(images, annotations, test_size = 0.2, random_state = 1)

#Utility function to move images 
def move_files_to_folder(list_of_files, destination_folder):
    for f in list_of_files:
        try:
            shutil.move(f, destination_folder)
        except:
            print(f)
            assert False


# destiantions for images
train_images_dest = os.path.join(path_yolo, "train/images")
val_images_dest = os.path.join(path_yolo, "val/images")

# destiantions for annotations
train_ann_dest = os.path.join(path_yolo, "train/labels")
val_ann_dest = os.path.join(path_yolo, "val/labels")


# Move the splits into their folders
move_files_to_folder(train_images,train_images_dest)
move_files_to_folder(val_images, val_images_dest)

move_files_to_folder(train_annotations, train_ann_dest)
move_files_to_folder(val_annotations, val_ann_dest)

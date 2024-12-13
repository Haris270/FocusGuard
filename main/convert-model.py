
#  import YOLO from ultralytics
from ultralytics import YOLO

# Load the YOLO v.11 nano Model
model = YOLO("yolo11n.pt")

# Export the model as NCNN format
model.export(format = "ncnn")




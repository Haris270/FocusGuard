import cv2  # OpenCV library for Image & Video Processing
import time
from picamera2 import Picamera2  # Library for working with the Camera Module 3
from ultralytics import YOLO  # YOLO library for object detection
from gpiozero import Buzzer

from trigger_alarm import trigger_alarm

# Initialize the PiCamera2 instance
picam2 = Picamera2()

# Configure the Camera Resolution & Format
picam2.preview_configuration.main.size = (1280, 1280)  # set the resolution
picam2.preview_configuration.main.format = "RGB888"  # set the image format
picam2.preview_configuration.align()  # align the configurations
picam2.configure("preview")  # set the preview mode
picam2.start()  # start the camera

# load the converted NCNN format YOLO model
model = YOLO("yolo11n_ncnn_model")

detection_timestamps = []
ALARM_TRIGGER_COUNT = 3
ALARM_SPAN_SECONDS = 8

# Main loop for capturing frames & detecting objects
while True:
    frame = picam2.capture_array()  # Capture the current frame

    results = model.predict(frame, conf=0.4, show=True, verbose=False)  # make prediction

    # Iterate through the detection results
    for result in results:
        for box in result.boxes:  # Iterate through each bounding box
            class_id = int(box.cls)  # get the class ID for the detected object
            confidence = float(box.conf)  # get the detection confidence score

            if class_id == 67:  # Class ID for cell phone is 67 in COCO dataset (which YOLO is trained on)
                print("Cell Phone Detected!")
                detection_timestamps.append(time.time())  # Add current timestamp

    # Remove timestamps older than current the ALARM_SPAN_SECONDS
    current_time = time.time()
    detection_timestamps = [t for t in detection_timestamps if current_time - t <= ALARM_SPAN_SECONDS]

    # check if detection exceeds trigger count
    if len(detection_timestamps) > ALARM_TRIGGER_COUNT:
        print("distraction!")
        trigger_alarm()
        detection_timestamps.clear()  # Reset after the alarm

    # Get an annotated frame with bounding boxes and labels
    annotated_frame = results[0].plot()

    # Calculate FPS based on inference time
    inference_time = results[0].speed['inference']
    fps = 1000 / inference_time

    # Add FPS info to the Visible Frame
    text = f'FPS : {fps:.1f}'
    font = cv2.FONT_HERSHEY_SIMPLEX
    text_size = cv2.getTextSize(text, font, 1, 2)[0]
    text_x = annotated_frame.shape[1] - text_size[0] - 10
    text_y = text_size[1] + 10

    cv2.putText(annotated_frame, text, (text_x, text_y), font, 1, (255, 255, 255))

    # Display the Annotated Frame
    cv2.imshow("Camera", annotated_frame)

    # Break if 'q' key is pressed
    if cv2.waitKey(1) == ord("q"):
        break

# Close display window
cv2.destroyAllWindows()




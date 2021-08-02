import cv2

from ultrafastLaneDetector import UltrafastLaneDetector, ModelType

model_path = "models/tusimple_18.pth"
model_type = ModelType.TUSIMPLE
use_gpu = False

# Initialize lane detection model
lane_detector = UltrafastLaneDetector(model_path, model_type, use_gpu)

# Initialize webcam
cap = cv2.VideoCapture(0)
cv2.namedWindow("Detected lanes", cv2.WINDOW_NORMAL)

while(True):
    ret, frame = cap.read()

    # Detect the lanes
    output_img = lane_detector.detect_lanes(frame)

    
    cv2.imshow("Detected lanes", output_img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


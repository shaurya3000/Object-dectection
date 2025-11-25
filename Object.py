from ultralytics import YOLO
import cv2
import base64
import time



model = YOLO("yolov8n.pt")


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Cannot access webcam")
    exit()


frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = 20.0  


fourcc = cv2.VideoWriter_fourcc(*'MJPG')
video_out = cv2.VideoWriter('AI vision .avi', fourcc, fps, (frame_width, frame_height))

print("🚀 AI vision Real-Time Detection started! Press Q to quit.")

detected_ids = []

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLO tracking on the frame
    results = model.track(frame, conf=0.5, verbose=False, persist=True, tracker="bytetrack.yaml")

    
    for r in results:
        if r.boxes and r.boxes.id is not None:
            for box in r.boxes:
                detected_class = model.names[int(box.cls)]
                detected_id = int(box.id)
                
                
    
                
    # Draw detections on the frame
    annotated_frame = results[0].plot()

    
    video_out.write(annotated_frame)

    
    cv2.imshow("AI Vision", annotated_frame)

    # Exit on Q key
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
video_out.release()
cv2.destroyAllWindows()
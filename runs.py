from ultralytics import YOLO
import cv2
# Load mô hình YOLOv8 pre-trained
model = YOLO('yolov8n.pt')
# Mở camera
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Không mở được camera!")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        break
    # Dự đoán với YOLOv8
    results = model(frame)
    # Xử lý các bounding box chỉ cho lớp "person"
    for result in results:
        boxes = result.boxes
        for box in boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            if model.names[cls_id] == "person":
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 000, 0), 2)
                label = f"{model.names[cls_id]} {conf:.2f}"
                cv2.putText(frame, label, (x1, y1 - 5),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("YOLOv8 - Phát hiện người", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# pip install ultralytics opencv-python

from ultralytics import YOLO
import cv2

def load_model(model_path: str = "yolov11m.pt"):
    """
    Load YOLOv11 model và gộp tất cả label thành 'foot'
    """
    model = YOLO(model_path)
    # Lấy names gốc
    orig_names = model.model.names
    # Nếu names là list thì tạo list mới, nếu là dict thì tạo dict mới
    if isinstance(orig_names, (list, tuple)):
        model.model.names = ['foot'] * len(orig_names)
    else:
        model.model.names = {i: "foot" for i in orig_names.keys()}
    return model

def detect_from_camera(model,
                       conf: float = 0.25,
                       iou: float = 0.45,
                       target_size: tuple = None):
    """
    Chạy inference real-time, vẽ bounding box với label 'foot'
    """
    cap = cv2.VideoCapture(1)
    if not cap.isOpened():
        print("Không mở được webcam!")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if target_size is not None:
            frame = cv2.resize(frame, target_size)

        # Chạy inference
        results = model.predict(
            source=frame,
            conf=conf,
            iou=iou,
            stream=False
        )
        # Vẽ và hiển thị (tất cả box đều hiển thị 'foot')
        annotated = results[0].plot()
        cv2.imshow("YOLOv11 Foot Detection", annotated)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    model = load_model("yolov11m.pt")
    # Nếu muốn resize khung hình xuống 640×360 để tăng tốc, truyền target_size=(640, 360)
    detect_from_camera(model, conf=0.1, iou=0.45, target_size=None)

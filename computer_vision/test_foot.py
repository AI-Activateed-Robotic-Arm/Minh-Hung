# 1. Cài đặt dependencies (chạy 1 lần)
# pip install ultralytics huggingface_hub opencv-python

from huggingface_hub import hf_hub_download
from ultralytics import YOLO
import cv2

def download_model():
    # Tải về file .pt từ repo HuggingFace
    return hf_hub_download(
        repo_id="AunyMoons/loras-pack",
        filename="foot-yolov8l.pt"
    )

def load_model(model_path: str):
    # Load YOLOv8 model
    return YOLO(model_path)

def infer_image(model, img_path: str,
                target_size: tuple = (640, 360),
                conf: float = 0.25, iou: float = 0.45):
    # 1. Đọc ảnh gốc
    img = cv2.imread(img_path)
    # 2. Resize về kích thước mong muốn
    img_small = cv2.resize(img, target_size)
    # 3. Chạy inference trên ảnh đã resize
    results = model.predict(
        source=img_small,
        conf=conf,       # ngưỡng confidence
        iou=iou,         # ngưỡng NMS IoU
        save=False       # nếu muốn lưu ảnh kết quả, để True
    )
    # 4. Vẽ bounding boxes và hiển thị
    img_res = results[0].plot()
    cv2.imshow("YOLOv8 Inference (Resized)", img_res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def infer_webcam(model,
                 target_size: tuple = (640, 360),
                 conf: float = 0.25, iou: float = 0.45):
    cap = cv2.VideoCapture(1)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        # Resize mỗi frame
        frame_small = cv2.resize(frame, target_size)
        # Inference
        results = model.predict(
            source=frame_small,
            conf=conf,
            iou=iou,
            save=False,
            stream=False
        )
        # Vẽ và hiển thị
        out = results[0].plot()
        cv2.imshow("Webcam YOLOv8 (Resized)", out)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # 1. Download và load model
    model_file = download_model()
    model = load_model('test.pt')

    # 2. Inference trên ảnh tĩnh (đã resize)
    img_path = "img.png"  # đổi thành đường dẫn ảnh của bạn
    # infer_image(model, img_path, target_size=(480, 270))

    # 3. (Tuỳ chọn) Inference real-time từ webcam (nhấn 'q' để thoát)
    infer_webcam(model, target_size=(480, 270))

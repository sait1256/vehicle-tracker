import cv2
from ultralytics import YOLO
import supervision as sv

def main():
    # Model yükle
    model = YOLO("yolo11n.pt")

    # Tracker ve annotator ayarla
    tracker = sv.ByteTrack()
    box_annotator = sv.BoxAnnotator()
    label_annotator = sv.LabelAnnotator()

    # Kamerayı aç
    cap = cv2.VideoCapture("video.mp4")

    print("Araç takibi başladı! Çıkmak için 'q' tuşuna bas.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Sadece araçları tespit et (car=2, truck=7, bus=5, motorcycle=3)
        results = model(frame, classes=[2, 3, 5, 7], verbose=False)[0]

        # Tespitleri supervision formatına çevir
        detections = sv.Detections.from_ultralytics(results)

        # Takip et
        detections = tracker.update_with_detections(detections)

        # Etiket oluştur
        labels = [f"#{tracker_id}" for tracker_id in detections.tracker_id]

        # Çiz
        frame = box_annotator.annotate(frame, detections)
        frame = label_annotator.annotate(frame, detections, labels)

        # Araç sayısını yaz
        cv2.putText(frame, f"Arac Sayisi: {len(detections)}", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("Arac Takibi", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
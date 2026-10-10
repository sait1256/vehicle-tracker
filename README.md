# Gerçek Zamanlı Araç Takibi 🚗

YOLO11 ve ByteTrack algoritması ile gerçek zamanlı araç tespiti ve takibi.

## 🎯 Özellikler
- Gerçek zamanlı araç tespiti
- Her araca özel ID atama
- Araç sayısı takibi
- Drone/İHA görüntülerinde çalışır

## 🛠️ Kullanılan Teknolojiler
- Python 3.13
- PyTorch 2.6 (CUDA 12.4)
- Ultralytics YOLO11
- Supervision (ByteTrack)
- OpenCV
- NVIDIA RTX 4050 GPU

## 📁 Proje Yapısı
```
vehicle-tracker/
├── tracker.py     # Ana takip kodu
└── README.md
```

## ⚙️ Kurulum
```bash
pip install ultralytics opencv-python supervision
```

## 🏃 Kullanım

### Kamera ile:
```bash
python tracker.py
```

### Video ile:
`tracker.py` dosyasında şu satırı değiştir:
```python
cap = cv2.VideoCapture("video.mp4")
```

## 📌 Tespit Edilen Araçlar
- 🚗 Araba
- 🚌 Otobüs
- 🚛 Kamyon
- 🏍️ Motosiklet
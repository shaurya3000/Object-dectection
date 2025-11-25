# OBJECT DECTECTION – Real-Time Object Detection using YOLOv8 + ByteTrack

This project implements a *real-time object detection and tracking system* using *YOLOv8 (Ultralytics)* and *ByteTrack*.  
The system uses a webcam feed to detect objects such as people, chairs, bottles, laptops, etc., and displays bounding boxes, class names, and confidence values in real time.

---

## 🚀 Features

- Real-time object detection using *YOLOv8n*
- Object tracking using *ByteTrack*
- Smooth bounding box overlays using Ultralytics built-in plot()
- Saves output video (AI vision.avi)
- Works on any webcam
- Lightweight and runs on CPU or GPU

---

## 📌 Requirements

Install dependencies:

```bash
pip install ultralytics opencv-python
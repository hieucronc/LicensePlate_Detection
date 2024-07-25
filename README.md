# **Hệ thống Nhận Diện Biển Số Xe sử dụng YOLOv8 và EasyOCR**
![image](https://github.com/user-attachments/assets/0f95559f-2f6b-486b-9260-4c7a08838224)
Sử dụng Python để nhận diện biển số xe trong ảnh bằng YOLO và trích xuất văn bản từ biển số đó bằng EasyOCR.
## Cài đặt
Clone repo.
Cài đặt các thư viện:
```Bash
pip install -r requirements.txt
```

```Bash
python main.py
```
Bạn có thể thay thế input_image_path trong file main.py bằng đường dẫn đến ảnh của bạn.

## Lưu ý
Mô hình YOLO hiện tại chỉ được huấn luyện để nhận diện biển số xe Việt Nam có định dạng vuông (2 dòng). Do đó, mô hình có thể gặp khó khăn trong việc nhận diện các biển số dài (1 dòng).
# License Plate Recognition using YOLO and EasyOCR

This repository contains Python code for detecting license plates in images using YOLO object detection and extracting text from the detected license plate using EasyOCR.

## Table of Contents

- [Overview](#overview)
- [Setup](#setup)
- [Usage](#usage)


## Overview

This project demonstrates how to use YOLO (You Only Look Once) for license plate detection and EasyOCR for text extraction. YOLO is a state-of-the-art, real-time object detection system, and EasyOCR is a deep learning-based OCR tool that supports multiple languages.

The workflow includes:
- Loading a pre-trained YOLO model for object detection.
- Detecting the license plate in an input image and cropping it.
- Applying EasyOCR to recognize and extract text from the cropped license plate.

## Setup

1. Clone the repository.
2. Install dependencies:
```bash
pip install -r requirements.txt
```
## Usage:
Replace input_image_path in the main.py script with the path to your input image.

```bash
python main.py
```
The script will:

Detect the license plate in the image.

Display the cropped license plate region.

Extract and print the recognized text from the license plate.

## Limitations of the Model
The current YOLO model is specifically trained for Vietnamese square license plates (two lines). As a result, it may struggle to accurately (can't) detect other license plate formats, such as long rectangular, (single-line) plates.


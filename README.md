# Small-Object-Detection-Benchmarks-FullImageVsGOIS

## **Quick Steps for COCO Evaluation**

This benchmark evaluates **Full Image Inference** vs. **Guided-Object Inference with Slicing (GOIS)** for small object detection using COCO metrics. Results are based on a subset of 970 images (15%) from the **VisDrone-2019-Train** dataset.
### **1. Clone the Repository**
Clone this repository to access the required files:
git clone https://github.com/MMUZAMMUL/Small-Object-Detection-Benchmarks-Full_ImageVsGOIS.git
cd Small-Object-Detection-Benchmarks-Full_ImageVsGOIS
## **Instructions**:
1. pip install pycocotools    .
2. Open evaluation.py        .
3. Update the paths:            .
Ground Truth Path: Set the path for Ground_Truth.json & Prediction Path: Download the prediction .json file for either Full Image or GOIS benchmarks and set its path..
4. Run python evaluation.py

---

# Full Image Inference Results with Seven Different Models

| Model           | Download Link                                                                                     | mAP@0.50:0.95 | mAP@0.50 | mAP@0.75 | mAP-Small | mAP-Medium | mAP-Large | AR@1 | AR@10 | AR@100 | AR-Small | AR-Medium | AR-Large | F1 Score |
|-----------------|--------------------------------------------------------------------------------------------------|---------------|----------|----------|-----------|------------|-----------|------|-------|--------|----------|-----------|----------|----------|
| YOLO11          | [Download](https://github.com/MMUZAMMUL/Small-Object-Detection-Benchmarks-Full_ImageVsGOIS/releases/download/yolo11/FI_yolo11n.json)  | 0.12          | 0.43     | 0.12     | 0.02      | 0.14       | 0.18      | 0.23 | 0.27  | 0.29   | 0.04     | 0.49      | 1.09     | 0.17     |
| RT-DETR-L       | [Download](https://github.com/MMUZAMMUL/Small-Object-Detection-Benchmarks-Full_ImageVsGOIS/releases/download/RT-DETRv1/FI_rtder-l.json) | 0.18          | 0.67     | 0.17     | 0.56      | 0.20       | 0.27      | 0.34 | 0.42  | 1.01   | 0.44     | 1.44      | 2.45     | 0.61     |
| YOLOv10         | [Download](https://github.com/MMUZAMMUL/Small-Object-Detection-Benchmarks-Full_ImageVsGOIS/releases/download/yolov10-v1/FI_yolov10n.json) | 0.13          | 0.44     | 0.13     | 0.45      | 0.14       | 0.19      | 0.23 | 0.29  | 0.27   | 0.02     | 0.38      | 1.18     | 0.17     |
| YOLOv9          | [Download](https://github.com/MMUZAMMUL/Small-Object-Detection-Benchmarks-Full_ImageVsGOIS/releases/download/Yolov9-v1/FI_YOLOv9c.json)  | 0.02          | 0.11     | 0.02     | 0.06      | 0.03       | 0.03      | 0.04 | 0.04  | 0.02   | 0.17     | 0.12      | 0.22     | 0.52     |
| YOLOv8n         | [Download](https://github.com/MMUZAMMUL/Small-Object-Detection-Benchmarks-Full_ImageVsGOIS/releases/download/Yolov8-v1/FI_yolov8n.json)  | 0.23          | 0.67     | 0.18     | 0.72      | 0.24       | 0.32      | 0.42 | 0.46  | 0.41   | 0.10     | 0.50      | 1.22     | 0.19     |
| YOLOv5n         | [Download](https://github.com/MMUZAMMUL/Small-Object-Detection-Benchmarks-Full_ImageVsGOIS/releases/download/Yolov5-v1/FI_yolov5su.json)  | 0.57          | 1.34     | 0.63     | 1.33      | 0.54       | 0.79      | 0.90 | 1.01  | 1.18   | 1.20     | 1.51      | 2.22     | 1.79     |
| YOLOv8s-WorldV2 | [Download](https://github.com/MMUZAMMUL/Small-Object-Detection-Benchmarks-Full_ImageVsGOIS/releases/download/yolo8world-v1/FI_yolov8s-worldv2.json) | 0.12          | 0.32     | 0.13     | 0.30      | 0.15       | 0.16      | 0.21 | 0.42  | 0.46   | 0.11     | 0.75      | 1.79     | 0.30     |


# Guided-Object Inference Slicing (GOIS) Results with Seven Different Models

| Model           | Download Link                                                                                          | mAP@0.50:0.95 | mAP@0.50 | mAP@0.75 | mAP-Small | mAP-Medium | mAP-Large | AR@1 | AR@10 | AR@100 | AR-Small | AR-Medium | AR-Large | F1 Score |
|-----------------|------------------------------------------------------------------------------------------------------|---------------|----------|----------|-----------|------------|-----------|------|-------|--------|----------|-----------|----------|----------|
| YOLO11          | [Download](https://github.com/MMUZAMMUL/Small-Object-Detection-Benchmarks-Full_ImageVsGOIS/releases/download/GOIS-YOLO11/GOIS_yolo11n.json) | 0.33          | 0.51     | 0.34     | 0.10      | 0.57       | 0.96      | 0.27 | 0.68  | 0.87   | 0.33     | 1.40      | 1.93     | 0.47     |
| RT-DETR-L       | [Download](https://github.com/MMUZAMMUL/Small-Object-Detection-Benchmarks-Full_ImageVsGOIS/releases/download/GOIS-RT/GOIS_rtdetr-l.json)       | 0.61          | 0.94     | 0.63     | 0.22      | 0.95       | 1.49      | 0.46 | 1.16  | 1.71   | 1.03     | 2.25      | 2.73     | 0.90     |
| YOLOv10         | [Download](https://github.com/MMUZAMMUL/Small-Object-Detection-Benchmarks-Full_ImageVsGOIS/releases/download/GOIS-Yolo10/GOIS_yolov10n.json)    | 0.31          | 0.48     | 0.33     | 0.08      | 0.56       | 0.93      | 0.26 | 0.61  | 0.76   | 0.27     | 1.25      | 1.85     | 0.44     |
| YOLOv9          | [Download](https://github.com/MMUZAMMUL/Small-Object-Detection-Benchmarks-Full_ImageVsGOIS/releases/download/GOIS-YOLO9/GOIS_YOLOv9c.json)      | 0.53          | 0.76     | 0.58     | 0.18      | 0.90       | 1.18      | 0.40 | 0.91  | 1.16   | 0.53     | 1.79      | 2.21     | 0.73     |
| YOLOv8n         | [Download](https://github.com/MMUZAMMUL/Small-Object-Detection-Benchmarks-Full_ImageVsGOIS/releases/download/GOIS-YOLO8/GOIS_yolov8n.json)      | 0.30          | 0.47     | 0.32     | 0.13      | 0.53       | 0.97      | 0.28 | 0.67  | 0.84   | 0.39     | 1.34      | 1.93     | 0.44     |
| YOLOv5n         | [Download](https://github.com/MMUZAMMUL/Small-Object-Detection-Benchmarks-Full_ImageVsGOIS/releases/download/GOIS-YOLO5/GOIS_yolov5su.json)     | 0.38          | 0.58     | 0.41     | 0.16      | 0.65       | 1.02      | 0.29 | 0.71  | 0.93   | 0.51     | 1.44      | 1.93     | 0.54     |
| YOLOv8s-WorldV2 | [Download](https://github.com/MMUZAMMUL/Small-Object-Detection-Benchmarks-Full_ImageVsGOIS/releases/download/GOIS-YOLOWORLD/GOIS_yolov8s-worldv2.json) | 0.40          | 0.60     | 0.43     | 0.16      | 0.68       | 1.01      | 0.36 | 0.84  | 1.03   | 0.48     | 1.59      | 1.97     | 0.58     |



# Percentage(%age) improvement achived by GOIS over Full image 

***
| Metric         | YOLO11 %↑ | RT-DETR-L %↑ | YOLOv10 %↑ | YOLOv9 %↑ | YOLOv8n %↑ | YOLOv5n %↑ | YOLOv8s-WorldV2 %↑ |
| -------------- | --------- | ------------ | ---------- | --------- | ---------- | ---------- | ------------------- |
| mAP@0.50:0.95  | 175.0     | 41.86        | 158.33     | 29.27     | 114.29     | 111.11     | 73.91               |
| mAP@0.50       | 183.33    | 40.3         | 182.35     | 35.71     | 135.0      | 114.81     | 76.47               |
| mAP@0.75       | 161.54    | 43.18        | 153.85     | 28.89     | 128.57     | 115.79     | 86.96               |
| mAP-Small      | 400.0     | 100.0        | 300.0      | 200.0     | 325.0      | 433.33     | 300.0               |
| mAP-Medium     | 147.83    | 41.79        | 211.11     | 25.0      | 120.83     | 103.13     | 61.9                |
| mAP-Large      | 68.42     | 11.19        | 47.62      | -11.28    | 79.63      | 29.11      | 12.22               |
| AR@1           | 125.0     | 43.75        | 100.0      | 33.33     | 86.67      | 81.25      | 71.43               |
| AR@10          | 151.85    | 43.21        | 144.0      | 40.0      | 131.03     | 97.22      | 100.0               |
| AR@100         | 200.0     | 69.31        | 181.48     | 58.9      | 162.5      | 126.83     | 123.91              |
| AR-Small       | 725.0     | 134.09       | 1250.0     | 211.76    | 875.0      | 410.0      | 336.36              |
| AR-Medium      | 185.71    | 56.25        | 228.95     | 49.17     | 168.0      | 114.93     | 112.0               |
| AR-Large       | 77.06     | 11.43        | 56.78      | -0.45     | 58.2       | 27.81      | 10.06               |
| F1 Score       | 176.47    | 47.54        | 158.82     | 40.38     | 131.58     | 116.0      | 93.33               |



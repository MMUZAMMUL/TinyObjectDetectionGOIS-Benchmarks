# Tiny Object Dectection-Benchmarks-FullImage Vs GOIS [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/<USERNAME>/<REPOSITORY>/blob/<BRANCH>/<PATH_TO_NOTEBOOK>)
BY MUZAMMUL(ZJU)
# Enhancing Tiny Object Detection Without Fine-Tuning: Dynamic Adaptive Guided Object Inference Slicing Framework with Latest YOLO Models and RT-DETR Transformer
Here is a demonstration video for the project:

[![Watch the video](assets/321.png)](https://youtu.be/T5t5eb_w0S4)
(https://youtu.be/T5t5eb_w0S4)


## **Quick Steps for COCO Evaluation**

This benchmark evaluates **Full Image Inference Detection** vs. ** Dynamic Adaptive Guided-Object Inference Slicing (GOIS)** for small object detection using COCO metrics. Results are based on a subset of 970 images (15%) from the **VisDrone-2019-Train** dataset.
### **1. Clone the Repository**
Clone this repository to access the required files:[clone] (https://github.com/MMUZAMMUL/Small-Object-Detection-Benchmarks-Full_ImageVsGOIS.git)
cd Small-Object-Detection-Benchmarks-Full_ImageVsGOIS
## **Instructions**:
1. pip install pycocotools    .
2. Open evaluation.py        .
3. Update the paths:            .
Ground Truth Path: Set the path for Ground_Truth & Prediction Path: Download the prediction .json file for either Full Image or GOIS benchmarks and set its path..
4. Run python evaluation.py

---

# Full Image Inference Results with Seven Different Models

| Model           | Predictions-Link                                                                                     | mAP@0.50:0.95 | mAP@0.50 | mAP@0.75 | mAP-Small | mAP-Medium | mAP-Large | AR@1 | AR@10 | AR@100 | AR-Small | AR-Medium | AR-Large | F1 Score |
|-----------------|--------------------------------------------------------------------------------------------------|---------------|----------|----------|-----------|------------|-----------|------|-------|--------|----------|-----------|----------|----------|
| YOLO11          | [Download](https://github.com/MMUZAMMUL/Small-Object-Detection-Benchmarks-Full_ImageVsGOIS/releases/download/yolo11/FI_yolo11n.json)  | 0.12          | 0.18     | 0.13     | 0.02      | 0.23       | 0.57      | 0.12 | 0.27  | 0.29   | 0.04     | 0.49      | 1.09     | 0.17     |
| RT-DETR-L       | [Download](https://github.com/MMUZAMMUL/Small-Object-Detection-Benchmarks-Full_ImageVsGOIS/releases/download/RT-DETRv1/FI_rtder-l.json) | 0.43          | 0.67     | 0.44     | 0.11      | 0.67       | 1.34      | 0.32 | 0.81  | 1.01   | 0.44     | 1.44      | 2.45     | 0.61     |
| YOLOv10         | [Download](https://github.com/MMUZAMMUL/Small-Object-Detection-Benchmarks-Full_ImageVsGOIS/releases/download/yolov10-v1/FI_yolov10n.json) | 0.12          | 0.17     | 0.13     | 0.02      | 0.18       | 0.63      | 0.13 | 0.25  | 0.27   | 0.02     | 0.38      | 1.18     | 0.17     |
| YOLOv9          | [Download](https://github.com/MMUZAMMUL/Small-Object-Detection-Benchmarks-Full_ImageVsGOIS/releases/download/Yolov9-v1/FI_YOLOv9c.json)  | 0.41          | 0.56     | 0.45     | 0.06      | 0.72       | 1.33      | 0.30 | 0.65  | 0.73   | 0.17     | 1.20      | 2.22     | 0.52     |
| YOLOv8n         | [Download](https://github.com/MMUZAMMUL/Small-Object-Detection-Benchmarks-Full_ImageVsGOIS/releases/download/Yolov8-v1/FI_yolov8n.json)  | 0.14          | 0.20     | 0.14     | 0.03      | 0.24       | 0.54      | 0.15 | 0.29  | 0.32   | 0.04     | 0.50      | 1.22     | 0.19     |
| YOLOv5n         | [Download](https://github.com/MMUZAMMUL/Small-Object-Detection-Benchmarks-Full_ImageVsGOIS/releases/download/Yolov5-v1/FI_yolov5su.json)  | 0.18          | 0.27     | 0.19     | 0.03      | 0.32       | 0.79      | 0.16 | 0.36  | 0.41   | 0.10     | 0.67      | 1.51     | 0.25     |
| YOLOv8s-WorldV2 | [Download](https://github.com/MMUZAMMUL/Small-Object-Detection-Benchmarks-Full_ImageVsGOIS/releases/download/yolo8world-v1/FI_yolov8s-worldv2.json) | 0.23          | 0.34     | 0.23     | 0.04      | 0.42       | 0.90      | 0.21 | 0.42  | 0.46   | 0.11     | 0.75      | 1.79     | 0.30     |



# Guided-Object Inference Slicing (GOIS) Results with Seven Different Models

| Model           | Predictions-Link                                                                                            | mAP@0.50:0.95 | mAP@0.50 | mAP@0.75 | mAP-Small | mAP-Medium | mAP-Large | AR@1 | AR@10 | AR@100 | AR-Small | AR-Medium | AR-Large | F1 Score |
|-----------------|------------------------------------------------------------------------------------------------------|---------------|----------|----------|-----------|------------|-----------|------|-------|--------|----------|-----------|----------|----------|
| YOLO11          | [Download](https://github.com/MMUZAMMUL/Small-Object-Detection-Benchmarks-Full_ImageVsGOIS/releases/download/GOIS-YOLO11/GOIS_yolo11n.json) | 0.33          | 0.51     | 0.34     | 0.10      | 0.57       | 0.96      | 0.27 | 0.68  | 0.87   | 0.33     | 1.40      | 1.93     | 0.47     |
| RT-DETR-L       | [Download](https://github.com/MMUZAMMUL/Small-Object-Detection-Benchmarks-Full_ImageVsGOIS/releases/download/GOIS-RT/GOIS_rtdetr-l.json)       | 0.61          | 0.94     | 0.63     | 0.22      | 0.95       | 1.49      | 0.46 | 1.16  | 1.71   | 1.03     | 2.25      | 2.73     | 0.90     |
| YOLOv10         | [Download](https://github.com/MMUZAMMUL/Small-Object-Detection-Benchmarks-Full_ImageVsGOIS/releases/download/GOIS-Yolo10/GOIS_yolov10n.json)    | 0.31          | 0.48     | 0.33     | 0.08      | 0.56       | 0.93      | 0.26 | 0.61  | 0.76   | 0.27     | 1.25      | 1.85     | 0.44     |
| YOLOv9          | [Download](https://github.com/MMUZAMMUL/Small-Object-Detection-Benchmarks-Full_ImageVsGOIS/releases/download/GOIS-YOLO9/GOIS_YOLOv9c.json)      | 0.53          | 0.76     | 0.58     | 0.18      | 0.90       | 1.18      | 0.40 | 0.91  | 1.16   | 0.53     | 1.79      | 2.21     | 0.73     |
| YOLOv8n         | [Download](https://github.com/MMUZAMMUL/Small-Object-Detection-Benchmarks-Full_ImageVsGOIS/releases/download/GOIS-YOLO8/GOIS_yolov8n.json)      | 0.30          | 0.47     | 0.32     | 0.13      | 0.53       | 0.97      | 0.28 | 0.67  | 0.84   | 0.39     | 1.34      | 1.93     | 0.44     |
| YOLOv5n         | [Download](https://github.com/MMUZAMMUL/Small-Object-Detection-Benchmarks-Full_ImageVsGOIS/releases/download/GOIS-YOLO5/GOIS_yolov5su.json)     | 0.38          | 0.58     | 0.41     | 0.16      | 0.65       | 1.02      | 0.29 | 0.71  | 0.93   | 0.51     | 1.44      | 1.93     | 0.54     |
| YOLOv8s-WorldV2 | [Download](https://github.com/MMUZAMMUL/Small-Object-Detection-Benchmarks-Full_ImageVsGOIS/releases/download/GOIS-YOLOWORLD/GOIS_yolov8s-worldv2.json) | 0.40          | 0.60     | 0.43     | 0.16      | 0.68       | 1.01      | 0.36 | 0.84  | 1.03   | 0.48     | 1.59      | 1.97     | 0.58     |




# Percentage(%age) improvement achived by GOIS over Full image 
****
| Model            | mAP@0.50:0.95 %↑ | mAP@0.50 %↑ | mAP@0.75 %↑ | mAP-Small %↑ | mAP-Medium %↑ | mAP-Large %↑ | AR@1 %↑ | AR@10 %↑ | AR@100 %↑ | AR-Small %↑ | AR-Medium %↑ | AR-Large %↑ | F1 Score %↑ |
|------------------|------------------|-------------|-------------|--------------|---------------|--------------|---------|----------|-----------|-------------|--------------|-------------|-------------|
| YOLO11           | 175.0           | 183.33      | 161.54      | 400.0        | 147.83        | 68.42        | 125.0   | 151.85   | 200.0     | 725.0       | 185.71       | 77.06       | 176.47      |
| RT-DETR-L        | 41.86           | 40.3        | 43.18       | 100.0        | 41.79         | 11.19        | 43.75   | 43.21    | 69.31     | 134.09      | 56.25        | 11.43       | 47.54       |
| YOLOv10          | 158.33          | 182.35      | 153.85      | 300.0        | 211.11        | 47.62        | 100.0   | 144.0    | 181.48    | 1250.0      | 228.95       | 56.78       | 158.82      |
| YOLOv9           | 29.27           | 35.71       | 28.89       | 200.0        | 25.0          | -11.28       | 33.33   | 40.0     | 58.9      | 211.76      | 49.17        | -0.45       | 40.38       |
| YOLOv8n          | 114.29          | 135.0       | 128.57      | 333.33       | 120.83        | 79.63        | 86.67   | 131.03   | 162.5     | 875.0       | 168.0        | 58.2        | 131.58      |
| YOLOv5n          | 111.11          | 114.81      | 115.79      | 433.33       | 103.12        | 29.11        | 81.25   | 97.22    | 126.83    | 410.0       | 114.93       | 27.81       | 116.0       |
| YOLOv8s-WorldV2  | 73.91           | 76.47       | 86.96       | 300.0        | 61.9          | 12.22        | 71.43   | 100.0    | 123.91    | 336.36      | 112.0        | 10.06       | 93.33       |




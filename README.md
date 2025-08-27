### License

[**MIT License**](LICENSE) - All rights reserved to the author. This project may be used for study and educational purposes, but **redistribution, redevelopment, or use of the code for personal or commercial purposes is strictly prohibited without the author's written consent.**

# Enhancing Tiny Object Detection by applying Guided Object Inference Slicing(GOIS) Complete Benchmarks Evaluated results
 [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](Guided_Object_Inference_Slicing_Prediction_Vs_Full_Image_Prediction_Evaluation.ipynb)

## Testing Code Steps for Section 1,2,3

### 1. **Download Required Files**
- **Ground Truth (GT)**: Download the COCO.json file containing the ground truth annotations.
- **FI-Det COCO.json**: Download the Full Inference Detection results in COCO.json format.
- **OGIS-Det COCO.json**: Download the Object Guided Inference Slicing Detection results in COCO.json format.
- Upload the files to your preferred storage location (e.g., Google Drive).
- Follow step 6,7 in 
# Section 1: Without Fine Tuning 15% Dataset Subset(970 Images) Inference Results VisDrone2019Train Dataset

## Comparative Results for FI-Det and GOIS-Det
This table presents the Average Precision (AP) and Average Recall (AR) metrics for seven models. Each model includes rows for FI-Det, GOIS-Det, and the percentage improvement achieved by GOIS over FI-Det. Downloadable links for FI-Det and GOIS-Det results are included. Ground Truth COCO for this evaluation is available at | [15% Train Dataset GT](https://github.com/MMUZAMMUL/TinyObjectDetectionGOIS-Benchmarks/blob/main/Ground_Trouth-COCO.json)

| **Model** | **AP-Small** | **AR-Small** | **AP-Medium** | **AP-Large** | **AR@1** | **AR@10** | **AR@100** | **AR-Medium** | **AR-Large** | **mAP@0.95** | **mAP@0.50** | **mAP@0.75** |
|----------------|---------------|--------------|----------------|---------------|----------|-----------|------------|---------------|--------------|-------------------|--------------|--------------|
| **YOLO11** [FI-Det](https://github.com/MMUZAMMUL/Small-Object-Detection-Benchmarks-Full_ImageVsGOIS/releases/download/yolo11/FI_yolo11n.json), [GOIS-Det](https://github.com/MMUZAMMUL/Small-Object-Detection-Benchmarks-Full_ImageVsGOIS/releases/download/GOIS-YOLO11/GOIS_yolo11n.json) | 0.002 / 0.01 | 0.004 / 0.033 | 0.023 / 0.057 | 0.057 / 0.096 | 0.012 / 0.027 | 0.027 / 0.068 | 0.029 / 0.087 | 0.049 / 0.14 | 0.109 / 0.193 | 0.012 / 0.033 | 0.018 / 0.051 | 0.013 / 0.034 |
| **% Improve** | **↑ 388.07%** | **↑ 718.09%** | **↑ 152.67%** | **↑ 69.75%** | **↑ 128.48%** | **↑ 154.67%** | **↑ 194.56%** | **↑ 188.51%** | **↑ 77.16%** | **↑ 164.89%** | **↑ 183.25%** | **↑ 160.64%** |
| **RT-DETR-L** [FI-Det](https://github.com/MMUZAMMUL/Small-Object-Detection-Benchmarks-Full_ImageVsGOIS/releases/download/RT-DETRv1/FI_rtder-l.json), [GOIS-Det](https://github.com/MMUZAMMUL/Small-Object-Detection-Benchmarks-Full_ImageVsGOIS/releases/download/GOIS-RT/GOIS_rtdetr-l.json) | 0.011 / 0.022 | 0.044 / 0.103 | 0.067 / 0.095 | 0.134 / 0.149 | 0.032 / 0.046 | 0.081 / 0.116 | 0.101 / 0.171 | 0.144 / 0.225 | 0.245 / 0.273 | 0.043 / 0.061 | 0.067 / 0.094 | 0.044 / 0.063 |
| **% Improve** | **↑ 103.75%** | **↑ 135.04%** | **↑ 42.48%** | **↑ 10.79%** | **↑ 40.91%** | **↑ 42.27%** | **↑ 68.99%** | **↑ 55.97%** | **↑ 11.44%** | **↑ 41.08%** | **↑ 39.79%** | **↑ 43.49%** |
| **YOLOv10** [FI-Det](https://github.com/MMUZAMMUL/Small-Object-Detection-Benchmarks-Full_ImageVsGOIS/releases/download/yolov10-v1/FI_yolov10n.json), [GOIS-Det](https://github.com/MMUZAMMUL/Small-Object-Detection-Benchmarks-Full_ImageVsGOIS/releases/download/GOIS-Yolo10/GOIS_yolov10n.json) | 0.002 / 0.008 | 0.002 / 0.027 | 0.018 / 0.056 | 0.063 / 0.093 | 0.013 / 0.026 | 0.025 / 0.061 | 0.027 / 0.076 | 0.038 / 0.125 | 0.118 / 0.185 | 0.012 / 0.031 | 0.017 / 0.048 | 0.013 / 0.033 |
| **% Improve** | **↑ 445.53%** | **↑ 1052.31%** | **↑ 202.98%** | **↑ 49.03%** | **↑ 101.74%** | **↑ 141.36%** | **↑ 182.78%** | **↑ 231.55%** | **↑ 56.42%** | **↑ 155.67%** | **↑ 181.62%** | **↑ 158.41%** |
| **YOLOv8n** [FI-Det](https://github.com/MMUZAMMUL/Small-Object-Detection-Benchmarks-Full_ImageVsGOIS/releases/download/Yolov8-v1/FI_yolov8n.json), [GOIS-Det](https://github.com/MMUZAMMUL/Small-Object-Detection-Benchmarks-Full_ImageVsGOIS/releases/download/GOIS-YOLO8/GOIS_yolov8n.json) | 0.003 / 0.013 | 0.004 / 0.039 | 0.024 / 0.053 | 0.054 / 0.097 | 0.015 / 0.028 | 0.029 / 0.067 | 0.032 / 0.084 | 0.05 / 0.134 | 0.122 / 0.193 | 0.014 / 0.03 | 0.02 / 0.047 | 0.014 / 0.032 |
| **% Improve** | **↑ 360.46%** | **↑ 805.84%** | **↑ 121.22%** | **↑ 79.27%** | **↑ 80.94%** | **↑ 128.38%** | **↑ 159.81%** | **↑ 167.54%** | **↑ 58.05%** | **↑ 120.03%** | **↑ 138.30%** | **↑ 133.27%** |
| **YOLOv8s-WorldV2** [FI-Det](https://github.com/MMUZAMMUL/Small-Object-Detection-Benchmarks-Full_ImageVsGOIS/releases/download/yolo8world-v1/FI_yolov8s-worldv2.json), [GOIS-Det](https://github.com/MMUZAMMUL/Small-Object-Detection-Benchmarks-Full_ImageVsGOIS/releases/download/GOIS-YOLOWORLD/GOIS_yolov8s-worldv2.json) | 0.004 / 0.016 | 0.011 / 0.048 | 0.042 / 0.068 | 0.090 / 0.101 | 0.021 / 0.036 | 0.042 / 0.084 | 0.046 / 0.103 | 0.075 / 0.159 | 0.179 / 0.197 | 0.023 / 0.040 | 0.034 / 0.060 | 0.023 / 0.043 |
| **% Improve** | **↑ 287.28%** | **↑ 325.65%** | **↑ 62.42%** | **↑ 11.68%** | **↑ 69.48%** | **↑ 100.75%** | **↑ 125.29%** | **↑ 112.30%** | **↑ 10.25%** | **↑ 77.07%** | **↑ 73.88%** | **↑ 87.13%** |


# Section 2: Fine Tuning Models with 10 epoches Visdrone Traning and then Inference results  on  Full Dataset(6,471 Images) VisDrone2019Train 

## Comparative Results for FI-Det and GOIS-Det
This table presents the Average Precision (AP) and Average Recall (AR) metrics for five models (YOLO11, YOLOv10, YOLOv9, YOLOv8, YOLOv5). Each model includes three rows: FI-Det results, GOIS-Det results, and % improvement achieved by GOIS. Downloadable links for FI-Det and GOIS-Det results are included in the first column next to the model name. Ground Truth COCO for this evaluation available at | [FullTraineDatasetGT](https://github.com/MMUZAMMUL/TinyObjectDetectionGOIS-Benchmarks/releases/download/Full-VisdroneTrain-COCO-GT/ground_truth_coco.json)

| **Model**                                                                                      | **AP-Small**        | **AR-Small**        | **AP-Medium**       | **AP-Large**        | **AR@1**           | **AR@10**          | **AR@100**         | **AR-Medium**       | **AR-Large**       | **F1 Score**       | **mAP@0.95** | **mAP@0.50** | **mAP@0.75** |
|------------------------------------------------------------------------------------------------|---------------------|---------------------|---------------------|---------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|----------------------|------------------|------------------|
| YOLO11 [FI-Det](https://github.com/MMUZAMMUL/TinyObjectDetectionGOIS-Benchmarks/releases/download/FT-YOLOv11-FI/Yolo11n_predictions_coco.json)  | 0.024 | 0.035 | 0.159 | 0.283 | 0.045 | 0.112 | 0.137 | 0.208 | 0.349 | 0.170 | 0.120 | 0.171 | 0.119 |
| YOLO11 - [GOIS-Det](https://github.com/MMUZAMMUL/TinyObjectDetectionGOIS-Benchmarks/releases/download/FT-YOLOv11-GOIS/Yolo11n-gois_predictions_coco.json) | 0.071 | 0.133 | 0.164 | 0.151 | 0.053 | 0.152 | 0.207 | 0.273 | 0.227 | 0.470 | 0.134 | 0.192 | 0.132 |
| **% Improvement**                                                                              | **↑ 195.83%** | **↑ 278.66%** | **↑ 3.14%** | **↓ 46.64%** | **↑ 18.81%** | **↑ 35.46%** | **↑ 51.17%** | **↑ 31.44%** | **↓ 34.90%** | **↑ 176.47%** | **↑ 11.67%** | **↑ 12.87%** | **↑ 10.92%** |
| YOLOv10 [FI-Det](https://github.com/MMUZAMMUL/TinyObjectDetectionGOIS-Benchmarks/releases/download/FT-YOLOv10-FI/Yolo10-full_predictions_coco.json) | 0.022 | 0.029 | 0.133 | 0.222 | 0.041 | 0.097 | 0.117 | 0.178 | 0.278 | 0.17 | 0.091 | 0.140 | 0.100 |
| YOLOv10 - [GOIS-Det](https://github.com/MMUZAMMUL/TinyObjectDetectionGOIS-Benchmarks/releases/download/FT-YOLOv10-GOIS/Yolo10-gois_predictions_coco.json) | 0.061 | 0.110 | 0.130 | 0.101 | 0.047 | 0.127 | 0.171 | 0.218 | 0.159 | 0.44 | 0.099 | 0.156 | 0.107 |
| **% Improvement**                                                                              | **↑ 177.27%** | **↑ 279.22%** | **↓ 2.26%** | **↓ 54.95%** | **↑ 14.18%** | **↑ 31.01%** | **↑ 46.09%** | **↑ 22.50%** | **↓ 42.82%** | **↑ 158.82%** | **↑ 8.79%** | **↑ 11.43%** | **↑ 7.00%** |
| YOLOv9 [FI-Det](https://github.com/MMUZAMMUL/TinyObjectDetectionGOIS-Benchmarks/releases/download/FT-YOLOv9-FI/Yolo9-full_predictions_coco.json) | 0.079 | 0.051 | 0.320 | 0.472 | 0.027 | 0.060 | 0.069 | 0.116 | 0.225 | 0.051 | 0.039 | 0.054 | 0.043 |
| YOLOv9 - [GOIS-Det](https://github.com/MMUZAMMUL/TinyObjectDetectionGOIS-Benchmarks/releases/download/FT-YOLOv9-GOIS/Yolo9-gois_predictions_coco.json) | 0.130 | 0.074 | 0.242 | 0.171 | 0.036 | 0.086 | 0.111 | 0.177 | 0.233 | 0.075 | 0.051 | 0.074 | 0.056 |
| **% Improvement**                                                                              | **↑ 64.56%** | **↑ 35.76%** | **↓ 24.38%** | **↓ 63.77%** | **↑ 32.61%** | **↑ 41.88%** | **↑ 59.89%** | **↑ 52.01%** | **↑ 3.89%** | **↑ 59.89%** | **↓ 11.79%** | **↓ 8.39%** | **↓ 14.22%** |
| YOLOv8 [FI-Det](https://github.com/MMUZAMMUL/TinyObjectDetectionGOIS-Benchmarks/releases/download/FT-YOLOv8-FI/Yolo8-full_predictions_coco.json) | 0.025 | 0.032 | 0.158 | 0.290 | 0.046 | 0.113 | 0.136 | 0.209 | 0.365 | 0.17 | 0.108 | 0.168 | 0.118 |
| YOLOv8 - [GOIS-Det](https://github.com/MMUZAMMUL/TinyObjectDetectionGOIS-Benchmarks/releases/download/FT-YOLOv8-GOIS/Yolo8-gois_predictions_coco.json) | 0.070 | 0.044 | 0.163 | 0.149 | 0.056 | 0.158 | 0.211 | 0.281 | 0.220 | 0.082 | 0.121 | 0.193 | 0.130 |
| **% Improvement**                                                                              | **↑ 180.00%** | **↑ 140.15%** | **↑ 3.16%** | **↓ 48.62%** | **↑ 22.33%** | **↑ 40.05%** | **↑ 55.92%** | **↑ 34.65%** | **↓ 39.72%** | **↑ 168.36%** | **↑ 12.04%** | **↑ 14.88%** | **↑ 10.17%** |
| YOLOv5 [FI-Det](https://github.com/MMUZAMMUL/TinyObjectDetectionGOIS-Benchmarks/releases/download/FT-YOLOv5-FI/Yolo5-full_predictions_coco.json) | 0.019 | 0.026 | 0.138 | 0.270 | 0.040 | 0.098 | 0.119 | 0.178 | 0.278 | 0.17 | 0.096 | 0.150 | 0.104 |
| YOLOv5 - [GOIS-Det](https://github.com/MMUZAMMUL/TinyObjectDetectionGOIS-Benchmarks/releases/download/FT-YOLOv5-GOIS/Yolo5-gois_predictions_coco.json) | 0.059 | 0.040 | 0.150 | 0.134 | 0.050 | 0.139 | 0.188 | 0.254 | 0.205 | 0.070 | 0.109 | 0.174 | 0.116 |
| **% Improvement**                                                                              | **↑ 210.53%** | **↑ 188.07%** | **↑ 8.70%** | **↓ 50.37%** | **↑ 26.22%** | **↑ 42.71%** | **↑ 58.12%** | **↑ 40.05%** | **↓ 37.62%** | **↑ 193.98%** | **↑ 13.54%** | **↑ 16.00%** | **↑ 11.54%** |


# Section 3: NO Fine Tuning Five Models Inference results  on Full Dataset(6,471 Images) VisDrone2019Train 
his table presents the Average Precision (AP) and Average Recall (AR) metrics for five models (YOLO11, YOLOv10, YOLOv9, YOLOv8, YOLOv5). Each model includes three rows: FI-Det results, GOIS-Det results, and % improvement achieved by GOIS. Downloadable links for FI-Det and GOIS-Det results are included in the first column next to the model name. Ground Truth COCO for this evaluation available at | [FullTraineDatasetGT](https://drive.google.com/file/d/1-xQ6z7Yx0y3pZp_TZpbWjbM4VrbQ4yL0/view?usp=drive_link)
| **Model**                                                                                      | **AP-Small** | **AR-Small** | **AP-Medium** | **AP-Large** | **AR@1** | **AR@10** | **AR@100** | **AR-Medium** | **AR-Large** | **F1 Score** | **mAP@0.95** | **mAP@0.50** | **mAP@0.75** |
|------------------------------------------------------------------------------------------------|--------------|--------------|---------------|--------------|-----------|-----------|------------|---------------|--------------|--------------|------------------------|------------------|------------------|
| YOLO11 [FI-Det](https://drive.google.com/file/d/1UY5555KzgbNu2Ao4LWKLE2WDNyNZb2Zx/view?usp=drive_link), | 0.024 | 0.035 | 0.159 | 0.283 | 0.045 | 0.112 | 0.137 | 0.208 | 0.349 | 0.170 | 0.120 | 0.171 | 0.119 |
| YOLO11 -[GOIS-Det](https://drive.google.com/file/d/1-9mf-KK9sFkcvMx-RN7NWxA7lsuTFrV6/view?usp=drive_link)                                                                          | 0.071 | 0.133 | 0.164 | 0.151 | 0.053 | 0.152 | 0.207 | 0.273 | 0.227 | 0.470 | 0.134 | 0.192 | 0.132 |
| **% Improvement**                                                                              | **↑ 196.90%** | **↑ 278.66%** | **↑ 2.94%** | **↓ 46.71%** | **↑ 18.81%** | **↑ 35.46%** | **↑ 51.17%** | **↑ 31.44%** | **↓ 34.90%** | **↑ 176.47%** | **↑ 12.01%** | **↑ 12.38%** | **↑ 11.26%** |
| YOLOv10 [FI-Det](https://drive.google.com/file/d/108lw39DbQaNFfLH4hRiXDUPBHN0aMwoq/view?usp=drive_link), | 0.022 | 0.029 | 0.133 | 0.222 | 0.041 | 0.097 | 0.117 | 0.178 | 0.278 | 0.17 | 0.091 | 0.140 | 0.100 |
| YOLOv10 - [GOIS-Det](https://drive.google.com/file/d/10Br73D63gjm_w4EH9IxREcNnS6yM0H0v/view?usp=drive_link)                                                                        | 0.061 | 0.110 | 0.130 | 0.101 | 0.047 | 0.127 | 0.171 | 0.218 | 0.159 | 0.44 | 0.099 | 0.156 | 0.107 |
| **% Improvement**                                                                              | **↑ 176.54%** | **↑ 279.22%** | **↓ 2.30%** | **↓ 54.85%** | **↑ 14.18%** | **↑ 31.01%** | **↑ 46.09%** | **↑ 22.50%** | **↓ 42.82%** | **↑ 158.82%** | **↑ 8.88%** | **↑ 11.40%** | **↑ 7.08%** |
| YOLOv9 [FI-Det](https://drive.google.com/file/d/1-2dQfFQkOwdnUPr0A_Jp7w-88nEtT1QA/view?usp=drive_link),  | 0.039 | 0.051 | 0.070 | 0.139 | 0.027 | 0.060 | 0.069 | 0.116 | 0.225 | 0.051 | 0.039 | 0.054 | 0.043 |
| YOLOv9 -[GOIS-Det](https://drive.google.com/file/d/1-EHJeCZr0s0DFhCVX2DEuHgWCC75dUSD/view?usp=drive_link)                                                                         | 0.051 | 0.074 | 0.089 | 0.125 | 0.036 | 0.086 | 0.111 | 0.177 | 0.233 | 0.075 | 0.051 | 0.074 | 0.056 |
| **% Improvement**                                                                              | **↑ 30.25%** | **↑ 35.76%** | **↑ 26.16%** | **↓ 10.20%** | **↑ 32.61%** | **↑ 41.88%** | **↑ 59.89%** | **↑ 52.01%** | **↑ 3.89%** | **↑ 59.89%** | **↑ 30.25%** | **↑ 35.76%** | **↑ 31.27%** |
| YOLOv8 [FI-Det](https://drive.google.com/file/d/1-3oSVkRHVM-CmMrXSYIMZmCcMdIEfvlx/view?usp=drive_link), [GOIS-Det](https://drive.google.com/file/d/1-HC8p_UA_s0h7MqTHACJF45n4AR658VU/view?usp=drive_link) | 0.012 | 0.029 | 0.022 | 0.061 | 0.013 | 0.028 | 0.030 | 0.048 | 0.124 | 0.029 | 0.012 | 0.018 | 0.012 |
| YOLOv8 - [GOIS-Det](https://drive.google.com/file/d/191eM0XM94iqkdmNvOvkLP0x4qNl_JztT/view?usp=drive_link)                                                                          | 0.029 | 0.044 | 0.051 | 0.092 | 0.026 | 0.065 | 0.082 | 0.134 | 0.191 | 0.082 | 0.029 | 0.044 | 0.030 |
| **% Improvement**                                                                              | **↑ 130.33%** | **↑ 140.15%** | **↑ 131.56%** | **↑ 50.25%** | **↑ 100.68%** | **↑ 132.76%** | **↑ 168.36%** | **↑ 175.62%** | **↑ 53.47%** | **↑ 168.36%** | **↑ 130.33%** | **↑ 140.15%** | **↑ 142.12%** |
| YOLOv5 [FI-Det](https://drive.google.com/file/d/1-8I5JZFhtdRH8lvYAzW-wNjQaRClcpGy/view?usp=drive_link),  | 0.010 | 0.026 | 0.019 | 0.052 | 0.011 | 0.022 | 0.024 | 0.037 | 0.115 | 0.026 | 0.010 | 0.014 | 0.010 |
| YOLOv5 -[GOIS-Det](https://drive.google.com/file/d/191eM0XM94iqkdmNvOvkLP0x4qNl_JztT/view?usp=drive_link)                                                                            | 0.026 | 0.040 | 0.049 | 0.086 | 0.024 | 0.055 | 0.070 | 0.121 | 0.180 | 0.070 | 0.026 | 0.040 | 0.027 |
| **% Improvement**                                                                              | **↑ 166.92%** | **↑ 188.07%** | **↑ 164.97%** | **↑ 66.55%** | **↑ 115.96%** | **↑ 149.03%** | **↑ 193.98%** | **↑ 226.48%** | **↑ 55.92%** | **↑ 193.98%** | **↑ 166.92%** | **↑ 188.07%** | **↑ 171.82%** |

**Notes:**
- ↑ represents percentage improvement achieved by GOIS-Det over FI-Det.
- ↓ represents performance degradation in GOIS-Det compared to FI-Det.







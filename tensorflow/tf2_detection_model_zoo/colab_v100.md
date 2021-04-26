# TensorFlow 2 Detection Model Zoo Benchmarks

## Environment
    
- Colab Pro
- HW
    - CPU: Intel(R) Xeon(R) CPU @ 2.30GHz 4 cores
    - GPU: NVIDIA Tesla P100
    - MEM: 25GB

## Dataset
- [COCO2017](https://cocodataset.org/#home) 

## How to benchmarks

Notebook will be up soon.

## Parameters
- Input batch size: 1

## Results

- All results: [Colab_TF2.4.1_P100.csv](./results/Colab_TF2.4.1_P100.csv)
- Note: CenterNet MobileNetV2 (detection and keypoints) will result in an error inference by the saved model.

## mAP
| Model                               | Input     |   Native FP32 |   TF-TRT FP32 |   TF-TRT FP32+<br>tf_xla_auto_jit=2  |   TF-TRT FP16 |   TF-TRT FP16re+<br>tf_xla_auto_jit=2 |
|:------------------------------------|:----------|--------------:|--------------:|---------------:|--------------:|---------------:|
| CenterNet HourGlass104              | 512x512   |         38.47 |         38.47 |           0    |         38.47 |           0    |
| CenterNet HourGlass104 Keypoints    | 512x512   |         36.73 |         36.73 |           0    |         36.73 |           0    |
| CenterNet HourGlass104              | 1024x1024 |         39.76 |         39.76 |           0    |         39.76 |           0    |
| CenterNet HourGlass104 Keypoints    | 1024x1024 |         38.48 |         38.48 |           0    |         38.48 |           0    |
| CenterNet MobileNetV2 FPN           | nan       |         27.59 |         27.59 |           0    |         27.59 |           0    |
| CenterNet MobileNetV2 FPN Keypoints | nan       |         25.76 |         25.76 |           0    |         25.76 |           0    |
| CenterNet Resnet50 V1 FPN           | 512x512   |         31.28 |         31.28 |           0    |         31.28 |           0    |
| CenterNet Resnet50 V1 FPN Keypoints | 512x512   |         26.23 |         26.23 |           0    |         26.23 |           0    |
| CenterNet Resnet101 V1 FPN          | 512x512   |         24.49 |         24.49 |           0    |         24.49 |           0    |
| CenterNet Resnet50 V2               | 512x512   |          0    |          0    |           0    |          0    |           0    |
| CenterNet Resnet50 V2 Keypoints     | 512x512   |          0    |          0    |           0    |          0    |           0    |
| EfficientDet D0                     | 512x512   |         32.82 |         32.82 |          32.82 |         32.82 |          32.82 |
| EfficientDet D1                     | 640x640   |         36.63 |         36.63 |          36.63 |         36.63 |          36.64 |
| EfficientDet D2                     | 768x768   |         39.84 |         39.84 |          39.84 |         39.84 |          39.85 |
| EfficientDet D3                     | 896x896   |         42.48 |         42.48 |          42.48 |         42.48 |          42.47 |
| EfficientDet D4                     | 1024x1024 |         45.65 |         45.65 |          45.65 |         45.65 |          45.65 |
| EfficientDet D5                     | 1280x1280 |         46.14 |         46.14 |          46.14 |         46.14 |          46.14 |
| EfficientDet D6                     | 1280x1280 |         46.6  |         46.6  |          46.6  |         46.57 |          46.58 |
| EfficientDet D7                     | 1536x1536 |         47.75 |         47.75 |          47.75 |         47.75 |          47.75 |
| SSD MobileNet v2                    | 320x320   |         20.02 |         20.02 |          20.02 |         20.01 |          20.01 |
| SSD MobileNet V1 FPN                | 640x640   |         28.67 |         28.67 |          28.67 |         28.67 |          28.67 |
| SSD MobileNet V2 FPNLite            | 320x320   |         22.1  |         22.1  |          22.1  |         22.1  |          22.09 |
| SSD MobileNet V2 FPNLite            | 640x640   |         27.69 |         27.69 |          27.69 |         27.7  |          27.7  |
| SSD ResNet50 V1 FPN RetinaNet50     | 640x640   |         33.7  |         33.7  |          33.7  |         33.74 |          33.71 |
| SSD ResNet50 V1 FPN RetinaNet50     | 1024x1024 |         37.58 |         37.58 |          37.58 |         37.57 |          37.58 |
| SSD ResNet101 V1 FPN RetinaNet101   | 640x640   |         35.03 |         35.03 |          35.03 |         34.99 |          35.01 |
| SSD ResNet101 V1 FPN RetinaNet101   | 1024x1024 |         38.76 |         38.76 |          38.76 |         38.75 |          38.75 |
| SSD ResNet152 V1 FPN RetinaNet152   | 640x640   |         34.85 |         34.85 |          34.85 |         34.84 |          34.84 |
| SSD ResNet152 V1 FPN RetinaNet152   | 1024x1024 |         38.9  |         38.9  |          38.9  |         38.91 |          38.92 |
| Faster R-CNN ResNet50 V1            | 640x640   |         27.94 |         27.94 |          27.94 |         27.94 |          27.93 |
| Faster R-CNN ResNet50 V1            | 1024x1024 |         30.66 |         30.66 |          30.66 |         30.66 |          30.66 |
| Faster R-CNN ResNet50 V1            | 800x1333  |         26.66 |         26.66 |          26.66 |         26.66 |          26.66 |
| Faster R-CNN ResNet101 V1           | 640x640   |         30.2  |         30.2  |          30.2  |         30.19 |          30.19 |
| Faster R-CNN ResNet101 V1           | 1024x1024 |         36.56 |         36.56 |          36.56 |         36.55 |          36.55 |
| Faster R-CNN ResNet101 V1           | 800x1333  |         31.45 |         31.45 |          31.45 |         31.44 |          31.44 |
| Faster R-CNN ResNet152 V1           | 640x640   |         31.16 |         31.16 |          31.16 |         31.16 |          31.13 |
| Faster R-CNN ResNet152 V1           | 1024x1024 |         36.86 |         36.86 |          36.86 |         36.84 |          36.86 |
| Faster R-CNN ResNet152 V1           | 800x1333  |         32.75 |         32.75 |          32.75 |         32.77 |          32.77 |
| Faster R-CNN Inception ResNet V2    | 640x640   |         36.89 |         36.89 |          36.89 |         36.9  |          36.9  |
| Faster R-CNN Inception ResNet V2    | 1024x1024 |         36.02 |         36.02 |          36.02 |         36.04 |          36.04 |
| Mask R-CNN Inception ResNet V2      | 1024x1024 |         37.94 |         37.94 |          37.93 |         37.98 |          37.98 |

## Latency mean (ms)
| Model                               | Input     |   Native FP32 |   TF-TRT FP32 |   TF-TRT FP32+<br>tf_xla_auto_jit=2  |   TF-TRT FP16 |   TF-TRT FP16re+<br>tf_xla_auto_jit=2 |
|:------------------------------------|:----------|--------------:|--------------:|---------------:|--------------:|---------------:|
| CenterNet HourGlass104              | 512x512   |         67.64 |         66.79 |           0    |         58.05 |           0    |
| CenterNet HourGlass104 Keypoints    | 512x512   |         72.77 |         72.91 |           0    |         63.84 |           0    |
| CenterNet HourGlass104              | 1024x1024 |        174.39 |        174.95 |           0    |        164.7  |           0    |
| CenterNet HourGlass104 Keypoints    | 1024x1024 |        189.25 |        190.4  |           0    |        179.97 |           0    |
| CenterNet MobileNetV2 FPN           | nan       |         25.52 |         25.75 |           0    |         24.9  |           0    |
| CenterNet MobileNetV2 FPN Keypoints | nan       |         29.43 |         29.55 |           0    |         28.69 |           0    |
| CenterNet Resnet50 V1 FPN           | 512x512   |         31.9  |         31.63 |           0    |         30.05 |           0    |
| CenterNet Resnet50 V1 FPN Keypoints | 512x512   |         25    |         25.3  |           0    |         24.31 |           0    |
| CenterNet Resnet101 V1 FPN          | 512x512   |         28.77 |         29.09 |           0    |         28.1  |           0    |
| CenterNet Resnet50 V2               | 512x512   |          0    |          0    |           0    |          0    |           0    |
| CenterNet Resnet50 V2 Keypoints     | 512x512   |          0    |          0    |           0    |          0    |           0    |
| EfficientDet D0                     | 512x512   |        134.86 |        130.41 |         118.78 |        125.47 |         117.93 |
| EfficientDet D1                     | 640x640   |        184.7  |        185.86 |         161.82 |        175.73 |         160.63 |
| EfficientDet D2                     | 768x768   |        252.79 |        243.42 |         216.2  |        244.33 |         211.95 |
| EfficientDet D3                     | 896x896   |        319.18 |        319.89 |         283.64 |        314.55 |         277.34 |
| EfficientDet D4                     | 1024x1024 |        414.85 |        424.16 |         389.43 |        428.63 |         399.02 |
| EfficientDet D5                     | 1280x1280 |        634.91 |        657.84 |         670.11 |        637.22 |         681.11 |
| EfficientDet D6                     | 1280x1280 |        782.6  |        772.02 |         841.98 |        805.51 |         839.73 |
| EfficientDet D7                     | 1536x1536 |        964.21 |        957.81 |         989.46 |        928.26 |         982.72 |
| SSD MobileNet v2                    | 320x320   |         33.75 |         33.87 |          30.34 |         29.47 |          29.9  |
| SSD MobileNet V1 FPN                | 640x640   |        118.59 |        119.39 |         120.69 |        106.72 |         116.68 |
| SSD MobileNet V2 FPNLite            | 320x320   |         53.22 |         54.52 |          55    |         46.41 |          55.31 |
| SSD MobileNet V2 FPNLite            | 640x640   |        111.49 |        110.24 |         117.03 |        102.21 |         116    |
| SSD ResNet50 V1 FPN RetinaNet50     | 640x640   |        127.95 |        127.84 |         128.13 |        107.24 |         117.89 |
| SSD ResNet50 V1 FPN RetinaNet50     | 1024x1024 |        264.94 |        264.82 |         254.73 |        227.36 |         242.4  |
| SSD ResNet101 V1 FPN RetinaNet101   | 640x640   |        137.92 |        139.75 |         136.79 |        111.07 |         124.49 |
| SSD ResNet101 V1 FPN RetinaNet101   | 1024x1024 |        279.92 |        282.07 |         276.59 |        234.74 |         251.01 |
| SSD ResNet152 V1 FPN RetinaNet152   | 640x640   |        304.83 |        144.66 |         141.57 |        112.2  |         125.47 |
| SSD ResNet152 V1 FPN RetinaNet152   | 1024x1024 |         63.95 |        296.69 |         282.58 |        243.92 |         241.66 |
| Faster R-CNN ResNet50 V1            | 640x640   |         76.19 |         67.51 |          64.82 |         54.31 |          53.8  |
| Faster R-CNN ResNet50 V1            | 1024x1024 |         78.61 |         78.9  |          80.23 |         61.45 |          68.35 |
| Faster R-CNN ResNet50 V1            | 800x1333  |         69.69 |         81.46 |         107.47 |         82.88 |         102.85 |
| Faster R-CNN ResNet101 V1           | 640x640   |         90.04 |         72.21 |          67.44 |         53.52 |          56.17 |
| Faster R-CNN ResNet101 V1           | 1024x1024 |        102.49 |         92.29 |          83.48 |         61.31 |          62.34 |
| Faster R-CNN ResNet101 V1           | 800x1333  |         77.54 |        103.6  |         124.98 |        106.49 |         117.2  |
| Faster R-CNN ResNet152 V1           | 640x640   |        107.07 |         81.44 |          80.12 |         55.28 |          61.82 |
| Faster R-CNN ResNet152 V1           | 1024x1024 |        124.24 |        108.71 |          93.43 |         64.5  |          61.47 |
| Faster R-CNN ResNet152 V1           | 800x1333  |        137.98 |        126.27 |         149.62 |        132.89 |         143.15 |
| Faster R-CNN Inception ResNet V2    | 640x640   |        223.62 |        227.39 |         179.37 |         80.42 |          73.48 |
| Faster R-CNN Inception ResNet V2    | 1024x1024 |        262.42 |        263.3  |         242.02 |        141.16 |         143.76 |
| Mask R-CNN Inception ResNet V2      | 1024x1024 |        266.77 |        266.89 |         315.58 |         82.93 |         110.41 |

# Torchvision Object Detection and Instance Segmentation pre-trained model Benchmarks

## Environment

- Local PC
    - SW
        - OS: Fedora 34
        - PyTorch: 1.9.0 (Build from source)
        - Torchvision: 0.10.0 (Build from source)
        - CUDA + cuDNN: 11.4 + 8.2.2
    - HW
        - CPU: AMD Ryzen 7 1700 Eight-Core Processor
        - GPU: NVIDIA GeForce GTX 1070
        - MEM: 32GB
- Colab Pro
    - SW
        - Torch: 1.9.0+cu102
        - Torchvision:  0.10.0+cu102
    - HW
        - CPU: Intel(R) Xeon(R) CPU @ 2.30GHz 4 cores / AMD EPYC 7B12 @ 2.25GHz 4cores
        - GPU: NVIDIA Tesla P100 / NVIDIA Tesla T4
        - MEM: 25GB

## Dataset
- [COCO2017](https://cocodataset.org/#home) 

## How to benchmarks
Source
- https://github.com/NobuoTsukamoto/pytorch-examples/tree/master/python/benchmark

## Results
- [All results](./results)

## mAP

(Measured on a local PC)

| Model                                  |    AP |   AP50 |   AP75 |   APsmall |   APmedium |   APlarge |   ARmax=1 |   ARmax=10 |   ARmax=100 |   ARsmall |   ARmidium |   ARlarge |
|:---------------------------------------|------:|-------:|-------:|----------:|-----------:|----------:|----------:|-----------:|------------:|----------:|-----------:|----------:|
| Faster R-CNN ResNet-50 FPN             | 36.22 |  58.41 |  38.52 |     19.97 |      39.84 |     48.1  |     30.29 |      47.58 |       49.89 |     30.13 |      53.87 |     64.84 |
| Faster R-CNN MobileNetV3-Large FPN     | 32.5  |  52.44 |  33.87 |     12.42 |      35.9  |     50.13 |     28.46 |      42.33 |       44.1  |     19.17 |      49.46 |     64.78 |
| Faster R-CNN MobileNetV3-Large 320 FPN | 22.7  |  37.9  |  23.17 |      2.56 |      21.72 |     44.19 |     21.5  |      28.96 |       29.32 |      3.68 |      29.53 |     56.87 |
| RetinaNet ResNet-50 FPN                | 35.8  |  55.58 |  37.67 |     18.55 |      39.45 |     48.8  |     30.99 |      49.27 |       53.14 |     32.74 |      57.59 |     69.38 |
| SSD300 VGG16                           | 25    |  41.45 |  26.18 |      5.44 |      26.7  |     43.4  |     23.78 |      34.26 |       36.33 |      8.68 |      40.42 |     60.12 |
| SSDlite320 MobileNetV3-Large           | 21.23 |  34.27 |  22.06 |      1.04 |      20.08 |     44.27 |     20.79 |      30.6  |       33.31 |      4.21 |      34.31 |     64.16 |
| Mask R-CNN ResNet-50 FPN               | 37.07 |  58.92 |  39.93 |     20.32 |      40.8  |     49.26 |     31    |      48.63 |       50.96 |     30.8  |      55.12 |     66.53 |

## latency

| Model                                  | NVIDIA GTX1070 (Local PC) | NVIDIA Tesla P100 (Colab) | NVIDIA Tesla T4 (Colab) | Intel Xeon CPU @ 2.3GHz (Colab) | AMD EPYC 7B12 @ 2.25GHz (Colab) |
|:---------------------------------------|--------------------------:|--------------------------:|------------------------:|--------------------------------:|--------------------------------:|
| Faster R-CNN ResNet-50 FPN             |                    122.90 |                     80.13 |                  114.95 |                         4415.93 |                         3510.95 |
| Faster R-CNN MobileNetV3-Large FPN     |                     31.16 |                     20.73 |                   22.16 |                          481.05 |                          296.66 |
| Faster R-CNN MobileNetV3-Large 320 FPN |                     14.94 |                     13.33 |                   14.49 |                          114.34 |                           68.21 |           
| RetinaNet ResNet-50 FPN                |                    126.74 |                     79.92 |                  125.55 |                         4558.58 |                         3373.16 |
| SSD300 VGG16                           |                     32.09 |                     27.97 |                   31.47 |                          624.55 |                          484.80 |
| SSDlite320 MobileNetV3-Large           |                     48.77 |                     47.55 |                   51.10 |                          107.79 |                           75.45 |
| Mask R-CNN ResNet-50 FPN               |                    118.05 |                     81.39 |                  119.06 |                         4390.58 |                         3613.13 |
| Keypoint R-CNN ResNet-50 FPN           |                    117.28 |                     80.80 |                  120.83 |                         4381.79 |                         3642.74 |


## Youtube video

### Faster R-CNN ResNet-50 FPN
[![](https://img.youtube.com/vi/25eX30Jo27c/0.jpg)](https://www.youtube.com/watch?v=25eX30Jo27c)

### Faster R-CNN MobileNetV3-Large FPN
[![](https://img.youtube.com/vi/Q1qFtAdLMYA/0.jpg)](https://www.youtube.com/watch?v=Q1qFtAdLMYA)
    
### Faster R-CNN MobileNetV3-Large 320 FPN
[![](https://img.youtube.com/vi/EHljbZQqnXI/0.jpg)](https://www.youtube.com/watch?v=EHljbZQqnXI)

### RetinaNet ResNet-50 FPN
[![](https://img.youtube.com/vi/1TrPFCAUTa8/0.jpg)](https://www.youtube.com/watch?v=1TrPFCAUTa8)

### SSDlite320 MobileNetV3-Large
[![](https://img.youtube.com/vi/K0bYTvZ0Vs4/0.jpg)](https://www.youtube.com/watch?v=K0bYTvZ0Vs4)

### Mask R-CNN ResNet-50 FPN
[![](https://img.youtube.com/vi/c328VyIgwnQ/0.jpg)](https://www.youtube.com/watch?v=c328VyIgwnQ)
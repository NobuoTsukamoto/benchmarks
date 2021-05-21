# TensorFlow Lite (TensorFlow 1 Detection Model Zoo) Benchmarks

## Environment

- HW
  - Raspberry Pi 4 Model B Rev 1.2 4GB
- OS
  - Raspberry Pi OS 64bit (raspios_arm64-2021-04-09)
    Linux raspberrypi 5.10.36-v8+ #1418 SMP PREEMPT Thu May 13 18:19:53 BST 2021 aarch64 GNU/Linux
- SW
  - TensorFlow Lite 2.5.0
    - FP32 XNNPACK: [PINTO0309/TensorflowLite-bin](https://github.com/PINTO0309/TensorflowLite-bin)
    - INT8: [TensorFlow Lite 2.5.0](https://github.com/tensorflow/tensorflow/releases/tag/v2.5.0)
  - OpenCV 4.5.2 (Self build)
  - Python3 3.7.3

## Dataset
- [COCO2017](https://cocodataset.org/#home)

## How to benchmarks
Source
- [NobuoTsukamoto/tflite-cv-example](https://github.com/NobuoTsukamoto/tflite-cv-example/)

```
$ python benchmark_tflite.py --model _PATH_TO_MODEL_FILE --thread=N(num threads) --count 350
```


Models
- [TensorFlow 1 Detection Model Zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf1_detection_zoo.md)
- [NobuoTsukamoto/export_tfv1_lite_models.ipynb](https://gist.github.com/NobuoTsukamoto/832905aa765f6faa16f53d6dddf61bd2)


## Results
- All results:
    - [Latency mean (ms)](./results/result_raspi4_64bit_latency.txt)

## COCO2017VAL mAP

| Model                      |Input  |Kind   |     AP |   AP50 |   AP75 |   APsmall |   APmedium |   APlarge |   ARmax=1 |   ARmax=10 |   ARmax=100 |   ARsmall |   ARmidium |   ARlarge |
|:---------------------------|:----  |:------|------:|-------:|-------:|----------:|-----------:|----------:|----------:|-----------:|------------:|----------:|-----------:|----------:|
| SSD Mobilenet v2           |300x300|FP32   | 23.36 |  34.5  |  25.99 |      1.53 |      15.55 |     55.97 |     20.95 |      25.98 |       25.98 |      1.93 |      17.68 |     62.2  |
| SSDLite Mobilenet v2       |300x300|FP32   | 23.93 |  36.13 |  26.51 |      1.8  |      16.62 |     55.86 |     21.3  |      26.64 |       26.64 |      2.27 |      18.85 |     62.03 |
| SSD Mobilenet v1 FPN       |640x640|FP32   | 32.2  |  47.21 |  36.31 |     11.9  |      34.77 |     51.02 |     26.68 |      37.21 |       37.21 |     13.22 |      40.06 |     59.17 |
| SSD Resnet 50 v1 FPN       |640x640|FP32   |  0.03 |   0.04 |   0.04 |      0    |       0    |      0.09 |      0.02 |       0.02 |        0.02 |      0    |       0    |      0.08 |
| SSDLite MobileDet-CPU      |320x320|FP32   | 25.66 |  40.33 |  27.36 |      2.46 |      22.07 |     55.27 |     22.89 |      31.46 |       31.46 |      4.08 |      28.42 |     66.19 |
| SSD MnasFPN                |320x320|FP32   | 32.64 |  48.13 |  36.82 |      7.31 |      37.11 |     56.03 |     26.54 |      37.66 |       37.66 |      8.08 |      43.3  |     64.96 |
| SSDLite Mobilenet v3 large |320x320|FP32   | 25.45 |  42.73 |  25.8  |      3.44 |      23.24 |     51.94 |     22.87 |      33.91 |       36.25 |      7.51 |      37.94 |     66.99 |
| SSDLite Mobilenet v3 small |320x320|FP32   | 15.99 |  28.56 |  15.7  |      1.14 |      11.8  |     34.42 |     16.36 |      24.52 |       26.51 |      3.12 |      24.06 |     53.44 |

## Latency mean (ms)

FP32: XNNPACK delegate

|Model name                 |Input  |Kind   |Threads|RasPi4 64bit|
|:--                        |:--    |:--    |--:    |--:         |
|SSD Mobilenet v2           |300x300|FP32   |      1|      498.06|
||||2|327.27|
||||3|320.19|
||||4|318.97|
|SSDLite Mobilenet v2       |300x300|FP32   |      1|      210.46|
||||2|130.44|
||||3|111.67|
||||4|109.60|
|                           |       |INT8   |      1|      168.15|
||||2|93.39|
||||3|69.49|
||||4|57.36|
|SSD Mobilenet v1 FPN       |640x640|FP32   |      1|    15478.10|
||||2|9843.06|
||||3|8119.81|
||||4|8476.19|
|SSD Resnet 50 v1 FPN       |640x640|FP32   |      1|    21784.14|
||||2|13699.05|
||||3|11959.48|
||||4|11593.65|
|SSDLite MobileDet-CPU      |320x320|FP32   |      1|      193.13|
||||2|143.60|
||||3|129.43|
||||4|126.46|
|SSD MnasFPN                |320x320|FP32   |      1|      306.79|
||||2|198.85|
||||3|170.20|
||||4|163.48|
|SSDLite Mobilenet v3 large |320x320|FP32|1|177.60|
||||2|120.72|
||||3|105.89|
||||4|104.32|
|SSDLite Mobilenet v3 small |320x320|FP32   |      1|       70.51|
||||2|51.11|
||||3|44.95|
||||4|43.34|
|SSDLite MobileNetEdgeTPU   |320x320|INT8   |      1|      337.53|
||||2|186.01|
||||3|136.34|
||||4|112.04|
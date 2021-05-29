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

| Model                      |Input  |mAP(FP32) |mAP(INT8) |
|:---------------------------|:----  |---------:|---------:|
| SSD Mobilenet v2           |300x300|    23.36 |          |
| SSDLite Mobilenet v2       |300x300|    23.93 |    22.44 |
| SSD Mobilenet v1 FPN       |640x640|    32.2  |          |
| SSD Resnet 50 v1 FPN       |640x640|     ???? |          |
| SSDLite MobileDet-CPU      |320x320|    25.66 |          |
| SSDLite MobileDet-EdgeTPU  |320x320|          |    26.82 |
| SSD MnasFPN                |320x320|    32.64 |          |
| SSDLite Mobilenet v3 large |320x320|    25.45 |          |
| SSDLite Mobilenet v3 small |320x320|    15.99 |          |
| SSDLite MobileNetEdgeTPU   |320x320|          |    26.96 |

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
|SSDLite MobileDet-EdgeTPU  |320x320|INT8   |      1|      276.50|
||||2|153.73|
||||3|113.04|
||||4| 95.02|
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
# TensorFlow Lite (TensorFlow 1 Detection Model Zoo) Benchmarks

## Environment

- HW
  - Raspberry Pi 4 Model B Rev 1.2 4GB
  - Raspberry Pi 3 Model B+ 2GB
- OS
  - Raspberry Pi OS 64bit (raspios_arm64-2021-04-09)
    Linux raspberrypi 5.10.36-v8+ #1418 SMP PREEMPT Thu May 13 18:19:53 BST 2021 aarch64 GNU/Linux
- SW
  - TensorFlow Lite 2.5.0
    - FP32 XNNPACK: [PINTO0309/TensorflowLite-bin](https://github.com/PINTO0309/TensorflowLite-bin)
    - INT8: [TensorFlow Lite 2.5.0](https://github.com/tensorflow/tensorflow/releases/tag/v2.5.0)
  - OpenCV 4.5.2 (Self build)
  - Python3 3.7.3
  - Edge TPU runtime Frogfish 

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
- [All results](./results)

## COCO2017VAL mAP (RasPi4 64bit)

- FP32: XNNPACK delegate
- EdgeTPU: EdgeTPU delegate, maximum frequency (500 MHz)

| Model                      |Input  |     FP32 |     INT8 |  EdgeTPU |
|:---------------------------|:----  |---------:|---------:|---------:|
| SSD Mobilenet v2           |300x300|    23.36 |          |          |
| SSDLite Mobilenet v2       |300x300|    23.93 |    22.44 |    22.37 |
| SSD Mobilenet v1 FPN       |640x640|    32.2  |          |          |
| SSD Resnet 50 v1 FPN       |640x640|     ???? |          |          |
| SSDLite MobileDet-CPU      |320x320|    25.66 |          |          |
| SSDLite MobileDet-EdgeTPU  |320x320|          |    26.82 |    26.96 |
| SSD MnasFPN                |320x320|    32.64 |          |          |
| SSDLite Mobilenet v3 large |320x320|    25.45 |          |          |
| SSDLite Mobilenet v3 small |320x320|    15.99 |          |          |
| SSDLite MobileNetEdgeTPU   |320x320|          |    26.96 |    26.9  |

## Latency mean (ms)

- FP32: XNNPACK delegate
- EdgeTPU: EdgeTPU delegate, maximum frequency (500 MHz)

|Model name                 |Input  |Kind   |Threads|RasPi3 64bit|RasPi4 64bit|
|:--                        |:--    |:--    |--:    |--:         |--:         |
|SSD Mobilenet v2           |300x300|FP32   |      1|     714.44 |      498.06|
|                           |       |       |      2|     432.01 |      327.27|
|                           |       |       |      3|     367.88 |      320.19|
|                           |       |       |      4|     532.58 |      318.97|
|SSDLite Mobilenet v2       |300x300|FP32   |      1|     349.29 |      210.46|
|                           |       |       |      2|     207.46 |      130.44|
|                           |       |       |      3|     171.00 |      111.67|
|                           |       |       |      4|     198.68 |      109.60|
|                           |       |INT8   |      1|     341.93 |      168.15|
|                           |       |       |      2|     192.29 |       93.39|
|                           |       |       |      3|     144.47 |       69.49|
|                           |       |       |      4|     121.79 |       57.36|
|                           |       |EdgeTPU|      1|      60.62 |       14.75|
|SSD Mobilenet v1 FPN       |640x640|FP32   |      1|   20260.18 |    15478.10|
|                           |       |       |      2|   10665.89 |     9843.06|
|                           |       |       |      3|    8113.69 |     8119.81|
|                           |       |       |      4|    7307.04 |     8476.19|
|SSD Resnet 50 v1 FPN       |640x640|FP32   |      1|   29025.96 |    21784.14|
|                           |       |       |      2|   15448.84 |    13699.05|
|                           |       |       |      3|   12084.88 |    11959.48|
|                           |       |       |      4|   10513.79 |    11593.65|
|SSDLite MobileDet-CPU      |320x320|FP32   |      1|     337.91 |      193.13|
|                           |       |       |      2|     235.68 |      143.60|
|                           |       |       |      3|     211.84 |      129.43|
|                           |       |       |      4|     206.21 |      126.46|
|SSDLite MobileDet-EdgeTPU  |320x320|INT8   |      1|     571.67 |      276.50|
|                           |       |       |      2|     315.45 |      153.73|
|                           |       |       |      3|     218.99 |      113.04|
|                           |       |       |      4|     179.08 |       95.02|
|                           |       |EdgeTPU|      1|      62.99 |       14.75|
|SSD MnasFPN                |320x320|FP32   |      1|     519.17 |      306.79|
|                           |       |       |      2|     337.19 |      198.85|
|                           |       |       |      3|     289.75 |      170.20|
|                           |       |       |      4|     286.28 |      163.48|
|SSDLite Mobilenet v3 large |320x320|FP32   |      1|     366.79 |      177.60|
|                           |       |       |      2|     249.41 |      120.72|
|                           |       |       |      3|     218.46 |      105.89|
|                           |       |       |      4|     214.87 |      104.32|
|SSDLite Mobilenet v3 small |320x320|FP32   |      1|     150.08 |       70.51|
|                           |       |       |      2|     106.19 |       51.11|
|                           |       |       |      3|      94.81 |       44.95|
|                           |       |       |      4|      92.66 |       43.34|
|SSDLite MobileNetEdgeTPU   |320x320|INT8   |      1|     650.97 |      337.53|
|                           |       |       |      2|     352.55 |      186.01|
|                           |       |       |      3|     255.97 |      136.34|
|                           |       |       |      4|     207.27 |      112.04|
|                           |       |EdgeTPU|      1|      74.45 |       14.83|

## ARM NN Delegate Latency mean (ms)
- Delegate Parameter : `{'backends': 'CpuAcc', 'logging-severity': 'info', 'number-of-threads': 'N', 'enable-fast-math': 'true'}`  
  N: Num of Threads
- -: RuntimeError: Tensor numDimensions must be less than or equal to MaxNumOfTensorDimensions at function CheckValidNumDimensions [/home/pi/ArmNNDelegate/armnn/src/armnn/Tensor.cpp:293]
|Model name                 |Input  |Kind   |Threads|RasPi3 64bit|RasPi4 64bit|
|:--                        |:--    |:--    |--:    |--:         |--:         |
|SSD Mobilenet v2           |300x300|FP32   |      1|     594.36 |    |
|                           |       |       |      2|     372.15 |    |
|                           |       |       |      3|     327.36 |    |
|                           |       |       |      4|     309.59 |    |
|SSDLite Mobilenet v2       |300x300|FP32   |      1|     418.45 |    |
|                           |       |       |      2|     256.14 |    |
|                           |       |       |      3|     212.09 |    |
|                           |       |       |      4|     198.27 |    |
|                           |       |INT8   |      1|     328.67 |    |
|                           |       |       |      2|     188.87 |    |
|                           |       |       |      3|     145.87 |    |
|                           |       |       |      4|     124.49 |    |
|SSD Mobilenet v1 FPN       |640x640|FP32   |      1|          - |    |
|                           |       |       |      2|          - |    |
|                           |       |       |      3|          - |    |
|                           |       |       |      4|          - |    |
|SSD Resnet 50 v1 FPN       |640x640|FP32   |      1|            |    |
|                           |       |       |      2|            |    |
|                           |       |       |      3|            |    |
|                           |       |       |      4|            |    |
|SSDLite MobileDet-CPU      |320x320|FP32   |      1|     884.18 |    |
|                           |       |       |      2|     527.78 |    |
|                           |       |       |      3|     436.93 |    |
|                           |       |       |      4|     380.36 |    |
|SSDLite MobileDet-EdgeTPU  |320x320|INT8   |      1|     530.66 |    |
|                           |       |       |      2|     293.96 |    |
|                           |       |       |      3|     245.89 |    |
|                           |       |       |      4|     208.19 |    |
|SSD MnasFPN                |320x320|FP32   |      1|     980.23 |    |
|                           |       |       |      2|     600.04 |    |
|                           |       |       |      3|     492.19 |    |
|                           |       |       |      4|     443.87 |    |
|SSDLite Mobilenet v3 large |320x320|FP32   |      1|     566.57 |    |
|                           |       |       |      2|     369.69 |    |
|                           |       |       |      3|     318.85 |    |
|                           |       |       |      4|     291.93 |    |
|SSDLite Mobilenet v3 small |320x320|FP32   |      1|     321.16 |    |
|                           |       |       |      2|     199.56 |    |
|                           |       |       |      3|     167.38 |    |
|                           |       |       |      4|     150.36 |    |
|SSDLite MobileNetEdgeTPU   |320x320|INT8   |      1|     635.03 |    |
|                           |       |       |      2|     355.39 |    |
|                           |       |       |      3|     267.93 |    |
|                           |       |       |      4|     215.30 |    |

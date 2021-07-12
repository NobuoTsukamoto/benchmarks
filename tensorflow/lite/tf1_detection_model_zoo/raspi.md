# TensorFlow Lite (TensorFlow 1 Detection Model Zoo) Benchmarks

## Environment

- HW
  - RasPi4: Raspberry Pi 4 Model B Rev 1.2 4GB
  - RasPi3 B+: Raspberry Pi 3 Model B+ 2GB
  - RasPi3 V1.2: Raspberry Pi 3 Model B V1.2
  - RasPi2 V1.1: Raspberry Pi 2 Model B V1.1 
- OS
  - Raspberry Pi OS 64bit (raspios_arm64-2021-04-09)
    Linux raspberrypi 5.10.36-v8+ #1418 SMP PREEMPT Thu May 13 18:19:53 BST 2021 aarch64 GNU/Linux
  - Raspberry Pi OS 32bit (2021-05-07-raspios-buster-armhf)
- SW
  - TensorFlow Lite 2.5.0
    - FP32 XNNPACK: [PINTO0309/TensorflowLite-bin](https://github.com/PINTO0309/TensorflowLite-bin)
    - INT8: [TensorFlow Lite 2.5.0](https://github.com/tensorflow/tensorflow/releases/tag/v2.5.0)
  - OpenCV 4.5.2 (Self build)
  - Python3 3.7.3
  - ARM NN Delegate
    - Arm NN v21.05
    - Arm Compute Library v21.05
  - Coral EdgeTPU Delegate
    - libEdgeTPU Release Frogfish
    - Edge TPU Compiler version 15.0.340273435

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

| Model                      |Input  |     FP32 |FP32<br>ARM NN delegate |     INT8 |INT8<br>ARM NN delegate |  EdgeTPU |
|:---------------------------|:----  |---------:|-----------------------:|---------:|-----------------------:|---------:|
| SSD Mobilenet v2           |300x300|    23.36 |                  23.93 |          |                        |          |
| SSDLite Mobilenet v2       |300x300|    23.93 |                  23.36 |    22.44 |                  22.41 |    22.37 |
| SSD Mobilenet v1 FPN       |640x640|    32.2  |                        |          |                        |          |
| SSD Resnet 50 v1 FPN       |640x640|     ???? |                        |          |                        |          |
| SSDLite MobileDet-CPU      |320x320|    25.66 |                  25.66 |          |                        |          |
| SSDLite MobileDet-EdgeTPU  |320x320|          |                        |    26.82 |                  26.84 |    26.96 |
| SSD MnasFPN                |320x320|    32.64 |                  32.64 |          |                        |          |
| SSDLite Mobilenet v3 large |320x320|    25.45 |                  25.45 |          |                        |          |
| SSDLite Mobilenet v3 small |320x320|    15.99 |                  15.99 |          |                        |          |
| SSDLite MobileNetEdgeTPU   |320x320|          |                        |    26.96 |                  26.9  |    26.9  |

## Latency mean (ms)

- FP32: XNNPACK delegate
- EdgeTPU: EdgeTPU delegate, maximum frequency (500 MHz)
- Raspberry Pi 3 Model B V1.2 FP32(XNNPACK delegate) cannot be measured because it hangs during measurement.

|Model name                 |Input  |Kind   |Threads|RasPi2 V1.2 32bit|RasPi3 V1.2 32bit |RasPi3 V1.2 64bit |RasPi3 B+ 32bit  |RasPi3 B+ 64bit  |RasPi4 32bit     |RasPi4 64bit     |
|:--                        |:--    |:--    |--:    |----------------:|-----------------:|-----------------:|----------------:|----------------:|----------------:|----------------:|
|SSD Mobilenet v2           |300x300|FP32   |      1|         3493.16 |           974.94 |                  |          868.52 |          714.44 |          504.20 |           498.06|
|                           |       |       |      2|         1814.76 |           576.12 |                  |          519.31 |          432.01 |          321.72 |           327.27|
|                           |       |       |      3|         1335.17 |           487.71 |                  |          415.30 |          367.88 |          321.78 |           320.19|
|                           |       |       |      4|         1146.69 |           491.05 |                  |          398.19 |          532.58 |          291.66 |           318.97|
|SSDLite Mobilenet v2       |300x300|FP32   |      1|         1499.11 |           488.89 |                  |          423.25 |          349.29 |          225.44 |           210.46|
|                           |       |       |      2|          791.71 |           274.48 |                  |          245.17 |          207.46 |          136.29 |           130.44|
|                           |       |       |      3|          563.94 |           211.11 |                  |          190.98 |          171.00 |          111.38 |           111.67|
|                           |       |       |      4|          450.64 |           184.20 |                  |          169.57 |          198.68 |          105.13 |           109.60|
|                           |       |INT8   |      1|         1269.54 |           595.73 |           395.84 |          509.42 |          341.93 |          248.99 |           168.15|
|                           |       |       |      2|          670.78 |           326.12 |           222.17 |          279.53 |          192.29 |          140.03 |            93.39|
|                           |       |       |      3|          471.40 |           234.67 |           167.18 |          202.76 |          144.47 |          102.24 |            69.49|
|                           |       |       |      4|          375.59 |           188.35 |           140.06 |          164.04 |          121.79 |           82.39 |            57.36|
|                           |       |EdgeTPU|      1|                 |                  |                  |                 |           60.62 |           21.42 |            14.75|
|SSD Mobilenet v1 FPN       |640x640|FP32   |      1|                 |                  |                  |        25085.52 |        20260.18 |        15187.53 |         15478.10|
|                           |       |       |      2|                 |                  |                  |        13503.76 |        10665.89 |        11132.04 |          9843.06|
|                           |       |       |      3|                 |                  |                  |         9831.02 |         8113.69 |         9435.79 |          8119.81|
|                           |       |       |      4|                 |                  |                  |         8424.30 |         7307.04 |         8191.94 |          8476.19|
|SSD Resnet 50 v1 FPN       |640x640|FP32   |      1|                 |                  |                  |        35688.63 |        29025.96 |        21629.62 |         21784.14|
|                           |       |       |      2|                 |                  |                  |        19140.90 |        15448.84 |        14206.31 |         13699.05|
|                           |       |       |      3|                 |                  |                  |        14078.92 |        12084.88 |        12329.81 |         11959.48|
|                           |       |       |      4|                 |                  |                  |        11925.38 |        10513.79 |        11208.88 |         11593.65|
|SSDLite MobileDet-CPU      |320x320|FP32   |      1|         1225.71 |           426.80 |                  |          381.99 |          337.91 |          214.92 |           193.13|
|                           |       |       |      2|          780.94 |           280.39 |                  |          254.03 |          235.68 |          150.08 |           143.60|
|                           |       |       |      3|          615.75 |           239.01 |                  |          222.20 |          211.84 |          130.86 |           129.43|
|                           |       |       |      4|          542.29 |           223.90 |                  |          208.05 |          206.21 |          130.42 |           126.46|
|SSDLite MobileDet-EdgeTPU  |320x320|INT8   |      1|         1831.85 |           843.76 |           665.68 |          727.86 |          571.67 |          351.94 |           276.50|
|                           |       |       |      2|          989.07 |           458.36 |           368.05 |          393.94 |          315.45 |          198.43 |           153.73|
|                           |       |       |      3|          709.18 |           335.32 |           271.96 |          289.61 |          218.99 |          147.33 |           113.04|
|                           |       |       |      4|          567.45 |           270.66 |           224.53 |          235.80 |          179.08 |          119.89 |            95.02|
|                           |       |EdgeTPU|      1|                 |                  |                  |                 |           62.99 |           23.17 |            14.75|
|SSD MnasFPN                |320x320|FP32   |      1|         2085.03 |           715.69 |                  |          626.88 |          519.17 |          350.98 |           306.79|
|                           |       |       |      2|         1196.06 |           437.24 |                  |          390.30 |          337.19 |          228.64 |           198.85|
|                           |       |       |      3|          909.38 |           356.79 |                  |          317.99 |          289.75 |          196.02 |           170.20|
|                           |       |       |      4|          757.33 |           320.44 |                  |          289.49 |          286.28 |          187.31 |           163.48|
|SSDLite Mobilenet v3 large |320x320|FP32   |      1|         1274.11 |           452.54 |                  |          399.75 |          366.79 |          192.55 |           177.60|
|                           |       |       |      2|          724.00 |           286.26 |                  |          258.33 |          249.41 |          125.97 |           120.72|
|                           |       |       |      3|          519.01 |           237.21 |                  |          216.37 |          218.46 |          111.01 |           105.89|
|                           |       |       |      4|          441.57 |           219.75 |                  |          201.45 |          214.87 |          106.83 |           104.32|
|SSDLite Mobilenet v3 small |320x320|FP32   |      1|          463.32 |           180.93 |                  |          159.43 |          150.08 |           79.75 |            70.51|
|                           |       |       |      2|          279.25 |           120.99 |                  |          107.89 |          106.19 |           56.44 |            51.11|
|                           |       |       |      3|          221.65 |           101.84 |                  |           92.62 |           94.81 |           50.70 |            44.95|
|                           |       |       |      4|          193.07 |            85.83 |                  |           88.02 |           92.66 |           48.58 |            43.34|
|SSDLite MobileNetEdgeTPU   |320x320|INT8   |      1|         2225.88 |           993.54 |           761.11 |          850.55 |          650.97 |          418.68 |           337.53|
|                           |       |       |      2|         1187.89 |           532.92 |           409.95 |          459.16 |          352.55 |          230.56 |           186.01|
|                           |       |       |      3|          842.16 |           385.38 |           298.02 |          331.12 |          255.97 |          169.27 |           136.34|
|                           |       |       |      4|          667.30 |           307.42 |           240.86 |          267.08 |          207.27 |          138.37 |           112.04|
|                           |       |EdgeTPU|      1|                 |                  |                  |                 |           74.45 |           21.54 |            14.83|

## ARM NN Delegate Latency mean (ms)
- Delegate Parameter : `{'backends': 'CpuAcc', 'logging-severity': 'info', 'number-of-threads': 'N', 'enable-fast-math': 'true'}`  
  N: Num of Threads
- -: RuntimeError: Tensor numDimensions must be less than or equal to MaxNumOfTensorDimensions at function CheckValidNumDimensions [/home/pi/ArmNNDelegate/armnn/src/armnn/Tensor.cpp:293]
- Raspberry Pi 3 Model B V1.2 cannot be measured because it hangs during measurement.

|Model name                 |Input  |Kind   |Threads|RasPi3 V1.2 64bit|RasPi3 B+ 64bit|RasPi4 64bit|
|:--                        |:--    |:--    |--:    |--:              |--:            |--:         |
|SSD Mobilenet v2           |300x300|FP32   |      1|                 |        594.36 |     335.69 |
|                           |       |       |      2|                 |        372.15 |     218.16 |
|                           |       |       |      3|                 |        327.36 |     184.19 |
|                           |       |       |      4|                 |        309.59 |     175.40 |
|SSDLite Mobilenet v2       |300x300|FP32   |      1|                 |        418.45 |     230.25 |
|                           |       |       |      2|                 |        256.14 |     145.21 |
|                           |       |       |      3|                 |        212.09 |     120.18 |
|                           |       |       |      4|                 |        198.27 |     111.85 |
|                           |       |INT8   |      1|                 |        328.67 |     199.09 |
|                           |       |       |      2|                 |        188.87 |     115.64 |
|                           |       |       |      3|                 |        145.87 |      82.53 |
|                           |       |       |      4|                 |        124.49 |      69.45 |
|SSD Mobilenet v1 FPN       |640x640|FP32   |      1|                 |             - |          - |
|                           |       |       |      2|                 |             - |          - |
|                           |       |       |      3|                 |             - |          - |
|                           |       |       |      4|                 |             - |          - |
|SSD Resnet 50 v1 FPN       |640x640|FP32   |      1|                 |               |            |
|                           |       |       |      2|                 |               |            |
|                           |       |       |      3|                 |               |            |
|                           |       |       |      4|                 |               |            |
|SSDLite MobileDet-CPU      |320x320|FP32   |      1|                 |        884.18 |     416.97 |
|                           |       |       |      2|                 |        527.78 |     277.66 |
|                           |       |       |      3|                 |        436.93 |     237.00 |
|                           |       |       |      4|                 |        380.36 |     209.88 |
|SSDLite MobileDet-EdgeTPU  |320x320|INT8   |      1|                 |        530.66 |     327.92 |
|                           |       |       |      2|                 |        293.96 |     180.72 |
|                           |       |       |      3|                 |        245.89 |     130.23 |
|                           |       |       |      4|                 |        208.19 |     105.97 |
|SSD MnasFPN                |320x320|FP32   |      1|                 |        980.23 |     505.48 |
|                           |       |       |      2|                 |        600.04 |     320.27 |
|                           |       |       |      3|                 |        492.19 |     267.38 |
|                           |       |       |      4|                 |        443.87 |     252.25 |
|SSDLite Mobilenet v3 large |320x320|FP32   |      1|                 |        566.57 |     252.39 |
|                           |       |       |      2|                 |        369.69 |     174.67 |
|                           |       |       |      3|                 |        318.85 |     150.27 |
|                           |       |       |      4|                 |        291.93 |     135.99 |
|SSDLite Mobilenet v3 small |320x320|FP32   |      1|                 |        321.16 |     145.02 |
|                           |       |       |      2|                 |        199.56 |     100.34 |
|                           |       |       |      3|                 |        167.38 |      85.69 |
|                           |       |       |      4|                 |        150.36 |      78.51 |
|SSDLite MobileNetEdgeTPU   |320x320|INT8   |      1|                 |        635.03 |     378.45 |
|                           |       |       |      2|                 |        355.39 |     205.51 |
|                           |       |       |      3|                 |        267.93 |     148.41 |
|                           |       |       |      4|                 |        215.30 |     119.06 |

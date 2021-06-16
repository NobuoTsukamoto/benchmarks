# EfficientDet TensorFlow Lite Benchmarks

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
# AP
$ Python object_detection_benchmark_tflite.py --model PATH_TO_MODEL_FILE --images_dir /PATH_TO_COCO2017VAL --annotation_path PATH_TO_instances_val2017.json --threads 4

# Latancy
$ python benchmark_tflite.py --model _PATH_TO_MODEL_FILE --thread=N(num threads) --count 350
```

Models
- [Pretrained EfficientDet Checkpoints - google/automl](https://github.com/google/automl/tree/42ad3a40d237cb11b0894be69ba5855f41ae645f/efficientdet#2-pretrained-efficientdet-checkpoints)
- [NobuoTsukamoto/export-efficientdet-lite-tf-lite-model.ipynb](https://gist.github.com/NobuoTsukamoto/c47ed552c412db4dbfac97a8568f17f0)

## Results
- [All results](./results)

## COCO2017VAL mAP
- -: Segmantation fault
- *: Edge TPU Compiler Internal compiler error. Aborting!
- **: Transfer on tag 1 failed. Abort. Deadline exceeded: USB transfer error 2 [LibUsbDataOutCallback].   
  See details (https://github.com/google-coral/edgetpu/issues/11).

| Model               |Input  | FP32<br>XNNPACK delegate | FP32<br>ARM NN delegate | INT8       | EdgeTPU    |
|:--------------------|:----  |-------------------------:|------------------------:|-----------:|-----------:|
| EfficientDet-lite0  |320x320|                    26.03 |                   26.03 |      25.65 |      25.54 |
| EfficientDet-lite1  |384x384|                    30.16 |                   30.16 |      29.61 |      29.7  |
| EfficientDet-lite2  |448x448|                    33.16 |                   33.16 |      32.72 |      28.5  |
| EfficientDet-lite3  |512x512|                    36.32 |                   36.32 |      36    |          * |
| EfficientDet-lite3x |640x640|      　　　　　　　38.68 |                   38.68 |      38.24 |         ** |
| EfficientDet-lite4  |640x640|      　　　　　　　39.7  |                       - |      39.38 |          * |


## Latency mean (ms)
- FP32: XNNPACK delegate
- *: Transfer on tag 1 failed. Abort. Deadline exceeded: USB transfer error 2 [LibUsbDataOutCallback].   
  See details (https://github.com/google-coral/edgetpu/issues/11).
- **: bad_alloc error.

| Model               |Input  |Kind        |Threads   |RasPi3 64bit|RasPi4 64bit|
|:--------------------|:----  |:-----------|---------:|-----------:|-----------:|
| EfficientDet-lite0  |320x320|FP32        |        1 |     720.83 |     354.84 |
|                     |       |            |        2 |     483.75 |     232.89 |
|                     |       |            |        3 |     414.90 |     201.95 |
|                     |       |            |        4 |     342.94 |     193.39 |
|                     |       |INT8        |        1 |     624.07 |     344.03 |
|                     |       |            |        2 |     388.97 |     232.77 |
|                     |       |            |        3 |     317.03 |     143.85 |
|                     |       |            |        4 |     277.76 |     122.06 |
|                     |       |EdgeTPU     |        1 |     468.48 |      99.77 |
| EfficientDet-lite1  |384x384|FP32        |        1 |    1191.83 |     691.68 |
|                     |       |            |        2 |     780.83 |     424.00 |
|                     |       |            |        3 |     650.56 |     362.36 |
|                     |       |            |        4 |     652.47 |     348.76 |
|                     |       |INT8        |        1 |    1131.02 |     546.90 |
|                     |       |            |        2 |     675.48 |     324.85 |
|                     |       |            |        3 |     532.03 |     251.86 |
|                     |       |            |        4 |     458.83 |     211.73 |
|                     |       |EdgeTPU     |        1 |     693.04 |     141.15 |
| EfficientDet-lite2  |448x448|FP32        |        1 |    2145.50 |    1098.97 |
|                     |       |            |        2 |    1272.05 |     690.23 |
|                     |       |            |        3 |    1046.23 |     589.15 |
|                     |       |            |        4 |     963.23 |     565.30 |
|                     |       |INT8        |        1 |    1785.89 |     857.87 |
|                     |       |            |        2 |    1057.31 |     505.17 |
|                     |       |            |        3 |     836.27 |     394.94 |
|                     |       |            |        4 |     711.60 |     331.20 |
|                     |       |EdgeTPU     |        1 |    1138.33 |     219.76 |
| EfficientDet-lite3  |512x512|FP32        |        1 |    7206.10 |    2308.64 |
|                     |       |            |        2 |    4272.14 |    1370.47 |
|                     |       |            |        3 |    3471.59 |    1167.75 |
|                     |       |            |        4 |    3149.46 |    1139.21 |
|                     |       |INT8        |        1 |    3414.30 |    1657.71 |
|                     |       |            |        2 |    1965.97 |     948.42 |
|                     |       |            |        3 |    1495.18 |     716.57 |
|                     |       |            |        4 |    1260.19 |     601.34 |
| EfficientDet-lite3x |640x640|FP32        |        1 |    4094.17 |    4089.07 |
|                     |       |            |        2 |    2497.62 |    2472.28 |
|                     |       |            |        3 |    2009.69 |    2067.91 |
|                     |       |            |        4 |    1814.83 |    2015.04 |
|                     |       |INT8        |        1 |    2130.3  |    2979.10 |
|                     |       |            |        2 |    3463.11 |    1685.61 |
|                     |       |            |        3 |    2622.84 |    1267.22 |
|                     |       |            |        4 |    2191.00 |    1050.79 |
|                     |       |EdgeTPU     |        1 |          * |          * |
| EfficientDet-lite4  |640x640|FP32        |        1 |         ** |    5743.08 |
|                     |       |            |        2 |         ** |    3399.70 |
|                     |       |            |        3 |         ** |    2835.45 |
|                     |       |            |        4 |         ** |    2847.02 |
|                     |       |INT8        |        1 |    8242.53 |    4008.46 |
|                     |       |            |        2 |    4601.04 |    2244.46 |
|                     |       |            |        3 |    3463.92 |    1659.16 |
|                     |       |            |        4 |    2841.39 |    1360.11 |

## ARM NN Delegate Latency mean (ms)
- Delegate Parameter : `{'backends': 'CpuAcc', 'logging-severity': 'info', 'number-of-threads': 'N', 'enable-fast-math': 'true'}`  
  N: Num of Threads
- -: Segmantation fault

| Model               |Input  |Kind        |Threads   |RasPi4 64bit|
|:--------------------|:----  |:-----------|---------:|-----------:|
| EfficientDet-lite0  |320x320|FP32        |        1 |     520.00 |
|                     |       |            |        2 |     320.08 |
|                     |       |            |        3 |     258.25 |
|                     |       |            |        4 |     229.91 |
|                     |       |INT8        |        1 |    1187.71 |
|                     |       |            |        2 |     636.04 |
|                     |       |            |        3 |     464.67 |
|                     |       |            |        4 |     363.14 |
| EfficientDet-lite1  |384x384|FP32        |        1 |     917.73 |
|                     |       |            |        2 |     568.35 |
|                     |       |            |        3 |     454.73 |
|                     |       |            |        4 |     413.50 |
|                     |       |INT8        |        1 |    2300.32 |
|                     |       |            |        2 |    1215.24 |
|                     |       |            |        3 |     849.08 |
|                     |       |            |        4 |     676.47 |
| EfficientDet-lite2  |448x448|FP32        |        1 |    1419.79 |
|                     |       |            |        2 |     884.95 |
|                     |       |            |        3 |     706.44 |
|                     |       |            |        4 |     624.21 |
|                     |       |INT8        |        1 |    3524.52 |
|                     |       |            |        2 |    1850.40 |
|                     |       |            |        3 |    1315.06 |
|                     |       |            |        4 |    1016.84 |
| EfficientDet-lite3  |512x512|FP32        |        1 |    2772.21 |
|                     |       |            |        2 |    1665.98 |
|                     |       |            |        3 |    1348.81 |
|                     |       |            |        4 |    1190.78 |
|                     |       |INT8        |        1 |    6244.21 |
|                     |       |            |        2 |    3241.10 |
|                     |       |            |        3 |    2297.68 |
|                     |       |            |        4 |    1751.42 |
| EfficientDet-lite3x |640x640|FP32        |        1 |    4699.25 |
|                     |       |            |        2 |    2843.76 |
|                     |       |            |        3 |    2238.66 |
|                     |       |            |        4 |    2018.51 |
|                     |       |INT8        |        1 |   10737.77 |
|                     |       |            |        2 |    5561.44 |
|                     |       |            |        3 |    3907.89 |
|                     |       |            |        4 |    3001.89 |
| EfficientDet-lite4  |640x640|FP32        |        1 |          - |
|                     |       |            |        2 |          - |
|                     |       |            |        3 |          - |
|                     |       |            |        4 |          - |
|                     |       |INT8        |        1 |   14074.93 |
|                     |       |            |        2 |    7238.01 |
|                     |       |            |        3 |    5070.61 |
|                     |       |            |        4 |    3883.23 |

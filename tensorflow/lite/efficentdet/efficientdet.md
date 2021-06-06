# EfficientDet TensorFlow Lite Benchmarks

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
FP32: XNNPACK delegate  

| Model               |Input  | FP32       | INT8       |
|:--------------------|:----  |-----------:|-----------:|
| EfficientDet-lite0  |320x320|      26.03 |      25.65 |
| EfficientDet-lite1  |384x384|      30.16 |      29.61 |
| EfficientDet-lite2  |448x448|      33.16 |      32.72 |
| EfficientDet-lite3  |512x512|      33.16 |      36    |
| EfficientDet-lite3x |640x640|      36.32 |      38.24 |
| EfficientDet-lite4  |640x640|      39.7  |      39.38 |


## Latency mean (ms)
FP32: XNNPACK delegate

| Model               |Input  |Kind        |Threads   |RasPi4 64bit|
|:--------------------|:----  |:-----------|---------:|-----------:|
| EfficientDet-lite0  |320x320|FP32        |        1 |     354.84 |
|                     |       |            |        2 |     232.89 |
|                     |       |            |        3 |     201.95 |
|                     |       |            |        4 |     193.39 |
|                     |       |INT8        |        1 |     344.03 |
|                     |       |            |        2 |     232.77 |
|                     |       |            |        3 |     143.85 |
|                     |       |            |        4 |     122.06 |
| EfficientDet-lite1  |384x384|FP32        |        1 |     691.68 |
|                     |       |            |        2 |     424.00 |
|                     |       |            |        3 |     362.36 |
|                     |       |            |        4 |     348.76 |
|                     |       |INT8        |        1 |     546.90 |
|                     |       |            |        2 |     324.85 |
|                     |       |            |        3 |     251.86 |
|                     |       |            |        4 |     211.73 |
| EfficientDet-lite2  |448x448|FP32        |        1 |    1098.97 |
|                     |       |            |        2 |     690.23 |
|                     |       |            |        3 |     589.15 |
|                     |       |            |        4 |     565.30 |
|                     |       |INT8        |        1 |     857.87 |
|                     |       |            |        2 |     505.17 |
|                     |       |            |        3 |     394.94 |
|                     |       |            |        4 |     331.20 |
| EfficientDet-lite3  |512x512|FP32        |        1 |    2308.64 |
|                     |       |            |        2 |    1370.47 |
|                     |       |            |        3 |    1167.75 |
|                     |       |            |        4 |    1139.21 |
|                     |       |INT8        |        1 |    1657.71 |
|                     |       |            |        2 |     948.42 |
|                     |       |            |        3 |     716.57 |
|                     |       |            |        4 |     601.34 |
| EfficientDet-lite3x |640x640|FP32        |        1 |    4089.07 |
|                     |       |            |        2 |    2472.28 |
|                     |       |            |        3 |    2067.91 |
|                     |       |            |        4 |    2015.04 |
|                     |       |INT8        |        1 |    2979.10 |
|                     |       |            |        2 |    1685.61 |
|                     |       |            |        3 |    1267.22 |
|                     |       |            |        4 |    1050.79 |
| EfficientDet-lite4  |640x640|FP32        |        1 |    5743.08 |
|                     |       |            |        2 |    3399.70 |
|                     |       |            |        3 |    2835.45 |
|                     |       |            |        4 |    2847.02 |
|                     |       |INT8        |        1 |    4008.46 |
|                     |       |            |        2 |    2244.46 |
|                     |       |            |        3 |    1659.16 |
|                     |       |            |        4 |    1360.11 |

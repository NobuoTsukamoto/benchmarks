# TensorFlow Lite (TensorFlow 1 Detection Model Zoo) Benchmarks

## Environment

- HW
  - Dev Board 1GB
- OS
  - Mendel Linux  
    Linux orange-calf 4.14.98-imx #1 SMP PREEMPT Fri May 14 22:12:02 UTC 2021 aarch64 GNU/Linux
- SW
  - TensorFlow Lite 2.5.0
  - Python 3.7.3
  - Coral EdgeTPU Delegate
    - libEdgeTPU Release Grouper
    - Edge TPU Compiler version 16.0.384591198

## How to benchmarks
Source
- [NobuoTsukamoto/tflite-cv-example](https://github.com/NobuoTsukamoto/tflite-cv-example/)

```
$ python benchmark_tflite.py --model _PATH_TO_MODEL_FILE
```

Models
- [TensorFlow 1 Detection Model Zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf1_detection_zoo.md)
- [NobuoTsukamoto/export_tfv1_lite_models.ipynb](https://gist.github.com/NobuoTsukamoto/832905aa765f6faa16f53d6dddf61bd2)

## Results
- [All results](./results)

## Latency mean (ms)

- EdgeTPU: EdgeTPU delegate, maximum frequency (500 MHz)

### Dev Bard (Edge TPU delegate)
|Model name                 |Input  |Kind   |Dev Board |
|:--------------------------|:------|:----- |:---------|
|SSDLite Mobilenet v1       |300x300|EdgeTPU|    14.78 |
|SSDLite Mobilenet v2       |300x300|EdgeTPU|    17.49 |
|SSDLite MobileNetEdgeTPU   |320x320|EdgeTPU|    19.38 |
|SSDLite MobileDet-EdgeTPU  |300x300|EdgeTPU|    19.31 |
|SpaghettiNet for EdgeTpu S |300x300|EdgeTPU|    16.64 |
|SpaghettiNet for EdgeTpu M |300x300|EdgeTPU|    16.83 |
|SpaghettiNet for EdgeTpu L |300x300|EdgeTPU|    17.71 |


### Dev Bard (SpaghettiNet for Edge TPU delegate)

|Model name                 |Input  |no Post-processing|with Post-processing<br>max_detection=10|with Post-processing<br>max_detection=25|with Post-processing<br>max_detection=50|with Post-processing<br>max_detection=100|
|:--------------------------|:------|:-----|:------|:------|:------|:------|
|SpaghettiNet for EdgeTpu S |300x300| 10.98| 16.64 | 22.34 | 26.87 | 33.47 |
|SpaghettiNet for EdgeTpu M |300x300| 12.15| 16.83 | 22.39 | 28.39 | 35.00 |
|SpaghettiNet for EdgeTpu L |300x300| 12.50| 17.71 | 23.58 | 28.58 | 35.95 |
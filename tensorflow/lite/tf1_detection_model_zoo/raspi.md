# TensorFlow Lite (TensorFlow 2 Detection Model Zoo) Benchmarks

## Environment
    
- HW
  - Raspberry Pi 4 Model B Rev 1.2 4GB
- OS
  - Raspberry Pi OS 64bit (raspios_arm64-2021-04-09)  
    Linux raspberrypi 5.10.36-v8+ #1418 SMP PREEMPT Thu May 13 18:19:53 BST 2021 aarch64 GNU/Linux
- SW
  - TensorFlow Lite 2.5.0
    - FP32 XNNPACK: [PINTO0309/TensorflowLite-bin](https://github.com/PINTO0309/TensorflowLite-bin)
    - INT8 EdgeTPU: [TensorFlow 2.5.0](https://github.com/tensorflow/tensorflow/releases/tag/v2.5.0)
  - OpenCV 4.5.2 (Self build)
  - Python3 3.7.3

## Dataset
- [COCO2017](https://cocodataset.org/#home) 

## How to benchmarks
Source
- [NobuoTsukamoto/tflite-cv-example](https://github.com/NobuoTsukamoto/tflite-cv-example/)
Models
- [NobuoTsukamoto/export_tfv1_lite_models.ipynb](https://gist.github.com/NobuoTsukamoto/832905aa765f6faa16f53d6dddf61bd2)

```
$ python benchmark_tflite.py --model _PATH_TO_MODEL_FILE --thread=N(num threads) --count 350
```

## Results
- All results:
    - [Latency mean (ms)](./results/result_raspi4_64bit_latency.txt)

## mAP

## Latency mean (ms)

### FP32 Model

Note: The latency is the number of threads (1, 2, 3, 4) from the top.

|Model name                                                 |RasPi4 64bit|
|:--                                                        |--:|
|ssd_mobilenet_v2_300x300_coco                              |498.06<br>327.27<br>320.19<br>318.97|
|ssdlite_mobilenet_v2_coco                                  |210.46<br>130.44<br>111.67<br>109.60|
|ssd_mobilenet_v1_fpn_shared_box_predictor_640x640_coco     |15478.10<br>9843.06<br>8119.81<br>8476.19|
|ssd_resnet50_v1_fpn_shared_box_predictor_640x640_coco      |21784.14<br>13699.05<br>11959.48<br>11593.65|
|ssdlite_mobiledet_cpu_320x320_coco                         |193.13<br>143.60<br>129.43<br>126.46|
|ssd_mobilenet_v2_mnasfpn_shared_box_predictor_320x320_coco |306.79<br>198.85<br>170.20<br>163.48|
|ssd_mobilenet_v3_large_320x320_coco                        |177.60<br>120.72<br>105.89<br>104.32|
|ssd_mobilenet_v3_small_320x320_coco                        |70.51<br>51.11<br>44.95<br>43.34|

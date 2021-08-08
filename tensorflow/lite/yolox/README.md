# YOLOX TensorFlow Lite Benchmarks

## Environment

- HW
  - RasPi4: Raspberry Pi 4 Model B Rev 1.2 4GB
- OS
  - Raspberry Pi OS 64bit (raspios_arm64-2021-04-09)
    Linux raspberrypi 5.10.36-v8+ #1418 SMP PREEMPT Thu May 13 18:19:53 BST 2021 aarch64 GNU/Linux
  - Raspberry Pi OS 32bit (2021-05-07-raspios-buster-armhf)
- SW
  - TensorFlow Lite 2.5.0
    - FP32 XNNPACK: [PINTO0309/TensorflowLite-bin](https://github.com/PINTO0309/TensorflowLite-bin)
  - OpenCV 4.5.2 (Self build)
  - Python3 3.7.3

## Dataset
- [COCO2017](https://cocodataset.org/#home)

## How to benchmarks
Source
- [NobuoTsukamoto/tflite-cv-example](https://github.com/NobuoTsukamoto/tflite-cv-example/)

```
python benchmark_tflite.py --model _PATH_TO_MODEL_FILE_ --thread=N(num threads) --count 350

python yolox_tflite_coco_metrics.py --model _PATH_TO_MODEL_FILE_ --thread=4 --images_dir _COCO_VAL_IMAGES_DIR_ --annotation_path instances_val2017.json --exec_coco_metrics 
```


Models
- [Megvii-BaseDetection/YOLOX](https://github.com/Megvii-BaseDetection/YOLOX)
- [YOLOX TensorFlow Lite Model - PINTO_model_zoo](https://github.com/PINTO0309/PINTO_model_zoo)


## Results
- [All results](./results)

## COCO2017VAL mAP (RasPi4 64bit)

- FP32: XNNPACK delegate

| Model         |Input  | FP32  |
|:--------------|:------|------:|
| YOLOX-Nano    |416x416| 25.11 |
| YOLOX-Tiny    |416x416| 31.45 |

## Latency mean (ms)

- FP32: XNNPACK delegate

|Model name     |Input  |Kind   |Threads|RasPi4 64bit     |
|:--            |:--    |:--    |--:    |----------------:|
| YOLOX-Nano    |416x416|  FP32 |      1|          227.39 |
|               |       |       |      2|          146.85 |
|               |       |       |      3|          127.04 |
|               |       |       |      4|          117.85 |
| YOLOX-Tiny    |416x416|  FP32 |      1|          817.90 |
|               |       |       |      2|          468.40 |
|               |       |       |      3|          373.06 |
|               |       |       |      4|          367.50 |

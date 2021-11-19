# EfficientDet Jetson Nano TensorRT Benchmarks

## Environment

- HW
  - Jetson Nano
- OS
  - JetPack 4.6
    Linux raspberrypi 5.10.36-v8+ #1418 SMP PREEMPT Thu May 13 18:19:53 BST 2021 aarch64 GNU/Linux
- SW
  - TensorRT 8

## Dataset
- [COCO2017](https://cocodataset.org/#home)

## How to benchmarks
Export ONNX model.
- [TensorRT EfficientDet-Lite Model Conversion AutoML Models to ONNX Model](https://github.com/NobuoTsukamoto/tensorrt-examples/blob/main/cpp/efficientdet/Export_EfficientDetLite_TensorRT.ipynb)

```
# Latancy
$ usr/src/tensorrt/bin/trtexec --onnx=_PATH_TO_/efficientdet-liteX.onnx --workspace=200 --fp16
```

Models
- [Pretrained EfficientDet Checkpoints - google/automl](https://github.com/google/automl/tree/42ad3a40d237cb11b0894be69ba5855f41ae645f/efficientdet#2-pretrained-efficientdet-checkpoints)

## Results
- [All results](./results)

## Latency mean (ms)
| Model               |Input  |Jetson Nano FP16 |
|:--------------------|:----  |----------------:|
| EfficientDet-lite0  |320x320|           40.07 |
| EfficientDet-lite1  |384x384|           73.95 |
| EfficientDet-lite2  |448x448|          106.63 |
| EfficientDet-lite3  |512x512|          186.78 |
| EfficientDet-lite3x |640x640|          319.39 |
| EfficientDet-lite4  |640x640|          406.49 |

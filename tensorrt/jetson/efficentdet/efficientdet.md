# EfficientDet Jetson Nano TensorRT Benchmarks

## Environment

- HW
  - Jetson Nano
- OS
  - JetPack 4.6
    Linux raspberrypi 5.10.36-v8+ #1418 SMP PREEMPT Thu May 13 18:19:53 BST 2021 aarch64 GNU/Linux
- SW
  - TensorRT 8

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

### Jetson Nano
| Model               |Input  |    FP16 |    FP32 |
|:--------------------|:----  |--------:|--------:|
| EfficientDet-lite0  |320x320|   40.07 |   45.88 |
| EfficientDet-lite1  |384x384|   73.95 |   82.80 |
| EfficientDet-lite2  |448x448|  106.63 |  122.33 |
| EfficientDet-lite3  |512x512|  186.78 |  215.88 |
| EfficientDet-lite3x |640x640|  319.39 |  386.62 |
| EfficientDet-lite4  |640x640|  406.49 |  509.14 |

## Youtube video

Code
- https://github.com/NobuoTsukamoto/tensorrt-examples/tree/main/cpp/efficientdet

```
./trt_efficientdet \
  _PATH_TO_TRT_MODEL_FILE \
  --width=MODEL_INPUT_WIDTH \
  --height=MODEL_INPUT_HEIGHT \
  --file=_PATH_TO_INPUT_VIDEO_FILE \
  --score=0.4 \
  --label=_PATH_TO_/tensorrt-examples/models/coco_labels.txt \
  --output=_PATH_TO_OUTPUT_VIDEO_FILE
```

### EfficientDet-lite0 FP16
[![](https://img.youtube.com/vi/eR-xN1lGE2s/0.jpg)](https://www.youtube.com/watch?v=eR-xN1lGE2s)

### EfficientDet-lite1 FP16
[![](https://img.youtube.com/vi/tYTWntlrW-0/0.jpg)](https://www.youtube.com/watch?v=tYTWntlrW-0)
    
### EfficientDet-lite2 FP16
[![](https://img.youtube.com/vi/cXaTTipd4pM/0.jpg)](https://www.youtube.com/watch?v=cXaTTipd4pM)

### EfficientDet-lite3 FP16
[![](https://img.youtube.com/vi/9yB_diWI1Hk/0.jpg)](https://www.youtube.com/watch?v=9yB_diWI1Hk)

### EfficientDet-lite3x FP16
[![](https://img.youtube.com/vi/GcdrwMMF4O4/0.jpg)](https://www.youtube.com/watch?v=GcdrwMMF4O4)

### EfficientDet-lite4 FP16
[![](https://img.youtube.com/vi/A0bdgxcqr-c/0.jpg)](https://www.youtube.com/watch?v=A0bdgxcqr-c)
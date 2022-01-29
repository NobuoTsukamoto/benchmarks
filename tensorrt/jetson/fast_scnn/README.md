
# Jetson Nano TensorRT Fast-SCNN benchmarks

## Environment

- HW
  - Jetson Nano
- OS
  - JetPack 4.6
    Linux raspberrypi 5.10.36-v8+ #1418 SMP PREEMPT Thu May 13 18:19:53 BST 2021 aarch64 GNU/Linux
- SW
  - TensorRT 8

## How to benchmarks
Models (ONNX)
- [Tramac/Fast-SCNN-pytorch](https://github.com/Tramac/Fast-SCNN-pytorch)
- [PINTO_model_zoo/228_Fast-SCNN](https://github.com/PINTO0309/PINTO_model_zoo/tree/main/228_Fast-SCNN)

```
# Latancy
$ usr/src/tensorrt/bin/trtexec --onnx=_PATH_TO_/*.onnx [--fp16]
```


## Results

## End-to-End Host Latency mean (ms)

| Model (Input) | FP16    | FP32   |
|:--------------|--------:|-------:|
| 384x384       |  18.05  |  18.46 |
| 384x576       |  25.21  |  25.33 |
| 576x576       |  36.96  |  37.27 |
| 576x768       |  49.09  |  49.02 |
| 768x1344      |  111.74 | 111.89 |

## Youtube video

### 384x384 FP16
[![](https://img.youtube.com/vi/1qjGCSC2XYo/0.jpg)](https://youtu.be/1qjGCSC2XYo)

### 384x576 FP16
[![](https://img.youtube.com/vi/QtQDUJ0hJ5o/0.jpg)](https://youtu.be/QtQDUJ0hJ5o)

### 576x576 FP16
[![](https://img.youtube.com/vi/Qy4S4_5JCAM/0.jpg)](https://youtu.be/Qy4S4_5JCAM)

### 576x768 FP16
[![](https://img.youtube.com/vi/bzFMwWJak-8/0.jpg)](https://youtu.be/bzFMwWJak-8)

### 768x1344 FP16
[![](https://img.youtube.com/vi/Lg6BvEgN9AA/0.jpg)](https://youtu.be/Lg6BvEgN9AA)

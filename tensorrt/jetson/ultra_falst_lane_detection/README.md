
# Jetson Nano TensorRT Ultra-Fast-Lane-Detection benchmarks

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
- [cfzd/Ultra-Fast-Lane-Detection](https://github.com/cfzd/Ultra-Fast-Lane-Detection)
- [PINTO_model_zoo/140_Ultra-Fast-Lane-Detection](https://github.com/PINTO0309/PINTO_model_zoo/tree/main/140_Ultra-Fast-Lane-Detection)

```
# Latancy
$ usr/src/tensorrt/bin/trtexec --onnx=_PATH_TO_/*.onnx [--fp16]
```


## Results

## End-to-End Host Latency mean (ms)

| Model                                     | FP16  | FP32  |
|:------------------------------------------|------:|------:|
| ultra_falst_lane_detection_culane_288x800 | 50.36 | 89.59 |

## Youtube video

### FP16
[![](https://img.youtube.com/vi/gsqi37XZF9M/0.jpg)](https://youtu.be/gsqi37XZF9M)

### FP32
[![](https://img.youtube.com/vi/mG2IRRSXVxA/0.jpg)](https://youtu.be/mG2IRRSXVxA)

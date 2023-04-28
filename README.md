# Benchmarks

## About
Benchmarks such as TensorFlow, TensorFlow-Lite, PyTorch, Torchvision, etc...

## Summary

### HostPC / Google Colaboratory
|Description|Benchmarks|Framework|HW|
|:--|:--|:--|:--|
|[TF2 Detection Models](tensorflow/tf2_detection_model_zoo/local_gtx1070.md)|AP, Latency|TensorFlow<br>XLA Auto-clustering|Local PC GTX1070|
|[TF2 Detection Models](tensorflow/tf2_detection_model_zoo/colab_p100.md)|AP, Latency|TensorFlow<br>TF-TRT<br>XLA Auto-clustering|Google Colab Tesla P100|
|[TF2 Detection Models](tensorflow/tf2_detection_model_zoo/colab_v100.md)|AP, Latency|TensorFlow|Google Colab Tesla V100|
|[TF2 Detection Models](tensorflow/tf2_detection_model_zoo/v100_vs_p100_vs_gtx1070.md)|Latency|TensorFlow|V100 vs P100 vs GTX1070|
|[Torchvision detection models](pytorch/torchvision/README.md)|AP, Latency, <br>YouTube video|PyTorch, Torchvision|Local PC GTX1070|

### Raspberry Pi / Coral Dev Board + EdgeTPU
|Description|Benchmarks|Framework|HW|
|:--|:--|:--|:--|
|[TensorFlow 1 Detection Model Zoo](tensorflow/lite/tf1_detection_model_zoo/raspi.md)|AP, Latency|TensorFlow Lite<br>XNNPACK delegate<br>ARM NN delegate<br>EdgeTPU delegate|Raspberry Pi 2, 3, 4<br>Coral USB Accelerator|
|[EdgeTPU Models](tensorflow/lite/tf1_detection_model_zoo/devboard.md)|Latency|TensorFlow Lite<br>EdgeTPU delegate|Coral Dev Board|
|[EfficientDet-Lite](tensorflow/lite/efficentdet/efficientdet.md)|AP, Latency|TensorFlow Lit<br>XNNPACK delegate<br>ARM NN delegate<br>EdgeTPU delegate|Raspberry Pi 2, 3, 4<br>Coral USB Accelerator|
|[YOLOX TensorFlow LiteM](tensorflow/lite/yolox)|AP, Latency|TensorFlow Lite<br>XNNPACK delegate|Raspberry Pi 4|
|[TF-Lite SpaghettiNet EdgeTpu Latency vs max_detections](tensorflow/lite/spaghettinet/latency_vs_map.md)|AP, Latency|TensorFlow Lite EdgeTPU delegate|Raspberry Pi 4 + Coral USB Accelerator<br>Coral Dev Board|

### Jetson
|Description|Benchmarks|Framework|HW|
|:--|:--|:--|:--|
|[TensorRT EfficientDet and TensorFlow Object Detection API](tensorrt/jetson/detection/README.md)| Latency,<br>YouTube video | TensorRT | Jetson Nano |
|[TensorRT Autoseg-EdgeTPU and<br>DeepLab v3+ MobilenetEdgeTPUV2](tensorrt/jetson/deeplabv3_edgetpuv2/deeplabv3_edgetpuv2.md)| Latency,<br>YouTube video | TensorRT | Jetson Nano |
|[TensorRT Fast-SCNN](tensorrt/jetson/fast_scnn/README.md)| Latency,<br>YouTube video | TensorRT | Jetson Nano |
|[TensorRT Ultra-Fast-Lane-Detection](tensorrt/jetson/ultra_falst_lane_detection/README.md)| Latency,<br>YouTube video | TensorRT | Jetson Nano |

### TensorFlow Lite on RISC-V SoC
|Description|Benchmarks|Framework|HW|
|:--|:--|:--|:--|
|[Sipeed Lichee RV Dock Allwinner D1](tensorflow/lite/riscv/lichee_rv_dock/README.md) | Latency | TensorFlow Lite | CPU |
|[StarFive VisionFive 2](tensorflow/lite/riscv/visionfive2/README.md) | Latency | TensorFlow Lite | CPU, GPU |

## Reference
- [TensorFlow 1 Detection Model Zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf1_detection_zoo.md)
- [TensorFlow 2 Detection Model Zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md)
- [TensorFlow XLA Auto-clustering](https://www.tensorflow.org/xla#auto-clustering)
- [TF-TRT (tensorflow / tensorrt)](https://github.com/tensorflow/tensorrt)
- FP32 XNNPACK: [PINTO0309/TensorflowLite-bin](https://github.com/PINTO0309/TensorflowLite-bin)
- [EfficientDet](https://github.com/google/automl/tree/master/efficientdet)
- [The Arm NN TensorFlow Lite delegate](https://github.com/ARM-software/armnn/tree/branches/armnn_21_05/delegate)
- [ARM Compute Librarry](https://github.com/ARM-software/ComputeLibrary)
- [Coral EdgeTPU](https://coral.ai/)
- [PINTO0309/Bazel_bin](https://github.com/PINTO0309/Bazel_bin)
- [PyTorch](https://pytorch.org/)
- [Torchvision](https://pytorch.org/vision/stable/)
- [TensorRT](https://github.com/NVIDIA/TensorRT)
- [meta-tensorflow-lite](https://github.com/NobuoTsukamoto/meta-tensorflow-lite)
- [Yocto Project](https://www.yoctoproject.org/)
# Benchmarks

## About
Benchmarks such as TensorFlow, TensorFlow-Lite, etc...

## Summary

|Description|Benchmarks|Framework|
|:--|:--|:--|
|[TF2 Detection Models<br>Local PC GTX1070](tensorflow/tf2_detection_model_zoo/local_gtx1070.md)|AP, Latancy|TensorFlow<br>XLA Auto-clustering|
|[TF2 Detection Models<br>Colab Tesla P100](tensorflow/tf2_detection_model_zoo/colab_p100.md)|AP, Latancy|TensorFlow<br>TF-TRT<br>XLA Auto-clustering|
|[TF2 Detection Models<br>Colab Tesla V100](tensorflow/tf2_detection_model_zoo/colab_v100.md)|AP, Latancy|TensorFlow|
|[TF2 Detection Models<br>V100 vs P100 vs GTX1070](tensorflow/tf2_detection_model_zoo/v100_vs_p100_vs_gtx1070.md)|Latancy|TensorFlow|
|[TensorFlow 1 Detection Model Zoo<br>Raspberry Pi](tensorflow/lite/tf1_detection_model_zoo/raspi.md)|AP, Latancy|TensorFlow Lite|
|[EfficientDet-Lite<br>Raspberry Pi](tensorflow/lite/efficentdet/efficientdet.md)|AP, Latancy|TensorFlow Lit<br>XNNPACK delegate<br>ARM NN delegate|


## Reference
- [TensorFlow 1 Detection Model Zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf1_detection_zoo.md)
- [TensorFlow 2 Detection Model Zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md)
- [TensorFlow XLA Auto-clustering](https://www.tensorflow.org/xla#auto-clustering)
- [TF-TRT (tensorflow / tensorrt)](https://github.com/tensorflow/tensorrt)
- FP32 XNNPACK: [PINTO0309/TensorflowLite-bin](https://github.com/PINTO0309/TensorflowLite-bin)
- [EfficientDet](https://github.com/google/automl/tree/master/efficientdet)
- [The Arm NN TensorFlow Lite delegate](https://github.com/ARM-software/armnn/tree/branches/armnn_21_05/delegate)
- [ARM Compute Librarry](https://github.com/ARM-software/ComputeLibrary)
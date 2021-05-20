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
|[TensorFlow Lite (TensorFlow 1 Detection Model Zoo)](tensorflow/lite/tf1_detection_model_zoo/raspi.md)|Latancy|TensorFlow Lite<br>(XNNPACK)|


## Reference
- [TensorFlow 1 Detection Model Zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf1_detection_zoo.md)
- [TensorFlow 2 Detection Model Zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md)
- [TensorFlow XLA Auto-clustering](https://www.tensorflow.org/xla#auto-clustering)
- [TF-TRT (tensorflow / tensorrt)](https://github.com/tensorflow/tensorrt)
- FP32 XNNPACK: [PINTO0309/TensorflowLite-bin](https://github.com/PINTO0309/TensorflowLite-bin)
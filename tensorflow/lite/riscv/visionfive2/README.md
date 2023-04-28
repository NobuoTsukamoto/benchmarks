
# TensorFlow Lite on VisionFive 2 Benchmarks

## Environment

HW
  - StarFive VisionFive 2

OS
  - 202302 Release
    Linux geerling-image-69-vf2 5.15.0-starfive #1 SMP Mon Feb 27 14:03:14 EST 2023 riscv64 GNU/Linux

SW
  - TensorFlow Lite v2.12.0 (build from source)  
    build option
    ```bash
      cmake \
        -DTFLITE_ENABLE_XNNPACK=ON \
        -DTFLITE_ENABLE_GPU=ON \
        -DXNNPACK_ENABLE_RISCV_VECTOR=OFF
    ```

## How to benchmarks
  - XNNPACK delegate
    ```bash
    benchmark_model \
      --graph=_PATH_TO_TF_LITE_MODEL_FILE_ \
      --use_xnnpack=true \
      --num_threads=`N` (number of threads)
    ```
  - GPU delegate
    ```bash
    benchmark_model \
      --graph=_PATH_TO_TF_LITE_MODEL_FILE_ \
      --use_gpu=true
    ```

## Models
- [Pretrained EfficientDet Checkpoints - google/automl](https://github.com/google/automl/tree/42ad3a40d237cb11b0894be69ba5855f41ae645f/efficientdet#2-pretrained-efficientdet-checkpoints)
- [NobuoTsukamoto/export-efficientdet-lite-tf-lite-model.ipynb](https://gist.github.com/NobuoTsukamoto/c47ed552c412db4dbfac97a8568f17f0)

## Results
- [results](./results)

## Latency mean (ms)

### XNNPACK delegate
| Model               |Input  | Num threads | FP32     | INT8      |
|:--------------------|:----  |------------:|---------:|----------:|
| EfficientDet-lite0  |320x320|           1 |  1800.89 |  10311.40 |
|                     |       |           2 |   967.87 |   5286.31 |
|                     |       |           3 |   696.26 |   3848.13 |
|                     |       |           4 |   551.99 |   2926.33 |
| EfficientDet-lite1  |384x384|           1 |  3537.45 |  20653.00 |
|                     |       |           2 |  1914.71 |  10537.50 |
|                     |       |           3 |  1313.44 |   7390.17 |
|                     |       |           4 |  1035.22 |   5676.72 |
| EfficientDet-lite2  |448x448|           1 |  5904.75 |  35009.50 |
|                     |       |           2 |  3132.86 |  17824.50 |
|                     |       |           3 |  2202.07 |  12737.20 |
|                     |       |           4 |  1729.77 |   9450.72 |
| EfficientDet-lite3  |512x512|           1 | 13194.90 |  76227.10 |
|                     |       |           2 |  6861.08 |  38823.50 |
|                     |       |           3 |  4791.45 |  26623.60 |
|                     |       |           4 |  3798.13 |  20067.00 |
| EfficientDet-lite3x |640x640|           1 | 22824.20 | 141339.00 |
|                     |       |           2 | 11799.90 |  71824.70 |
|                     |       |           3 |  8341.26 |  49117.90 |
|                     |       |           4 |  6369.91 |  36906.40 |
| EfficientDet-lite4  |640x640|           1 | 32395.60 | 202239.00 |
|                     |       |           2 | 16824.10 | 102514.00 |
|                     |       |           3 | 11574.00 |  70122.80 |
|                     |       |           4 |  8932.28 |  52694.40 |


### GPU delegate
| Model               |Input  | FP32    | INT8    |
|:--------------------|:----  |--------:|--------:|
| EfficientDet-lite0  |320x320|  436.08 |  451.45 |
| EfficientDet-lite1  |384x384|  712.76 |  716.21 |
| EfficientDet-lite2  |448x448| 1073.37 | 1095.76 |
| EfficientDet-lite3  |512x512| 1817.58 | 1873.07 |
| EfficientDet-lite3x |640x640| 3280.28 | 3364.11 |
| EfficientDet-lite4  |640x640| 4384.98 | 4407.78 |

# EfficientDet TensorFlow Lite Benchmarks

## Environment

- HW
  - RasPi4: Raspberry Pi 4 Model B Rev 1.2 4GB
  - RasPi3 B+: Raspberry Pi 3 Model B+ 2GB
  - RasPi3 V1.2: Raspberry Pi 3 Model B V1.2
  - RasPi2 V1.1: Raspberry Pi 2 Model B V1.1 
- OS
  - Raspberry Pi OS 64bit (raspios_arm64-2021-04-09)
    Linux raspberrypi 5.10.36-v8+ #1418 SMP PREEMPT Thu May 13 18:19:53 BST 2021 aarch64 GNU/Linux
- SW
  - TensorFlow Lite 2.5.0
    - FP32 XNNPACK: [PINTO0309/TensorflowLite-bin](https://github.com/PINTO0309/TensorflowLite-bin)
    - INT8: [TensorFlow Lite 2.5.0](https://github.com/tensorflow/tensorflow/releases/tag/v2.5.0)
  - OpenCV 4.5.2 (Self build)
  - Python3 3.7.3
  - ARM NN Delegate
    - Arm NN v21.05
    - Arm Compute Library v21.05
  - Coral EdgeTPU Delegate
    - libEdgeTPU Release Frogfish
    - Edge TPU Compiler version 15.0.340273435

## Dataset
- [COCO2017](https://cocodataset.org/#home)

## How to benchmarks
Source
- [NobuoTsukamoto/tflite-cv-example](https://github.com/NobuoTsukamoto/tflite-cv-example/)

```
# AP
$ Python object_detection_benchmark_tflite.py --model PATH_TO_MODEL_FILE --images_dir /PATH_TO_COCO2017VAL --annotation_path PATH_TO_instances_val2017.json --threads 4

# Latancy
$ python benchmark_tflite.py --model _PATH_TO_MODEL_FILE --thread=N(num threads) --count 350
```

Models
- [Pretrained EfficientDet Checkpoints - google/automl](https://github.com/google/automl/tree/42ad3a40d237cb11b0894be69ba5855f41ae645f/efficientdet#2-pretrained-efficientdet-checkpoints)
- [NobuoTsukamoto/export-efficientdet-lite-tf-lite-model.ipynb](https://gist.github.com/NobuoTsukamoto/c47ed552c412db4dbfac97a8568f17f0)

## Results
- [All results](./results)

## COCO2017VAL mAP
- -: Segmantation fault
- *: Edge TPU Compiler Internal compiler error. Aborting!
- **: Transfer on tag 1 failed. Abort. Deadline exceeded: USB transfer error 2 [LibUsbDataOutCallback].   
  See details (https://github.com/google-coral/edgetpu/issues/11).

| Model               |Input  | FP32<br>XNNPACK delegate | FP32<br>ARM NN delegate | INT8       | EdgeTPU    |
|:--------------------|:----  |-------------------------:|------------------------:|-----------:|-----------:|
| EfficientDet-lite0  |320x320|                    26.03 |                   26.03 |      25.65 |      25.54 |
| EfficientDet-lite1  |384x384|                    30.16 |                   30.16 |      29.61 |      29.7  |
| EfficientDet-lite2  |448x448|                    33.16 |                   33.16 |      32.72 |      28.5  |
| EfficientDet-lite3  |512x512|                    36.32 |                   36.32 |      36    |          * |
| EfficientDet-lite3x |640x640|      　　　　　　　38.68 |                   38.68 |      38.24 |         ** |
| EfficientDet-lite4  |640x640|      　　　　　　　39.7  |                       - |      39.38 |          * |


## Latency mean (ms)
- FP32: XNNPACK delegate
- *: Transfer on tag 1 failed. Abort. Deadline exceeded: USB transfer error 2 [LibUsbDataOutCallback].   
  See details (https://github.com/google-coral/edgetpu/issues/11).
- **: bad_alloc error.

























| Model               |Input  |Kind        |Threads   |RasPi2 V1.2 32bit|RasPi3 V1.2 32bit |RasPi3 V1.2 64bit |RasPi3 B+ 32bit  |RasPi3 B+ 64bit  |RasPi4 32bit     |RasPi4 64bit     |
|:--------------------|:----  |:-----------|---------:|----------------:|----------------:|------------------:|----------------:|----------------:|----------------:|----------------:|
| EfficientDet-lite0  |320x320|FP32        |        1 |                 |                 |                   |          781.42 |          720.83 |          390.53 |          354.84 |
|                     |       |            |        2 |                 |                 |                   |          504.12 |          483.75 |          255.46 |          232.89 |
|                     |       |            |        3 |                 |                 |                   |          419.68 |          414.90 |          221.25 |          201.95 |
|                     |       |            |        4 |                 |                 |                   |          378.83 |          342.94 |          211.91 |          193.39 |
|                     |       |INT8        |        1 |                 |                 |            727.91 |          834.33 |          624.07 |          415.20 |          344.03 |
|                     |       |            |        2 |                 |                 |            452.35 |          489.97 |          388.97 |          252.07 |          232.77 |
|                     |       |            |        3 |                 |                 |            366.23 |          380.45 |          317.03 |          200.77 |          143.85 |
|                     |       |            |        4 |                 |                 |            323.70 |          325.58 |          277.76 |          119.99 |          122.06 |
|                     |       |EdgeTPU     |        1 |                 |                 |            525.40 |          138.78 |          468.48 |          134.98 |           99.77 |
| EfficientDet-lite1  |384x384|FP32        |        1 |                 |                 |                   |         1532.98 |         1191.83 |          736.27 |          691.68 |
|                     |       |            |        2 |                 |                 |                   |          987.37 |          780.83 |          455.01 |          424.00 |
|                     |       |            |        3 |                 |                 |                   |          806.23 |          650.56 |          387.35 |          362.36 |
|                     |       |            |        4 |                 |                 |                   |          718.50 |          652.47 |          371.40 |          348.76 |
|                     |       |INT8        |        1 |                 |                 |           1399.45 |         1590.94 |         1131.02 |          774.12 |          546.90 |
|                     |       |            |        2 |                 |                 |            850.91 |          919.48 |          675.48 |          452.86 |          324.85 |
|                     |       |            |        3 |                 |                 |            678.96 |          703.03 |          532.03 |          349.22 |          251.86 |
|                     |       |            |        4 |                 |                 |            593.82 |          595.76 |          458.83 |          293.58 |          211.73 |
|                     |       |EdgeTPU     |        1 |                 |                 |            774.14 |          188.16 |          693.04 |          170.43 |          141.15 |
| EfficientDet-lite2  |448x448|FP32        |        1 |                 |                 |                   |         2487.69 |         2145.50 |         1175.96 |         1098.97 |
|                     |       |            |        2 |                 |                 |                   |         1609.35 |         1272.05 |          733.35 |          690.23 |
|                     |       |            |        3 |                 |                 |                   |         1297.75 |         1046.23 |          631.99 |          589.15 |
|                     |       |            |        4 |                 |                 |                   |         1147.47 |          963.23 |          593.51 |          565.30 |
|                     |       |INT8        |        1 |                 |                 |           2201.83 |         2488.91 |         1785.89 |         1196.17 |          857.87 |
|                     |       |            |        2 |                 |                 |           1325.39 |         1431.96 |         1057.31 |          703.44 |          505.17 |
|                     |       |            |        3 |                 |                 |           1058.44 |         1093.88 |          836.27 |          533.97 |          394.94 |
|                     |       |            |        4 |                 |                 |            917.29 |          918.52 |          711.60 |          449.62 |          331.20 |
|                     |       |EdgeTPU     |        1 |                 |                 |           1267.29 |          299.01 |         1138.33 |          285.80 |          219.76 |
| EfficientDet-lite3  |512x512|FP32        |        1 |                 |                 |                   |         5417.56 |         7206.10 |         2437.04 |         2308.64 |
|                     |       |            |        2 |                 |                 |                   |         3163.71 |         4272.14 |         1456.22 |         1370.47 |
|                     |       |            |        3 |                 |                 |                   |         2523.05 |         3471.59 |         1226.60 |         1167.75 |
|                     |       |            |        4 |                 |                 |                   |         2181.24 |         3149.46 |         1193.19 |         1139.21 |
|                     |       |INT8        |        1 |                 |                 |           4203.37 |         4712.73 |         3414.30 |         2270.01 |         1657.71 |
|                     |       |            |        2 |                 |                 |           2449.24 |         2644.12 |         1965.97 |         1281.57 |          948.42 |
|                     |       |            |        3 |                 |                 |           1890.65 |         1978.40 |         1495.18 |          968.61 |          716.57 |
|                     |       |            |        4 |                 |                 |           1614.45 |         1636.10 |         1260.19 |          789.91 |          601.34 |
| EfficientDet-lite3x |640x640|FP32        |        1 |                 |                 |                   |         9362.97 |         4094.17 |         4277.40 |         4089.07 |
|                     |       |            |        2 |                 |                 |                   |         5609.27 |         2497.62 |         2563.39 |         2472.28 |
|                     |       |            |        3 |                 |                 |                   |         4464.57 |         2009.69 |         2139.81 |         2067.91 |
|                     |       |            |        4 |                 |                 |                   |         3889.91 |         1814.83 |         2086.10 |         2015.04 |
|                     |       |INT8        |        1 |                 |                 |           7476.25 |         8399.33 |         2130.3  |         4034.59 |         2979.10 |
|                     |       |            |        2 |                 |                 |           4312.28 |         4654.59 |         3463.11 |         2243.64 |         1685.61 |
|                     |       |            |        3 |                 |                 |           3309.98 |         3445.96 |         2622.84 |         1664.28 |         1267.22 |
|                     |       |            |        4 |                 |                 |           2798.00 |         2839.76 |         2191.00 |         1377.81 |         1050.79 |
|                     |       |EdgeTPU     |        1 |                 |                 |                 * |               * |               * |               * |               * |
| EfficientDet-lite4  |640x640|FP32        |        1 |                 |                 |                   |        13163.81 |              ** |         5943.51 |         5743.08 |
|                     |       |            |        2 |                 |                 |                   |         7790.65 |              ** |         3511.83 |         3399.70 |
|                     |       |            |        3 |                 |                 |                   |         6069.23 |              ** |         2974.06 |         2835.45 |
|                     |       |            |        4 |                 |                 |                   |         5214.19 |              ** |         2878.69 |         2847.02 |
|                     |       |INT8        |        1 |                 |                 |          10082.42 |        11087.51 |         8242.53 |         5237.25 |         4008.46 |
|                     |       |            |        2 |                 |                 |           5710.84 |         6071.24 |         4601.04 |         2911.11 |         2244.46 |
|                     |       |            |        3 |                 |                 |           4348.49 |         4446.50 |         3463.92 |         2145.94 |         1659.16 |
|                     |       |            |        4 |                 |                 |           3608.48 |         3599.83 |         2841.39 |         1717.24 |         1360.11 |

## ARM NN Delegate Latency mean (ms)
- Delegate Parameter : `{'backends': 'CpuAcc', 'logging-severity': 'info', 'number-of-threads': 'N', 'enable-fast-math': 'true'}`  
  N: Num of Threads
- -: Segmantation fault

| Model               |Input  |Kind        |Threads   |RasPi3 64bit|RasPi4 64bit|
|:--------------------|:----  |:-----------|---------:|-----------:|-----------:|
| EfficientDet-lite0  |320x320|FP32        |        1 |    1016.98 |     520.00 |
|                     |       |            |        2 |     618.40 |     320.08 |
|                     |       |            |        3 |     497.48 |     258.25 |
|                     |       |            |        4 |     442.76 |     229.91 |
|                     |       |INT8        |        1 |    2064.85 |    1187.71 |
|                     |       |            |        2 |    1081.59 |     636.04 |
|                     |       |            |        3 |     795.55 |     464.67 |
|                     |       |            |        4 |     628.61 |     363.14 |
| EfficientDet-lite1  |384x384|FP32        |        1 |    1760.95 |     917.73 |
|                     |       |            |        2 |    1063.56 |     568.35 |
|                     |       |            |        3 |     846.41 |     454.73 |
|                     |       |            |        4 |     772.97 |     413.50 |
|                     |       |INT8        |        1 |    3895.82 |    2300.32 |
|                     |       |            |        2 |    2060.10 |    1215.24 |
|                     |       |            |        3 |    1447.93 |     849.08 |
|                     |       |            |        4 |    1158.61 |     676.47 |
| EfficientDet-lite2  |448x448|FP32        |        1 |    2712.48 |    1419.79 |
|                     |       |            |        2 |    1627.73 |     884.95 |
|                     |       |            |        3 |    1305.44 |     706.44 |
|                     |       |            |        4 |    1176.66 |     624.21 |
|                     |       |INT8        |        1 |    5863.40 |    3524.52 |
|                     |       |            |        2 |    3088.07 |    1850.40 |
|                     |       |            |        3 |    2218.84 |    1315.06 |
|                     |       |            |        4 |    1742.30 |    1016.84 |
| EfficientDet-lite3  |512x512|FP32        |        1 |    4891.51 |    2772.21 |
|                     |       |            |        2 |    2867.34 |    1665.98 |
|                     |       |            |        3 |    2292.63 |    1348.81 |
|                     |       |            |        4 |    2048.76 |    1190.78 |
|                     |       |INT8        |        1 |   10307.17 |    6244.21 |
|                     |       |            |        2 |    5374.72 |    3241.10 |
|                     |       |            |        3 |    3824.26 |    2297.68 |
|                     |       |            |        4 |    2954.27 |    1751.42 |
| EfficientDet-lite3x |640x640|FP32        |        1 |          - |    4699.25 |
|                     |       |            |        2 |          - |    2843.76 |
|                     |       |            |        3 |          - |    2238.66 |
|                     |       |            |        4 |          - |    2018.51 |
|                     |       |INT8        |        1 |   17802.66 |   10737.77 |
|                     |       |            |        2 |    9204.81 |    5561.44 |
|                     |       |            |        3 |    6509.33 |    3907.89 |
|                     |       |            |        4 |    5128.52 |    3001.89 |
| EfficientDet-lite4  |640x640|FP32        |        1 |          - |          - |
|                     |       |            |        2 |          - |          - |
|                     |       |            |        3 |          - |          - |
|                     |       |            |        4 |          - |          - |
|                     |       |INT8        |        1 |   22841.22 |   14074.93 |
|                     |       |            |        2 |   11882.22 |    7238.01 |
|                     |       |            |        3 |    8330.73 |    5070.61 |
|                     |       |            |        4 |    6427.59 |    3883.23 |

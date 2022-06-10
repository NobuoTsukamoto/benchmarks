
# TensorFlow Lite on RISC-V CPU Benchmarks

## Environment

HW
  - Sipeed Lichee RV Dock Allwinner D1 Development Board RISC-V Linux Starter Kit
  - cpu info
    ```
    cat /proc/cpuinfo 
    processor       : 0
    hart            : 0
    isa             : rv64imafdc
    mmu             : sv39
    uarch           : thead,c906
    ```

OS
  - Linux nezha-allwinner-d1 5.16.0-nezha #1 PREEMPT Sun Jan 16 18:33:32 UTC 2022 riscv64 riscv64 riscv64 GNU/Linux

SW
  - Yocto Project
    ```
    # image:  core-image-full-cmdline

    Build Configuration:
    BB_VERSION           = "2.0.0"
    BUILD_SYS            = "x86_64-linux"
    NATIVELSBSTRING      = "ubuntu-20.04"
    TARGET_SYS           = "riscv64-oe-linux"
    MACHINE              = "nezha-allwinner-d1"
    DISTRO               = "nodistro"
    DISTRO_VERSION       = "nodistro.0"
    TUNE_FEATURES        = "riscv64"
    meta                 = "kirkstone:4eb0b7468383a1d0314b3bfd43ea37c95de464d9"
    meta-oe              
    meta-python          
    meta-networking      
    meta-multimedia      = "kirkstone:0b78362654262145415df8211052442823b9ec9b"
    meta-riscv           = "kirkstone:70e099d7ceca52a1dde2c978713012f6b20a9891"
    meta-tensorflow-lite = "main:a58e5f1efbf5de17580e1f9f65f70d76715003b2"
    ```

## How to benchmarks
- [TFLite Model Benchmark Tool with C++ Binary - tensorflow](https://github.com/tensorflow/tensorflow/tree/v2.9.1/tensorflow/lite/tools/benchmark)
- [TFLite Model Benchmark Tool with C++ Binary - meta-tensorflow-tensorflow](https://github.com/NobuoTsukamoto/meta-tensorflow-lite/blob/main/doc/tensorflow-lite-benchmark.md)

```
benchmark_model \
  --graph=_PATH_TO_TF_LITE_MODEL_FILE_ \
  --use_xnnpack=true \
  --num_threads=1
```

## Models
- [MobileNet - tensorflow/models](https://github.com/tensorflow/models/tree/master/research/slim/nets/mobilenet)

## Results
- [results](./results)

## Latency mean (ms)

| Model name                | Input   | Kind | Lichee RV Dock<br>XNNPACK delegate |
|:--------------------------|:--------|:-----|-----------------------------------:|
| Mobilenet V1 dm=1.0       | 224x224 | FP32 |  2874.29                           |
|                           |         | INT8 | 10091.20                           |
| Mobilenet V2  dm=1.0      | 224x224 | FP32 |   978.40                           |
|                           |         | INT8 |  6210.03                           |
| Mobilenet V3 Large dm=1.0 | 224x224 | FP32 |   754.20                           |
|                           |         | INT8 |  4853.66                           |
| Mobilenet V3 Small dm=1.0 | 224x224 | FP32 |   241.70                           |
|                           |         | INT8 |  1444.20                           |

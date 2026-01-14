import time

import psutil
import pynvml
from prometheus_client import Gauge, start_http_server


# init NVML (single GPU for now)
pynvml.nvmlInit()
GPU_HANDLE = pynvml.nvmlDeviceGetHandleByIndex(0)


# system metrics
cpu_usage = Gauge(
    "lab_cpu_usage_percent",
    "CPU usage percent",
)

memory_usage = Gauge(
    "lab_memory_usage_percent",
    "Memory usage percent",
)


# gpu metrics
gpu_temperature = Gauge(
    "lab_gpu_temperature_celsius",
    "GPU temperature in Celsius",
)

gpu_utilization = Gauge(
    "lab_gpu_utilization_percent",
    "GPU utilization percent",
)

gpu_vram_used = Gauge(
    "lab_gpu_vram_used_mb",
    "GPU VRAM used (MB)",
)

gpu_vram_total = Gauge(
    "lab_gpu_vram_total_mb",
    "GPU VRAM total (MB)",
)

gpu_power = Gauge(
    "lab_gpu_power_watts",
    "GPU power usage (W)",
)


def collect_metrics():
    cpu_usage.set(psutil.cpu_percent(interval=None))
    memory_usage.set(psutil.virtual_memory().percent)

    util = pynvml.nvmlDeviceGetUtilizationRates(GPU_HANDLE)
    mem = pynvml.nvmlDeviceGetMemoryInfo(GPU_HANDLE)
    temp = pynvml.nvmlDeviceGetTemperature(
        GPU_HANDLE, pynvml.NVML_TEMPERATURE_GPU
    )
    power = pynvml.nvmlDeviceGetPowerUsage(GPU_HANDLE) / 1000.0

    gpu_utilization.set(util.gpu)
    gpu_vram_used.set(mem.used / (1024 * 1024))
    gpu_vram_total.set(mem.total / (1024 * 1024))
    gpu_temperature.set(temp)
    gpu_power.set(power)


if __name__ == "__main__":
    start_http_server(8000)

    while True:
        collect_metrics()
        time.sleep(5)

# Hardware Metrics Lab

## Overview
Hardware Metrics Lab is a small personal project for exploring real-time
hardware monitoring in local network environments.

The goal is to better understand how lightweight agents, pull-based metrics
collection, and time-series dashboards fit together to provide practical
visibility into system behavior, without depending on cloud services or
vendor-specific solutions.

## Problem
In many studio, lab, and on-prem setups, machines operate entirely inside
a local network and often have limited or no internet access. Despite this,
there is still a need to observe system health, resource usage, and performance
patterns across multiple machines in near real time.

## High-Level Architecture

[Node Agent] → [Metrics Collector] → [Time-Series Storage] → [Dashboard]

Each machine runs a minimal agent that exposes hardware metrics over HTTP.
A central collector periodically scrapes these endpoints and stores the data
for visualization and analysis.

## Design Principles

- One lightweight agent per machine
- Pull-based metrics collection
- LAN-friendly and firewall-safe by default
- Designed with Windows-first environments in mind
- Keep the system simple, explicit, and easy to reason about

## Non-Goals

- Building a complete monitoring product
- Replacing existing enterprise observability platforms
- Strong coupling to any single vendor or ecosystem

## Tooling & Dependencies

This project uses a small set of well-established tools and libraries.
Nothing custom or proprietary is required.

### Runtime
- **Python 3.9+**  
  Used for the node agent implementation.  
  https://www.python.org/

### Metrics Collection
- **Prometheus**  
  Used as the central metrics collector (pull-based scraping).  
  https://prometheus.io/

- **prometheus-client (Python)**  
  Exposes metrics in Prometheus format over HTTP.  
  https://github.com/prometheus/client_python

### System Metrics
- **psutil**  
  Cross-platform system and process metrics (CPU, memory).  
  https://github.com/giampaolo/psutil

### GPU Metrics
- **nvidia-ml-py (NVML bindings)**  
  Accesses NVIDIA GPU telemetry (temperature, utilization, memory, power).  
  https://github.com/nicolargo/nvidia-ml-py

> Note: GPU metrics require an NVIDIA GPU with a compatible driver installed.

### Visualization
- **Grafana / Grafana Cloud**  
  Used for dashboarding and visualization of collected metrics.  
  https://grafana.com/

## Validation

Collected metrics were validated using real workloads (e.g. Cinebench)
to confirm that observed CPU and GPU behavior reflects actual system load,
rather than synthetic or sampled data artifacts.

Short visual references (screenshots or GIFs) are provided in the `docs/`
directory for context.

## Status
This repository is intended as a learning and experimentation space.
The focus is on correctness, clarity, and understanding system behavior,
rather than completeness or production scale.

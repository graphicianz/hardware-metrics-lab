# Hardware Metrics Lab

## Overview
Hardware Metrics Lab is a small side project focused on exploring real-time
hardware monitoring in local network environments.

The project looks at how lightweight agents, pull-based metrics collection,
and time-series dashboards can work together to provide practical operational
visibility, without relying on cloud services or proprietary platforms.

## Problem
In many studio, lab, and on-prem environments, machines operate entirely within
a LAN and may not have direct internet access. Even so, there is still a need
to understand system health, resource usage, and performance trends across
multiple machines in near real time.

## High-Level Architecture

[Node Agent] → [Metrics Collector] → [Time-Series Storage] → [Dashboard]

Each machine runs a minimal agent that exposes hardware metrics over HTTP.
A central collector periodically scrapes these endpoints and stores the data
for visualization and analysis.

## Design Principles

- Agent-based architecture (one agent per machine)
- Pull-based metrics collection
- LAN-friendly and firewall-safe by design
- Windows-first environment considerations
- Keep operational complexity low and transparent

## Non-Goals

- Building a full-featured monitoring product
- Cloud-hosted or SaaS-based monitoring
- Tight coupling to any specific vendor or platform

## Status
This repository is intended as a learning and experimentation space.
The focus is on clarity and correctness rather than completeness or scale.

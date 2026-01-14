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

## Status
This repository is intended as a learning and experimentation space.
The focus is on correctness, clarity, and understanding the system behavior,
rather than completeness or production scale.

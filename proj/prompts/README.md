# Kubernetes RCA Prompts

This directory contains the prompt definitions used to benchmark single-agent and multi-agent Root Cause Analysis (RCA) approaches on the 15 Kubernetes incident scenarios in [`proj/examples/`](../examples.md).

## Overview

| Path | Approach | Description |
| --- | --- | --- |
| [`base.md`](./base.md) | **Single-Agent (Baseline)** | Minimal 1-sentence prompt asking for incident RCA from `context` without structured prompt engineering techniques. |
| [`optimal.md`](./optimal.md) | **Single-Agent (Optimized)** | Structured single-agent prompt applying all 6 prompt engineering components (`Persona/Role`, `Context/State`, `Instructions/Tasks`, `Constraints`, `Few-shot Examples`, `Expected Format of Output`). |
| [`mas/`](./mas/README.md) | **Multi-Agent System (MAS)** | Coordinator + 3 domain specialist prompts (`k8s-config-events`, `logs-connectivity`, `metrics-telemetry`) for distributed RCA. |

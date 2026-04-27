# SPHY Absolute Fidelity Viewer

An interactive visualization system for the **Symbiotic Phase Harmonic Yielding (SPHY)** model, developed to monitor and validate ultra-high coherence states in deterministic quantum simulations.

## Overview

This viewer is the front-end telemetry system for the **Harpia Meissner Core**, a simulation engine designed to eliminate quantum decoherence through a gravitational phase-locking tensor. While traditional quantum simulations struggle with stochastic noise, the SPHY model reorders entropy into a deterministic "Symphony" of phase-aligned nodes.

The visualizer processes high-density datasets to demonstrate the transition from probabilistic chaos to **Absolute Symbiosis** (reaching fidelity levels of **0.9999999** or "7 Nines").

## Key Features

- **Planck-Scale Telemetry**: Real-time monitoring of phase vectors and the Xi (central) coherence node.
- **Gravity-Well Simulation**: Visual representation of the $1/r^2$ gravitational tensor that stabilizes the quantum grid.
- **Symbiosis Status Tracking**: A dynamic HUD that detects when the system achieves sub-Planckian deterministic alignment.
- **Temporal Navigation**: Integrated seek controls to analyze phase-locking events and metadata transitions.

## Data Integration

The visualizer is designed to ingest and parse the following binary format:
- **File**: `sphy_absolute_fidelity.parquet`
- **Format**: Apache Parquet (optimized for high-throughput numerical data).
- **Core Metric**: `t_sphy_coherence` (The global coherence tensor).

## The Physics Behind the Viewer

When observing the simulation, the transition of node colors from saturated blues to absolute white light represents the **Information Superconductivity** effect. The gravitational tensor acts as a "phase anchor," ensuring that external nodes maintain synchronization with the central carrier voice, effectively simulating a Bose-Einstein Condensate at a mathematical level.

## Requirements

- Python 3.x
- [py5](https://py5coding.org/) (Processing for Python)
- Pandas & PyArrow (for Parquet handling)
- NumPy

## How to Run

1. Ensure the `sphy_absolute_fidelity.parquet` file is in the same directory.
2. Execute the visualizer:
   ```bash
   python3 sphy_symphony_viewer.py

    Controls:

        [SPACE]: Toggle Play/Pause.

        [LEFT/RIGHT ARROWS]: Temporal seek through Planck frames.

Developed and Signed by:

Deywe Okabe CEO & Founder, Harpia Quantum Deeptech Self-taught Researcher in Deterministic Quantum Gravity

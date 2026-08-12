# Railway Digital Twin Safety Verifier

> **Status: 🔵 Completed / Portfolio Maintained**

A Python-based railway simulation and analytics project that combines a **digital-twin representation of railway operations**, data-driven intelligence, network analysis, simulation, and safety-oriented verification.

The project was built to explore a practical question:

> **Can a railway operating state be simulated, inspected, and checked for unsafe conditions before an operational decision is accepted?**

This repository is a research/engineering project and is **not a production railway control system**.

## What It Demonstrates

- Digital-twin style modelling of railway entities and operational state
- Railway schedule and event data processing
- Platform occupancy and tracking logic
- Railway network construction and analysis
- Simulation of operational scenarios
- Data-driven analytics and intelligent processing
- Safety-oriented rule/verification logic
- Interactive Streamlit visualization
- Dataset transformation and performance optimization

## System Overview

```text
Railway Data
     │
     ▼
Data Ingestion & Transformation
     │
     ▼
┌──────────────────────────────┐
│ Railway Digital Twin         │
│ trains / stations / routes   │
│ schedules / platform state   │
└──────────────┬───────────────┘
               │
       ┌───────┴────────┐
       ▼                ▼
 Network Analysis    Intelligence
       │                │
       └───────┬────────┘
               ▼
          Simulation
               │
               ▼
      Safety Verification
               │
       ┌───────┴────────┐
       ▼                ▼
    Allowed          Conflict /
    State            Unsafe State
               │
               ▼
        Streamlit Dashboard
```

## Main Components

| Component | Purpose |
|---|---|
| `src/digital_twin/` | Digital-twin domain/state modelling |
| `src/railway/` | Railway-specific logic and operational rules |
| `src/simulation/` | Scenario and operational simulation |
| `src/network/` | Railway network construction and analysis |
| `src/intelligence/` | Dataset analysis and intelligent processing |
| `src/ai/` | Predictive/intelligent components |
| `src/logging/` | Application logging |
| `src/utils/` | Shared utilities |
| `dashboard/` | Streamlit interactive interface |
| `data/` | Sample and processed railway datasets |
| `config/` | Configuration |
| `docs/` | Supporting technical documentation |

## Dashboard

The Streamlit dashboard provides an interactive way to inspect railway data and simulation state.

### Current capabilities

- Upload railway datasets in supported formats
- Automatic dataset/column inspection
- Railway network visualization
- Station and route analysis
- Schedule and operational analytics
- Platform occupancy inspection
- Time-based exploration of train events
- Data-quality metrics
- Interactive charts and visualizations

## Data Engineering & Performance Work

One part of the project focused on handling a large schedule dataset efficiently.

An original JSON schedule dataset was transformed into a more efficient CSV representation using `convert_schedules_to_csv.py`.

The repository documentation records an approximately **80 MB → 32 MB** reduction for the processed dataset and substantially faster loading compared with the original JSON workflow.

The project also uses caching and delayed data loading in the dashboard to avoid unnecessarily loading large datasets during startup.

## Technology Stack

- **Python**
- **Streamlit**
- **Pandas / NumPy**
- **Plotly / Matplotlib**
- **NetworkX**
- **scikit-learn**

## Quick Start

### 1. Clone

```bash
git clone https://github.com/Balu-Annapureddy/digital_twin_railway_safety_verifier.git
cd digital_twin_railway_safety_verifier
```

### 2. Create an environment

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the dashboard

```bash
streamlit run dashboard/app.py
```

The dashboard normally opens at `http://localhost:8501`.

## Project Structure

```text
.
├── dashboard/
├── config/
├── data/
├── docs/
├── scenarios/
├── src/
│   ├── ai/
│   ├── digital_twin/
│   ├── intelligence/
│   ├── logging/
│   ├── network/
│   ├── railway/
│   ├── simulation/
│   └── utils/
├── convert_schedules_to_csv.py
├── requirements.txt
└── README.md
```

## Documentation

- [`QUICKSTART.md`](QUICKSTART.md) — additional setup and usage notes
- [`OPTIMIZATION_GUIDE.md`](OPTIMIZATION_GUIDE.md) — data/performance notes
- [`PROJECT_SUMMARY.md`](PROJECT_SUMMARY.md) — project history and implementation summary
- [`docs/`](docs/) — technical documentation

## Engineering Notes

This project intentionally separates the **simulation/digital-twin layer** from the **visualization layer**. The dashboard is an interface over the underlying processing and simulation components rather than the core of the project.

The project also explores the distinction between:

- predictive/data-driven intelligence, and
- deterministic operational safety rules.

That separation is important for safety-oriented systems because a prediction should not automatically be treated as permission to perform an operational action.

## Limitations

This is an academic/research prototype using datasets and simulation rather than live railway infrastructure.

It should **not** be used for real railway signalling, dispatching, train control, or safety-critical operational decisions.

The system does not connect to railway signalling hardware or live railway control networks.

## Project Status

**Completed / Portfolio Maintained**

The project is no longer positioned as a continuously deployed railway platform. Its purpose in this portfolio is to demonstrate engineering work across:

**simulation + digital twins + data engineering + network analysis + intelligent systems + safety verification + interactive visualization.**

## License

See the repository for the current licensing terms.

---

Built as an engineering project exploring how digital representations, simulation, data-driven intelligence, and deterministic verification can work together in a safety-oriented domain.

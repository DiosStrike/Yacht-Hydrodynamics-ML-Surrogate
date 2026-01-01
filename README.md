# Yacht Hydrodynamics Digital Twin: Real-time ML Surrogate & ESG Pipeline

### Principal Investigator: Tanghao Chen (Dios)

---

## Executive Summary

This project implements a high-fidelity **Digital Twin** platform designed for yacht residuary resistance ($R_r$) prediction and energy efficiency monitoring. By leveraging a machine learning surrogate model trained on the **Delft Ship Hydromechanics dataset**, the system enables millisecond-level performance inference, effectively bypassing the computational overhead of traditional Computational Fluid Dynamics (CFD) simulations. 

The platform is developed as part of a professional portfolio to demonstrate the integration of fluid mechanics, structural engineering principles, and data science using Python. It features stochastic physical modeling, a multi-tier expert decision system, and a dynamic hydrodynamic visualizer to provide actionable insights for sustainable maritime operations and ESG (Environmental, Social, and Governance) compliance.

---

## Key Engineering Features

### 1. ML Surrogate Modeling
The core inference engine utilizes a non-linear surrogate model to approximate hull resistance based on six independent geometric and hydrodynamic variables. This allows for real-time sensitivity analysis and rapid design iteration within the established experimental design space of the Delft series.

### 2. Stochastic Telemetry Simulation (Ornstein-Uhlenbeck Process)
To emulate real-world sensor data, the system implements an **Ornstein-Uhlenbeck (OU) stochastic process**. This provides a physically accurate simulation of velocity fluctuations (Froude Number), incorporating mean-reverting tendencies (engine/hull inertia) and Gaussian noise (environmental/wave interference).

### 3. Multi-tier Expert Decision Logic
A robust three-tier alert system provides real-time operational guidance:
* **STABLE / OPTIMAL (Green):** System operating within high-efficiency parameters with minimal environmental impact.
* **CAUTION (Yellow):** Early detection of performance degradation or increased energy intensity.
* **CRITICAL (Red):** Immediate speed reduction or trim adjustment required to meet ESG carbon targets and prevent efficiency loss.

### 4. Dynamic Side-View Wave Visualization
A custom HTML5 Canvas engine renders a vertical-plane hydrodynamic simulation. The water surface profile is dynamically generated through sine wave superposition, where:
* **Wave Amplitude:** Directly driven by the predicted Residuary Resistance ($R_r$).
* **Phase Shift / Velocity:** Synchronized with the Froude Number ($F_r$) to simulate relative motion.
* **Hull Dynamics:** The vessel maintains real-time vertical alignment with the simulated wave surface, effectively modeling the "bobbing" effect.

---

## Technical Specification

### Parameter Definitions
The system adheres to standard naval architecture nomenclature from the Delft Ship Hydromechanics dataset:
* **LC:** Longitudinal position of the center of buoyancy.
* **PC:** Prismatic coefficient.
* **LD:** Length-displacement ratio.
* **BDr:** Beam-draught ratio.
* **LB:** Length-beam ratio.
* **Fr:** Froude number (Dimensionless velocity).
* **Rr:** Residuary resistance (kN).

### Tech Stack
* **Backend:** Python 3.x, Flask (RESTful API Architecture)
* **Computing:** NumPy (Stochastic Calculus & Numerical Methods)
* **Frontend:** JavaScript (ES6+), Chart.js (Telemetry Visualization), Bootstrap 5 (3-6-3 Responsive Layout)
* **Graphics:** HTML5 Canvas API (Real-time Physics Rendering)

---

## Installation and Deployment

### Prerequisites
* Python 3.8 or higher
* pip package manager

### Local Setup
1. Clone the repository:
   ```bash
   git clone [https://github.com/YourUsername/Yacht-Hydrodynamics-ML-Surrogate.git](https://github.com/YourUsername/Yacht-Hydrodynamics-ML-Surrogate.git)
   cd Yacht-Hydrodynamics-ML-Surrogate
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
3. Execute the application:
    ```bash
    python app.py
4. Access the dashboard: Navigate to http://127.0.0.1:5001 in a modern web browser.

# Containerization
The project includes a Dockerfile for standardized deployment:
    ```bash
    docker build -t yacht-digital-twin .
    docker run -p 5001:5001 yacht-digital-twin
---
### Project Structure
    ```text
    .
    ├── data/                   # Dataset repository
    ├── models/                 # Serialized ML models (.pkl)
    │   ├── best_yacht_model.pkl
    │   └── feature_scaler.pkl
    ├── src/                    # Core logic for training and preprocessing
    │   ├── preprocess.py
    │   └── train.py
    ├── app.py                  # Main Flask Web Application
    ├── requirements.txt        # Dependency manifest
    ├── Dockerfile              # Container configuration
    ├── README.md               # Technical documentation
    └── voyage_telemetry.jsonl  # Simulated IoT telemetry logs
    
---
### License
This project is developed for academic and research purposes as part of a Graduate-level AI Engineering Portfolio.
# Yacht Hydrodynamics Digital Twin: Real-time ML Surrogate & ESG Pipeline

### Principal Investigator: Tanghao Chen (Dios)
---
**[English Version](#english-version)** | **[中文说明版](#chinese-version)**
---

<div id="english-version"></div>

# English Version

## Executive Summary

This project implements a high-fidelity **Digital Twin** platform designed for yacht residuary resistance ($R_r$) prediction and energy efficiency monitoring. By leveraging a machine learning surrogate model trained on the **Delft Ship Hydromechanics dataset**, the system enables millisecond-level performance inference, effectively bypassing the computational overhead of traditional Computational Fluid Dynamics (CFD) simulations. 

The platform is developed as part of a professional portfolio to demonstrate the integration of fluid mechanics, structural engineering principles, and data science using Python. It features stochastic physical modeling, a multi-tier expert decision system, and a dynamic hydrodynamic visualizer to provide actionable insights for sustainable maritime operations and ESG (Environmental, Social, and Governance) compliance.

---
> **Live Demo:** [https://yacht-digital-twin-dios.onrender.com](https://yacht-digital-twin-dios.onrender.com)
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
---
# 游艇流体力学数字孪生：实时机器学习代理模型与 ESG 监测系统

### 首席研究员：陈唐昊 (Tanghao Chen / Dios)

---
<div id="chinese-version"></div>

# 中文说明版

## 项目执行摘要 (Executive Summary)

本项目实现了一个高保真**数字孪生 (Digital Twin)** 平台，专门用于游艇剩余阻力 ($R_r$) 预测和能源效率监测。通过利用基于 **Delft 船舶流体力学数据集 (Delft Ship Hydromechanics dataset)** 训练的机器学习代理模型 (Surrogate Model)，系统能够实现毫秒级的性能推理，有效地避开了传统计算流体动力学 (CFD) 模拟带来的巨大计算开销。

该平台作为专业作品集的一部分，旨在展示流体力学、结构工程原理与 Python 数据科学的深度集成。其核心功能包括随机物理建模、多级专家决策系统以及动态流体力学可视化器，为可持续航运操作和 ESG（环境、社会和治理）合规性提供可落地的技术洞察。

---
> **在线演示 (Live Demo):** [https://yacht-digital-twin-dios.onrender.com](https://yacht-digital-twin-dios.onrender.com)
---

## 核心工程亮点

### 1. 机器学习代理建模 (ML Surrogate Modeling)
核心推理引擎采用非线性代理模型，根据六个独立的几何和流体力学变量来近似估算船体阻力。这使得在 Delft 系列建立的实验设计空间内，可以进行实时灵敏度分析和快速的设计迭代。

### 2. 随机遥测模拟 (Ornstein-Uhlenbeck 过程)
为了模拟真实世界的传感器数据，系统引入了 **Ornstein-Uhlenbeck (OU) 随机过程**。这提供了一个物理上准确的航行速度波动（弗劳德数 $F_r$）模拟，结合了均值回归特性（模拟发动机/船体惯性）和高斯噪声（模拟环境/波浪干扰）。

### 3. 多级专家决策逻辑
一个健壮的三级警报系统提供实时操作指导：
* **稳定 / 最佳 (绿色):** 系统在高效参数下运行，对环境影响最小。
* **注意 (黄色):** 早期检测到性能下降或能耗强度增加。
* **危险 (红色):** 需立即降低航速或调整纵倾，以满足 ESG 碳排放目标并防止效率损失。

### 4. 动态侧视波浪可视化
采用自定义 HTML5 Canvas 引擎渲染垂直平面的流体力学模拟。水面轮廓通过正弦波叠加动态生成，其中：
* **波幅 (Amplitude):** 由预测的剩余阻力 ($R_r$) 直接驱动。
* **相位差 / 速度:** 与弗劳德数 ($F_r$) 同步，以模拟相对运动。
* **船体动力学:** 船体与模拟波浪表面保持实时垂直对齐，有效模拟了航行中的“起伏 (Bobbing)”效应。

---

## 技术规范 (Technical Specification)

### 参数定义
系统遵循 Delft 船舶流体力学数据集的标准船舶建筑命名法：
* **LC:** 浮心纵向位置。
* **PC:** 棱形系数。
* **LD:** 长度-排水量比。
* **BDr:** 宽吃水比。
* **LB:** 长宽比。
* **Fr:** 弗劳德数 (无量纲速度)。
* **Rr:** 剩余阻力 (单位: kN)。

### 技术栈
* **后端:** Python 3.x, Flask (RESTful API 架构)
* **计算:** NumPy (随机微积分与数值计算)
* **前端:** JavaScript (ES6+), Chart.js (遥测数据可视化), Bootstrap 5 (响应式布局)
* **图形:** HTML5 Canvas API (实时物理渲染)

---

## 安装与部署

### 环境要求
* Python 3.11 或更高版本
* pip 包管理器

### 本地环境配置
1. 克隆仓库：
   ```bash
   git clone [https://github.com/YourUsername/Yacht-Hydrodynamics-ML-Surrogate.git](https://github.com/YourUsername/Yacht-Hydrodynamics-ML-Surrogate.git)
   cd Yacht-Hydrodynamics-ML-Surrogate
2. 安装依赖：
    ```bash
    pip install -r requirements.txt
3. 运行应用程序：
    ```bash
    python app.py
4. 访问仪表盘：在现代浏览器中访问 http://127.0.0.1:5001

# 容器化部署
本项目包含用于标准化部署的 Dockerfile：

    docker build -t yacht-digital-twin .
    docker run -p 5001:5001 yacht-digital-twin
---
### 项目结构
    ├── data/                   # 数据集仓库
    ├── models/                 # 序列化机器学习模型 (.pkl)
    │   ├── best_yacht_model.pkl
    │   └── feature_scaler.pkl
    ├── src/                    # 预处理与训练核心逻辑
    │   ├── preprocess.py
    │   └── train.py
    ├── app.py                  # Flask Web 主程序
    ├── requirements.txt        # 依赖清单
    ├── Dockerfile              # Docker 容器配置文件
    ├── README.md               # 技术文档
    └── voyage_telemetry.jsonl  # 模拟 IoT 遥测数据日志 
---
### 许可证
本项目作为研究生级 AI 工程作品集的一部分，开发目的仅用于学术交流与研究。
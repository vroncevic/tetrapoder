# Tetrapoder — Kinematics Compiler, Gait Planner & Trajectory Streamer

**tetrapoder** is an autonomous kinematics compilation, gait trajectory planning, and binary streaming toolchain for 12-DOF quadruped (four-legged) robots.

Developed in **[python](https://www.python.org/)** code adhering to the ATS framework architecture and standards.

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)

---

## 📋 Table of Contents

- [🚀 Overview](#-overview)
- [📦 Installation & Dependencies](#-installation--dependencies)
- [🏗 Architecture & SOLID Principles](#-architecture--solid-principles)
- [📐 3-Link Inverse Kinematics (IK) Engine](#-3-link-inverse-kinematics-ik-engine)
- [🐾 Gait Planning & Trajectory Generation](#-gait-planning--trajectory-generation)
- [📡 Binary Protocol & Packet Serialization](#-binary-protocol--packet-serialization)
- [🛠 CLI Usage](#-cli-usage)
- [🧪 Testing & Quality Gates](#-testing--quality-gates)

---

## 🚀 Overview

Microcontrollers without hardware floating-point units (such as Atmel AVR ATmega328P/ATmega2560) face severe timing constraints when calculating trigonometric inverse kinematics, bezier splines, and gait state machines in real time.

**tetrapoder** offloads all heavy analytical 3D kinematics, gait scheduling, and trajectory interpolation to the host computer:
1. **Host-Side Computation**: Computes exact joint angles $(\theta_{\text{coxa}}, \theta_{\text{femur}}, \theta_{\text{tibia}})$ in floating-point degrees, then encodes them into fixed-point tenths-of-a-degree integers (`int16_t`).
2. **Binary Frame Compilation**: Packages trajectories into compact, CRC8-protected binary command packets (`.bin`).
3. **Hardware Dispatch**: Streams compiled motion plans or direct commands over UART/USB-Serial to the robot firmware.

```
+-------------------------------------------------------------------------+
|                              HOST COMPUTER                              |
|                                                                         |
|  [ Gait Planner ] ──> [ Trajectory Builder ] ──> [ Kinematics Solver ]  |
|                                                          │              |
|                                                          ▼              |
|  [ Serial Transport ] <── [ Motion Runner ] <── [ Motion Compiler ]     |
+───────────────────────────────────┬─────────────────────────────────────+
                                    │ UART / USB-Serial (115200 8N1)
                                    ▼
+-------------------------------------------------------------------------+
|                         AVR ROBOT CONTROLLER                            |
|                                                                         |
|  [ UART RX ] ──> [ Frame Parser ] ──> [ Ring Buffer ] ──> [ Servos ]    |
+-------------------------------------------------------------------------+
```

---

## 📦 Installation & Dependencies

### Prerequisites
- Python 3.12 or newer
- `ats_utilities` (core ATS framework)
- `pyserial` (serial hardware communication)

### Local Development Setup
```bash
# Clone the repository
git clone git@github.com:vroncevic/tetrapoder.git
cd tetrapoder

# Initialize and update submodules (gates, coverage)
git submodule update --init --recursive

# Install Python requirements
pip install -r requirements.txt
```

---

## 🏗 Architecture & SOLID Principles

`tetrapoder` follows Clean / Hexagonal Architecture:
- `core/model/`: Pure domain entities (`FootPosition`, `LegAngles`, `PlanCommand`, `MotionPlan`) and domain exceptions. Completely free of framework or I/O dependencies.
- `core/service/`: Driving and driven port interfaces (`@runtime_checkable Protocol`) and pure algorithmic domain services (`KinematicsSolver`, `GaitPlanBuilder`, `TrajectoryBuilder`, `ProtocolFrameBuilder`, `MotionCompiler`, `MotionRunner`, `CRC8`).
- `infrastructure/`: Concrete adapters implementing service ports:
  - `transport/serial_transport.py`: Hardware UART/Serial adapter.
  - `cli/`: Command-line interface parser and engine.
  - `command/`: Action definitions and execution coordinator.
- `setup/`: ATS bundle configuration, dependency injection registries, and validation pipelines.

### Architectural Rules
- Maximum 6 methods per class (including `__init__`, properties, and dunders).
- Strictly zero private methods (`def _...`); capabilities are composed and delegated via public contracts.
- Strictly zero `typing.Any` across the entire codebase.
- One class or interface per module.
- 100% decoupling: concrete implementations do not inherit from `Protocol` interfaces.

---

## 📐 3-Link Inverse Kinematics (IK) Engine

Each of the 4 robot legs consists of 3 links:
- **Coxa** ($L_1 = 30.0\,\text{mm}$): Horizontal yaw rotation in the X-Y plane ($\theta_{\text{coxa}}$).
- **Femur** ($L_2 = 50.0\,\text{mm}$): Vertical pitch rotation in the limb plane ($\theta_{\text{femur}}$).
- **Tibia** ($L_3 = 60.0\,\text{mm}$): Vertical knee flexion/extension in the limb plane ($\theta_{\text{tibia}}$).

### Analytical Closed-Form Solution
Given target foot Cartesian coordinates $(x, y, z)$ relative to the leg base:
1. **Coxa Angle**:
   $$\theta_{\text{coxa}} = \operatorname{atan2}(y, x)$$
2. **Effective Limb-Plane Coordinate**:
   $$r_{\text{proj}} = \sqrt{x^2 + y^2} - L_1, \quad d = \sqrt{r_{\text{proj}}^2 + z^2}$$
3. **Femur & Tibia Angles** (Law of Cosines):
   $$\cos(\alpha) = \frac{L_2^2 + d^2 - L_3^2}{2 L_2 d}, \quad \theta_{\text{femur}} = \operatorname{atan2}(z, r_{\text{proj}}) + \alpha$$
   $$\cos(\beta) = \frac{L_2^2 + L_3^2 - d^2}{2 L_2 L_3}, \quad \theta_{\text{tibia}} = \beta$$

The solver verifies reachability ($|L_2 - L_3| \le d \le L_2 + L_3$) and maps joint angles to servo home references ($90^\circ$).

---

## 🐾 Gait Planning & Trajectory Generation

`tetrapoder` supports multiple locomotion modes and poses:
- **Stand**: Neutral stance with all four feet firmly on the ground.
- **Sit**: Low posture with retracted rear limbs.
- **Dance**: Wave and alternating pitch/roll movements.
- **Crawl Gait**: 4-phase wave gait where only one leg swings at any given time while the other three maintain a stable tripod base.
- **Trot Gait**: 2-phase dynamic gait swinging diagonal leg pairs simultaneously (LF+RR, then RF+LR).

Swing trajectories utilize parametric cubic Bézier curves for smooth foot lift-off, peak clearance, and ground touchdown, eliminating mechanical impact shock.

---

## 📡 Binary Protocol & Packet Serialization

All communication between `tetrapoder` and the robot controller uses compact binary frames protected by CRC8-CCITT ($x^8 + x^2 + x + 1$, polynomial `0x07`):

```
+------------+------------+------------+--------------------+------------+
| Header     | Command ID | Length     | Payload            | CRC8       |
| 1 byte     | 1 byte     | 1 byte     | N bytes            | 1 byte     |
| 0xAA       | uint8_t    | uint8_t    | (varies by cmd)    | uint8_t    |
+------------+------------+------------+--------------------+------------+
```

### Commands
| ID | Name | Description |
|:---|:---|:---|
| `0x01` | `CMD_PING` | Ping controller (heartbeat) |
| `0x02` | `CMD_STOP` | Emergency stop / disable servos |
| `0x03` | `CMD_SET_SERVO` | Direct single-servo position command |
| `0x04` | `CMD_SET_LEG` | Direct 3-angle command for one leg |
| `0x05` | `CMD_SET_ALL_LEGS`| Direct 12-angle command for all four legs |
| `0x10` | `CMD_EXEC_PLAN` | Select and execute precompiled firmware gait |
| `0x11` | `CMD_APPEND_KEYFRAME` | Append 12-angle keyframe to ring buffer |
| `0x12` | `CMD_CLEAR_BUFFER` | Flush command execution queue |

---

## 🛠 CLI Usage

The tool is invoked via `run.sh` or the installed `tetrapoder` CLI executable.

```bash
# Display help and usage
./run.sh robot --help

# Ping the robot controller
./run.sh robot --action ping --port /dev/ttyUSB0 --baudrate 115200

# Emergency stop
./run.sh robot --action stop --port /dev/ttyUSB0

# Compile a gait plan into a binary file
./run.sh robot --action compile --gait crawl --output motion_crawl.bin

# Compile and immediately upload/stream to the robot
./run.sh robot --action upload --gait crawl --port /dev/ttyUSB0

# Direct command: set all 4 legs to 90 degrees with 200 ms transition
./run.sh robot --action direct --angles 90,90,90,90,90,90,90,90,90,90,90,90 --time 200 --port /dev/ttyUSB0
```

---

## 🧪 Testing & Quality Gates

### Running Unit Tests
Unit tests strictly use standard Python `unittest` (69 test suites mirroring production modules 1:1):
```bash
python3 -m unittest discover -s tests -p "*_test.py"
```

### Quality Gates Execution
All four automated AST gate checks verify code compliance:
```bash
./run_quality_gates.sh
```
- `interfaces_checker.py`: Protocol adherence and method matching.
- `isp_checker.py`: Interface segregation principle ($\le 9$ methods per protocol).
- `limits_checker.py`: Line length ($\le 150$) and module line count ($\le 500$).
- `srp_checker.py`: Single responsibility principle ($\le 6$ methods per class).

### Code Coverage & Pylint
```bash
# Code Coverage (>= 85% requirement)
./run_coverage.sh

# Static Analysis (10.00 / 10.00 score)
pylint tetrapoder tests main.py setup.py
```

---

## 📄 License
This project is licensed under the terms of the GNU General Public License v3.0 (GPLv3).

# RESONANCE-1
## System Requirements — v0.1

## 1. Purpose

RESONANCE-1 is a programmable sensor-processing SoC designed
to acquire physical sensor data, process it using dedicated
digital hardware, and perform local machine-condition analysis.

The first application is vibration-based machine monitoring.

The system shall eventually operate on custom silicon and a
custom PCB.

---

## 2. Primary Use Case

The system monitors vibration from a small rotating machine.

It shall:

1. Acquire vibration samples.
2. Filter the samples.
3. Transform the signal into the frequency domain.
4. Extract meaningful features.
5. Compare the features against a baseline.
6. Generate an anomaly score.
7. Report the machine state.

Initial states:

- NORMAL
- ANOMALY

---

## 3. High-Level Signal Path

Physical vibration
        ↓
Sensor
        ↓
Analog front end
        ↓
ADC
        ↓
SPI
        ↓
RESONANCE-1 SoC
        ↓
Digital filtering
        ↓
FFT
        ↓
Feature extraction
        ↓
Anomaly detection
        ↓
RISC-V software
        ↓
UART / external interface

---

## 4. SoC Requirements

The SoC shall contain:

- RISC-V processor
- SRAM
- system interconnect
- SPI
- I2C
- UART
- GPIO
- timer
- watchdog
- interrupt controller
- DMA
- DSP accelerator

---

## 5. DSP Requirements

The initial DSP subsystem shall support:

- FIR filtering
- FFT
- RMS calculation
- peak detection
- basic statistical feature extraction

All DSP hardware shall use fixed-point arithmetic.

---

## 6. Processor

Initial processor target:

RV32-class RISC-V.

The processor shall be capable of:

- executing firmware from memory
- configuring peripherals
- configuring the DSP
- receiving interrupts
- reading DSP results
- communicating through UART

---

## 7. External Interfaces

Initial interfaces:

- UART
- SPI
- I2C
- GPIO

Additional interfaces may be added in later revisions.

---

## 8. Development Platforms

The system shall be developed in three stages:

1. Software reference model
2. FPGA implementation
3. ASIC implementation

The same functional architecture shall be maintained across
all three stages wherever practical.

---

## 9. ASIC Goal

The final digital design shall be suitable for implementation
using an open-source ASIC flow and an open PDK.

The exact fabrication process and shuttle will be selected
after the RTL architecture is stable.

---

## 10. Engineering Goals

The project shall provide practical experience in:

- analog electronics
- digital electronics
- signals and systems
- DSP
- computer architecture
- embedded systems
- RTL design
- SystemVerilog
- verification
- computer architecture
- semiconductor/VLSI design
- physical design
- PCB design
- firmware
- hardware/software co-design
- silicon bring-up

---

## 11. Design Principle

The project shall prioritize understanding over feature count.

A smaller subsystem that is completely understood,
verified, synthesized and demonstrated is preferable to
a large system assembled from unexplained IP.# RESONANCE-1
## System Requirements — v0.1

## 1. Purpose

RESONANCE-1 is a programmable sensor-processing SoC designed
to acquire physical sensor data, process it using dedicated
digital hardware, and perform local machine-condition analysis.

The first application is vibration-based machine monitoring.

The system shall eventually operate on custom silicon and a
custom PCB.

---

## 2. Primary Use Case

The system monitors vibration from a small rotating machine.

It shall:

1. Acquire vibration samples.
2. Filter the samples.
3. Transform the signal into the frequency domain.
4. Extract meaningful features.
5. Compare the features against a baseline.
6. Generate an anomaly score.
7. Report the machine state.

Initial states:

- NORMAL
- ANOMALY

---

## 3. High-Level Signal Path

Physical vibration
        ↓
Sensor
        ↓
Analog front end
        ↓
ADC
        ↓
SPI
        ↓
RESONANCE-1 SoC
        ↓
Digital filtering
        ↓
FFT
        ↓
Feature extraction
        ↓
Anomaly detection
        ↓
RISC-V software
        ↓
UART / external interface

---

## 4. SoC Requirements

The SoC shall contain:

- RISC-V processor
- SRAM
- system interconnect
- SPI
- I2C
- UART
- GPIO
- timer
- watchdog
- interrupt controller
- DMA
- DSP accelerator

---

## 5. DSP Requirements

The initial DSP subsystem shall support:

- FIR filtering
- FFT
- RMS calculation
- peak detection
- basic statistical feature extraction

All DSP hardware shall use fixed-point arithmetic.

---

## 6. Processor

Initial processor target:

RV32-class RISC-V.

The processor shall be capable of:

- executing firmware from memory
- configuring peripherals
- configuring the DSP
- receiving interrupts
- reading DSP results
- communicating through UART

---

## 7. External Interfaces

Initial interfaces:

- UART
- SPI
- I2C
- GPIO

Additional interfaces may be added in later revisions.

---

## 8. Development Platforms

The system shall be developed in three stages:

1. Software reference model
2. FPGA implementation
3. ASIC implementation

The same functional architecture shall be maintained across
all three stages wherever practical.

---

## 9. ASIC Goal

The final digital design shall be suitable for implementation
using an open-source ASIC flow and an open PDK.

The exact fabrication process and shuttle will be selected
after the RTL architecture is stable.

---

## 10. Engineering Goals

The project shall provide practical experience in:

- analog electronics
- digital electronics
- signals and systems
- DSP
- computer architecture
- embedded systems
- RTL design
- SystemVerilog
- verification
- computer architecture
- semiconductor/VLSI design
- physical design
- PCB design
- firmware
- hardware/software co-design
- silicon bring-up

---

## 11. Design Principle

The project shall prioritize understanding over feature count.

A smaller subsystem that is completely understood,
verified, synthesized and demonstrated is preferable to
a large system assembled from unexplained IP.
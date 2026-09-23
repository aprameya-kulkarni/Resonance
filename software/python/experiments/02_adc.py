import sys
from pathlib import Path

# ROOT = Path(__file__).resolve().parents[3]
# sys.path.append(str(ROOT))

import numpy as np
import matplotlib.pyplot as plt

from software.python.references.adc import quantize


# Configuration
fs = 10000
duration = 0.01
bits = 12

t = np.arange(0, duration, 1/fs)

signal = 0.8 * np.sin(2 * np.pi * 500 * t)

codes, reconstructed = quantize(
    signal,
    bits=bits,
    vmin=-1.0,
    vmax=1.0
)


plt.figure()

plt.plot(
    t,
    signal,
    label="Original"
)

plt.step(
    t,
    reconstructed,
    where="mid",
    label="Quantized"
)

plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title(f"{bits}-bit ADC Quantization")
plt.legend()
plt.grid()

plt.show()


error = signal - reconstructed

print("Maximum error:", np.max(np.abs(error)))
print("RMS error:", np.sqrt(np.mean(error**2)))
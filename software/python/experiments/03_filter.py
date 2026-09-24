import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


def fir_filter(samples, coefficients):
    """
    Causal FIR filter.

    y[n] = sum(h[k] * x[n-k])
    """
    samples = np.asarray(samples)
    coefficients = np.asarray(coefficients)

    output = np.zeros_like(samples, dtype=float)

    for n in range(len(samples)):
        acc = 0.0

        for k in range(len(coefficients)):
            if n - k >= 0:
                acc += coefficients[k] * samples[n - k]

        output[n] = acc

    return output


fs = 10000
duration = 0.1

t = np.arange(0, duration, 1/fs)

# Useful machine vibration
useful = (
    np.sin(2 * np.pi * 500 * t)
    + 0.5 * np.sin(2 * np.pi * 1500 * t)
)

# High-frequency interference
interference = (
    0.8 * np.sin(2 * np.pi * 3500 * t)
    + 0.6 * np.sin(2 * np.pi * 4200 * t)
)

input_signal = useful + interference


# Analog anti-aliasing filter model
cutoff = 2000

b, a = signal.butter(
    4,
    cutoff / (fs / 2),
    btype="low"
)

filtered = signal.filtfilt(
    b,
    a,
    input_signal
)


coefficients = np.array([
    0.25,
    0.25,
    0.25,
    0.25
])

fir_output = fir_filter(
    filtered,
    coefficients
)

plt.figure()

plt.plot(
    t[:1000],
    input_signal[:1000],
    label="Before filter"
)

plt.plot(
    t[:1000],
    filtered[:1000],
    label="After filter"
)

plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()

plt.show()


plt.figure()

plt.plot(
    t[:1000],
    filtered[:1000],
    label="Before FIR"
)

plt.plot(
    t[:1000],
    fir_output[:1000],
    label="After FIR"
)

plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()

plt.show()
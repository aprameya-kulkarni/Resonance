import numpy as np
import matplotlib.pyplot as plt

# Sampling configuration
fs = 2000          # samples per second
duration = 1.0      # seconds

# Time axis
t = np.arange(0, duration, 1/fs)

# Machine vibration components
f1 = 500
f2 = 1800

signal = (
    1.0 * np.sin(2 * np.pi * f1 * t)
    + 0.4 * np.sin(2 * np.pi * f2 * t)
)

# Add measurement noise
noise = 0.1 * np.random.randn(len(t))

vibration = signal + noise

plt.figure()
plt.plot(t[:1000], vibration[:1000])
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Simulated Machine Vibration")
plt.grid()
plt.show()

# FFT
N = len(vibration)

spectrum = np.fft.rfft(vibration)
frequencies = np.fft.rfftfreq(N, 1/fs)

magnitude = np.abs(spectrum) / N

plt.figure()
plt.plot(frequencies, magnitude)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title("Vibration Spectrum")
plt.xlim(0, 3000)
plt.grid()
plt.show()
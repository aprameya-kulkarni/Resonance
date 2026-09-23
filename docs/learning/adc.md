# ADC — Analog-to-Digital Conversion

## 1. Purpose

An **Analog-to-Digital Converter (ADC)** converts a continuous-time, continuous-amplitude analog signal into a digital representation that a processor, FPGA, DSP, or software system can process.

An ADC performs two fundamentally different operations:

1. **Sampling** — discretizes time.
2. **Quantization** — discretizes amplitude.

A useful conceptual chain is:

```text
Analog signal x(t)
       │
       ▼
Anti-aliasing filter
       │
       ▼
ADC sampling
       │
       ▼
Quantization
       │
       ▼
Digital sequence x[n]
       │
       ▼
Digital processing
```

The distinction between sampling and quantization is fundamental:

```text
Sampling:
continuous time  → discrete time

Quantization:
continuous amplitude → discrete amplitude
```

Therefore:

```text
x(t)  →  x[n]
```

is not a single physical operation. It represents the combined effect of sampling and quantization.

---

# 2. Analog and Digital Signals

## 2.1 Continuous-time signal

An analog signal can be represented as:

$$
x(t)
$$

where `t` can take any value in time.

For example:

$$
x(t)=A\cos(2\pi f_0t+\phi)
$$

where:

- $A$ = amplitude
- $f_0$ = frequency
- $\phi$ = phase
- $t$ = continuous time

The signal exists at every instant.

---

## 2.2 Discrete-time signal

After sampling at sampling frequency $f_s$, the signal becomes:

$$
x[n]=x(nT_s)
$$

where:

$$
T_s=\frac{1}{f_s}
$$

is the sampling period.

The index `n` is an integer:

$$
n=0,\pm1,\pm2,\ldots
$$

The signal is now defined only at discrete time instants.

---

# 3. Sampling

## 3.1 Definition

Sampling means measuring the amplitude of a continuous-time signal at regularly spaced time instants.

If:

$$
f_s = \frac{1}{T_s}
$$

then samples occur at:

$$
t=nT_s
$$

and:

$$
x[n]=x(nT_s)
$$

---

## 3.2 Sampling frequency

The **sampling frequency** or **sampling rate** is the number of samples acquired per second.

It is measured in:

- Hz
- samples/second
- kS/s
- MS/s
- GS/s

For example:

```text
48 kHz = 48,000 samples/second
```

---

# 4. Nyquist-Shannon Sampling Theorem

If a continuous-time signal is band-limited to a maximum frequency $f_{max}$, perfect reconstruction is theoretically possible when:

$$
f_s > 2f_{max}
$$

The quantity:

$$
\frac{f_s}{2}
$$

is called the **Nyquist frequency**.

Therefore:

$$
f_N=\frac{f_s}{2}
$$

The theorem assumes the signal contains no frequency components at or above the relevant Nyquist limit and that ideal sampling/reconstruction conditions are satisfied.

---

## 4.1 Example

Suppose:

$$
f_{max}=20\,kHz
$$

Then the theoretical minimum sampling rate is:

$$
f_s > 40\,kHz
$$

A practical system might use:

```text
44.1 kHz
48 kHz
96 kHz
```

rather than operating exactly at the theoretical boundary.

---

# 5. Why Sampling Rate Alone Is Not Enough

A common misconception is:

> "If the ADC has a sampling rate greater than twice my signal frequency, aliasing cannot happen."

This is incomplete.

Real signals are not perfectly band-limited, and real filters are not ideal.

For example, if:

```text
Desired signal bandwidth = 20 kHz
Sampling rate            = 48 kHz
Nyquist frequency        = 24 kHz
```

there is only:

```text
20 kHz → 24 kHz
```

of transition space.

A real anti-aliasing filter must attenuate unwanted energy sufficiently before it reaches the ADC.

Therefore, ADC sampling and analog filtering must be considered together.

---

# 6. Sampling in the Frequency Domain

Sampling produces spectral repetitions.

If the original spectrum is:

$$
X(f)
$$

sampling at $f_s$ produces repeated copies approximately centered at:

$$
k f_s
$$

where:

$$
k=0,\pm1,\pm2,\ldots
$$

Conceptually:

```text
             copies of spectrum
                  ↓
----|-------------|-------------|----
   -fs             0            +fs
```

More precisely, the sampled spectrum can be expressed as:

$$
X_s(f)=\frac{1}{T_s}\sum_{k=-\infty}^{\infty}X(f-kf_s)
$$

If these spectral copies overlap, aliasing occurs.

---

# 7. Aliasing

## 7.1 Definition

**Aliasing** occurs when different continuous-time frequencies produce the same sampled sequence.

A frequency above the Nyquist frequency can appear as a lower frequency after sampling.

This is a fundamental consequence of sampling.

---

## 7.2 Example

Suppose:

$$
f_s=10\,kHz
$$

Then:

$$
f_N=5\,kHz
$$

Consider an input tone at:

$$
f_{in}=7\,kHz
$$

The sampled signal can appear at:

$$
f_{alias}=|f_{in}-kf_s|
$$

Choose:

$$
k=1
$$

Then:

$$
f_{alias}=|7-10|=3\,kHz
$$

Therefore:

```text
Original analog tone = 7 kHz
Sampling frequency   = 10 kHz
Observed digital tone = 3 kHz
```

The ADC cannot determine from the samples alone that the original analog tone was 7 kHz rather than 3 kHz.

---

# 8. Sampling of a Sinusoid

For:

$$
x(t)=A\cos(2\pi f_0t+\phi)
$$

sampling gives:

$$
x[n]=A\cos(2\pi f_0nT_s+\phi)
$$

Since:

$$
T_s=\frac{1}{f_s}
$$

we get:

$$
x[n]=A\cos\left(2\pi\frac{f_0}{f_s}n+\phi\right)
$$

The discrete-time frequency is periodic modulo $f_s$.

This is the mathematical reason frequencies separated by integer multiples of $f_s$ become indistinguishable after sampling.

---

# 9. Quantization

Sampling discretizes **time**.

Quantization discretizes **amplitude**.

An ideal N-bit ADC has:

$$
L=2^N
$$

possible quantization codes.

Examples:

| ADC resolution | Number of codes |
|---:|---:|
| 8 bit | 256 |
| 10 bit | 1024 |
| 12 bit | 4096 |
| 14 bit | 16384 |
| 16 bit | 65536 |
| 24 bit | 16777216 |

Increasing resolution increases the number of available amplitude levels.

---

# 10. ADC Resolution

The **resolution** is the number of bits used to represent each sample.

For an N-bit ADC:

$$
L=2^N
$$

where `L` is the number of quantization levels.

Resolution is often informally described as the ADC's ability to distinguish small voltage changes.

However, resolution alone does **not** fully describe ADC quality.

A 16-bit ADC can have worse real-world performance than another 16-bit ADC because of:

- noise
- distortion
- nonlinearity
- reference instability
- clock jitter
- thermal effects
- power-supply coupling
- layout
- front-end limitations

---

# 11. Quantization Step / LSB Size

For an ADC with input range:

$$
V_{min}\leq V_{in}\leq V_{max}
$$

the total input span is:

$$
V_{FS}=V_{max}-V_{min}
$$

For an ideal N-bit ADC, the nominal quantization step is approximately:

$$
\Delta=\frac{V_{FS}}{2^N}
$$

This is commonly called **1 LSB**.

---

## 11.1 Example

For a 12-bit ADC with a 0–3.3 V input range:

$$
N=12
$$

$$
2^{12}=4096
$$

Therefore:

$$
\Delta=\frac{3.3}{4096}
$$

Approximately:

```text
0.806 mV per LSB
```

The exact code-to-voltage interpretation depends on the ADC's transfer-function convention, including whether the endpoints are represented as code centers or boundaries.

---

# 12. ADC Input Range

Common ADC ranges include:

```text
0 V to Vref
-Vref to +Vref
0 V to VDD
Differential ranges
Bipolar ranges
```

The input range must match the ADC architecture and input specification.

For a unipolar ADC:

```text
minimum input → lowest code
maximum valid input → highest code
```

For a bipolar ADC:

```text
negative input → negative-side codes
zero           → mid-scale or equivalent representation
positive input → positive-side codes
```

The exact transfer function depends on the ADC.

---

# 13. Quantization Process

Suppose an analog value lies between two quantization levels.

The ADC maps it to a digital code.

Conceptually:

```text
Analog amplitude
      │
      ▼
 ┌─────────────┐
 │ Quantizer   │
 └─────────────┘
      │
      ▼
Discrete code
```

The quantizer introduces a difference between the original value and the quantized value.

This difference is the **quantization error**.

---

# 14. Quantization Error

Define:

$$
e_q[n]=x[n]-x_q[n]
$$

where:

- $x[n]$ = sampled value before quantization
- $x_q[n]$ = quantized value
- $e_q[n]$ = quantization error

For an ideal uniform quantizer, the error is commonly modeled as:

$$
-\frac{\Delta}{2}\leq e_q[n]\leq\frac{\Delta}{2}
$$

assuming appropriate conditions.

The maximum magnitude of the quantization error is therefore:

$$
|e_q|_{max}=\frac{\Delta}{2}
$$

---

# 15. Quantization Noise Model

For an ideal ADC with a sufficiently varying input, quantization error can often be approximated as uniformly distributed.

Under the standard quantization-noise model:

$$
\sigma_q^2=\frac{\Delta^2}{12}
$$

Therefore:

$$
\sigma_q=\frac{\Delta}{\sqrt{12}}
$$

This model is an approximation, not a universal physical law.

It becomes less accurate for certain deterministic inputs, especially very small or periodic signals that interact with the quantizer in a correlated way.

---

# 16. Quantization Noise and Number of Bits

Since:

$$
\Delta\propto\frac{1}{2^N}
$$

increasing ADC resolution reduces quantization step size.

Each additional bit ideally:

```text
doubles the number of levels
halves the LSB size
reduces ideal quantization noise by about 6 dB
```

This leads to the well-known ideal ADC SNR relationship.

---

# 17. Ideal ADC SNR

For an ideal N-bit ADC with a full-scale sine-wave input:

$$
SNR_{ideal}\approx6.02N+1.76\,dB
$$

Examples:

| Resolution | Ideal SNR |
|---:|---:|
| 8 bit | 49.9 dB |
| 10 bit | 61.96 dB |
| 12 bit | 74.0 dB |
| 14 bit | 86.0 dB |
| 16 bit | 98.1 dB |
| 18 bit | 110.1 dB |
| 24 bit | 146.2 dB |

These values describe an **ideal quantization-limited ADC** under the standard full-scale sine-wave assumption.

A real ADC normally achieves less.

---

# 18. Why 1.76 dB Appears

The:

$$
6.02N
$$

term comes from the exponential relationship between the number of quantization levels and ADC resolution.

The:

$$
1.76\,dB
$$

term comes from comparing the RMS value of a full-scale sinusoid with the RMS quantization noise for the ideal uniform quantizer model.

The result is:

$$
SNR=20\log_{10}\left(\frac{V_{signal,rms}}{V_{noise,rms}}\right)
$$

which produces:

$$
SNR\approx6.02N+1.76\,dB
$$

---

# 19. Dynamic Range

**Dynamic range** describes the ratio between the largest usable signal and the smallest usable signal/noise floor.

A generic voltage ratio is expressed as:

$$
DR=20\log_{10}\left(\frac{V_{max}}{V_{min}}\right)
$$

The exact definition depends on what is being considered the minimum usable signal.

For an ideal N-bit ADC, the theoretical dynamic range is closely related to quantization-limited SNR.

However, real ADC datasheets may define dynamic range differently from SNR.

Always check the manufacturer's definition.

---

# 20. SNR

**Signal-to-Noise Ratio (SNR)** is:

$$
SNR=10\log_{10}\left(\frac{P_{signal}}{P_{noise}}\right)
$$

For voltage quantities across the same impedance:

$$
SNR=20\log_{10}\left(\frac{V_{signal,rms}}{V_{noise,rms}}\right)
$$

Higher SNR generally means the desired signal is larger relative to the noise floor.

---

# 21. SNR vs Dynamic Range

These terms are related but should not automatically be treated as identical.

### SNR

Usually describes:

```text
signal power / noise power
```

under a specified measurement condition.

### Dynamic range

Often describes:

```text
largest usable signal / smallest usable signal
```

with the exact definition varying by specification.

Some ADC datasheets use terms such as:

- SNR
- SINAD
- dynamic range
- signal-to-noise-and-distortion ratio
- spurious-free dynamic range

These are not interchangeable.

---

# 22. Noise Sources in a Real ADC

Real ADC performance is affected by many noise sources:

- quantization noise
- thermal noise
- reference-voltage noise
- clock/jitter-related effects
- input-driver noise
- power-supply noise
- substrate coupling
- digital switching noise
- amplifier noise
- resistor noise
- PCB coupling
- electromagnetic interference

Therefore:

$$
SNR_{real}<SNR_{ideal}
$$

in typical practical systems.

---

# 23. ENOB — Effective Number of Bits

**Effective Number of Bits (ENOB)** describes the effective resolution of a real ADC based on measured dynamic performance.

A common relationship using SINAD is:

$$
ENOB=\frac{SINAD-1.76}{6.02}
$$

where SINAD is expressed in dB.

For example, if:

$$
SINAD=62\,dB
$$

then:

$$
ENOB\approx\frac{62-1.76}{6.02}
$$

which is approximately:

```text
10.0 effective bits
```

A nominal 12-bit ADC can therefore have an ENOB significantly below 12 bits.

---

# 24. SNR vs SINAD

### SNR

Considers noise relative to signal, under the measurement definition being used.

### SINAD

**Signal-to-Noise and Distortion Ratio** includes both:

```text
noise + distortion
```

in the denominator.

Therefore:

$$
SINAD\leq SNR
$$

for the same measurement conditions.

ENOB is commonly derived from SINAD rather than SNR.

---

# 25. ADC Transfer Characteristic

An ideal ADC has a staircase-like transfer characteristic.

Conceptually:

```text
Digital code
    │
111 │             ┌────
110 │         ┌───┘
101 │     ┌───┘
100 │ ┌───┘
    └──────────────────► Vin
```

Each input-voltage interval maps to one digital code.

---

# 26. Offset Error

**Offset error** describes a shift of the ADC transfer characteristic from its ideal position.

Conceptually:

```text
Ideal transfer
      /
     /
    /

Actual transfer
       /
      /
     /
```

Offset error primarily affects where the conversion starts relative to the ideal transfer characteristic.

---

# 27. Gain Error

**Gain error** describes a difference in the slope/span of the transfer characteristic after accounting for offset.

It causes the ADC's full-scale response to differ from the ideal response.

---

# 28. INL and DNL

## 28.1 DNL — Differential Nonlinearity

DNL describes how much an individual code width differs from the ideal 1-LSB width.

Ideally:

$$
DNL=0\,LSB
$$

for every code transition.

Large DNL can produce missing codes.

---

## 28.2 INL — Integral Nonlinearity

INL describes deviation of the actual transfer characteristic from an ideal reference line after the specified offset/gain treatment.

INL is normally specified in:

```text
LSB
```

Both INL and DNL are important when evaluating ADC linearity.

---

# 29. Reference Voltage

Many ADCs use a reference voltage, commonly written as:

$$
V_{REF}
$$

The reference establishes the conversion scale.

For a simple unipolar ADC, the input range may approximately correspond to:

$$
0\rightarrow V_{REF}
$$

However, the exact relationship depends on the ADC architecture.

Reference quality matters because reference noise and instability directly affect conversion accuracy.

---

# 30. Sampling Clock and Jitter

Sampling is controlled by a clock.

Real clocks have timing uncertainty called **jitter**.

For a sinusoidal input, sampling-time uncertainty becomes increasingly problematic as input frequency increases.

A commonly used approximate jitter-limited SNR relationship is:

$$
SNR_{jitter}\approx-20\log_{10}(2\pi f_{in}\sigma_t)
$$

where:

- $f_{in}$ = input frequency
- $\sigma_t$ = RMS sampling-clock jitter

This shows why high-frequency ADC systems require very low-jitter clocks.

---

# 31. ADC Architecture

Common ADC architectures include:

### Flash ADC

- Very high speed
- Many comparators
- High power and area
- Common for very high-speed conversion

### SAR ADC

**Successive Approximation Register ADC**

- Good balance of speed, resolution, power
- Very common in embedded systems
- Uses a successive-approximation process

### Pipeline ADC

- High throughput
- Suitable for high-speed applications
- Uses multiple conversion stages

### Sigma-Delta ADC

- Very high resolution
- Oversampling
- Noise shaping
- Often used for precision and relatively lower-bandwidth applications

### Dual-slope / integrating ADC

- High accuracy
- Good noise rejection
- Common in measurement instruments
- Relatively slow

The ADC architecture is a design choice based on:

```text
speed
resolution
power
latency
bandwidth
accuracy
area
cost
```

---

# 32. Oversampling

Oversampling means sampling significantly faster than the minimum required rate.

If the signal bandwidth is:

$$
B
$$

then an oversampling ratio can be defined as:

$$
OSR=\frac{f_s}{2B}
$$

for a low-pass signal whose highest useful frequency is approximately $B$.

Oversampling can:

- provide more transition bandwidth for the analog anti-aliasing filter
- spread quantization noise over a larger Nyquist bandwidth
- enable digital filtering and decimation
- improve achievable in-band SNR under appropriate conditions

Oversampling does **not** automatically eliminate aliasing.

---

# 33. ADC and Digital Signal Processing

A practical acquisition system may look like:

```text
Physical signal
      │
      ▼
Sensor / analog source
      │
      ▼
Analog conditioning
      │
      ▼
Anti-aliasing filter
      │
      ▼
ADC
      │
      ▼
Digital samples
      │
      ▼
Digital filter
      │
      ▼
DSP / FPGA / CPU
```

The analog filter protects the sampling process.

The digital filter operates after the signal has already been sampled.

This distinction is critical.

---

# 34. Important Distinction: Analog Filter vs Digital Filter

An analog anti-aliasing filter can remove unwanted analog frequency content **before sampling**.

A digital filter cannot undo aliasing that has already occurred.

Once two analog frequencies have mapped to the same sampled frequency, the original frequency information is lost.

Therefore:

```text
Filter before ADC → can prevent aliasing

Filter after ADC  → cannot recover already-aliased information
```

---

# 35. Practical ADC Design Checklist

When evaluating an ADC, consider:

### Sampling

- Sampling rate
- Nyquist frequency
- Input bandwidth
- Clock jitter

### Resolution

- Number of bits
- LSB size
- Effective number of bits

### Accuracy

- Offset error
- Gain error
- INL
- DNL
- Missing codes

### Noise

- SNR
- Noise density
- Reference noise
- Input-driver noise

### Distortion

- THD
- SINAD
- SFDR

### Analog interface

- Input impedance
- Input common-mode range
- Differential/single-ended input
- Input settling requirements
- Drive amplifier requirements

### Reference

- Reference voltage
- Reference accuracy
- Reference noise
- Reference stability

### Timing

- Sampling clock
- Aperture uncertainty
- Jitter

### System

- Power consumption
- Interface
- Latency
- Throughput
- Temperature range

---

# 36. Key Equations

### Sampling period

$$
T_s=\frac{1}{f_s}
$$

### Nyquist frequency

$$
f_N=\frac{f_s}{2}
$$

### Number of ADC codes

$$
L=2^N
$$

### Approximate LSB size

$$
\Delta=\frac{V_{FS}}{2^N}
$$

### Maximum ideal quantization error

$$
|e_q|_{max}=\frac{\Delta}{2}
$$

### Quantization noise variance

$$
\sigma_q^2=\frac{\Delta^2}{12}
$$

### Ideal ADC SNR

$$
SNR_{ideal}\approx6.02N+1.76\,dB
$$

### ENOB

$$
ENOB=\frac{SINAD-1.76}{6.02}
$$

### Voltage-form SNR

$$
SNR=20\log_{10}\left(\frac{V_{signal,rms}}{V_{noise,rms}}\right)
$$

### Power-form SNR

$$
SNR=10\log_{10}\left(\frac{P_{signal}}{P_{noise}}\right)
$$

### Alias frequency

A useful way to find an alias is:

$$
f_{alias}=|f_{in}-kf_s|
$$

where `k` is chosen so that the resulting frequency lies in the relevant Nyquist interval.

---

# 37. Worked Example

Consider:

```text
ADC resolution = 12 bits
Sampling rate  = 48 kS/s
Input range    = 0 to 3.3 V
```

## Step 1 — Number of codes

$$
2^{12}=4096
$$

## Step 2 — Nyquist frequency

$$
f_N=\frac{48\,kHz}{2}=24\,kHz
$$

## Step 3 — LSB size

$$
\Delta=\frac{3.3}{4096}
$$

Approximately:

```text
0.806 mV
```

## Step 4 — Ideal SNR

$$
SNR\approx6.02(12)+1.76
$$

Approximately:

```text
74 dB
```

This is an ideal theoretical result, not a guarantee of real ADC performance.

---

# 38. What an ADC Does Not Do

An ADC does not:

- automatically remove noise
- automatically remove aliasing
- preserve all analog information
- provide exactly N effective bits in practice
- eliminate the need for analog signal conditioning
- reconstruct the original signal by itself

The ADC is one part of a larger acquisition chain.

---

# 39. Mental Model

Remember the following:

```text
SAMPLING
────────
Where did I measure the signal in time?

QUANTIZATION
────────────
To which amplitude level did I map the measurement?

RESOLUTION
──────────
How many amplitude levels are available?

LSB
───
How much input voltage corresponds to one code step?

QUANTIZATION ERROR
──────────────────
How far is the quantized value from the sampled value?

SNR
───
How large is the desired signal relative to noise?

DYNAMIC RANGE
─────────────
How large is the usable signal range relative to the smallest
usable level/noise floor under the specified definition?

ALIASING
────────
What happens when unwanted frequency content is sampled above
the usable Nyquist range?

ANTI-ALIASING FILTER
────────────────────
What analog filtering prevents that unwanted content from
reaching the ADC?
```

---

# 40. Summary

An ADC converts analog information into digital samples.

The fundamental sequence is:

```text
continuous time
      ↓
sampling
      ↓
discrete time
      ↓
quantization
      ↓
discrete amplitude
      ↓
digital representation
```

The most important relationships are:

$$
f_N=\frac{f_s}{2}
$$

$$
L=2^N
$$

$$
\Delta\approx\frac{V_{FS}}{2^N}
$$

$$
SNR_{ideal}\approx6.02N+1.76\,dB
$$

The key system-level lesson is:

> **Sampling determines which frequencies can be represented; quantization determines how finely amplitude can be represented.**

And because sampling can cause irreversible aliasing, the analog signal must be appropriately bandwidth-limited before conversion.

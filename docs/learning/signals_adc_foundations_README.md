# Signals & Systems / ADC Foundations

> A complete, structured set of notes for building intuition and technical depth in signals, sampling, ADCs, aliasing, and related ECE fundamentals.
>
> **Current scope:** Continuous-time signals → discrete-time signals → sampling → Nyquist theorem → spectral replicas → aliasing → anti-aliasing → quantization → ADC signal chain.

---

# Table of Contents

1. [1. Continuous-Time Signals](#1-continuous-time-signals)
2. [2. Discrete-Time Signals](#2-discrete-time-signals)
3. [3. Sampling](#3-sampling)
4. [4. Sampling Period and Sampling Frequency](#4-sampling-period-and-sampling-frequency)
5. [5. The Sampling Theorem](#5-the-sampling-theorem)
6. [6. Why the Factor of 2 Appears](#6-why-the-factor-of-2-appears)
7. [7. What Happens When the Sampling Condition Is Violated](#7-what-happens-when-the-sampling-condition-is-violated)
8. [8. Aliasing](#8-aliasing)
9. [9. Frequency Folding](#9-frequency-folding)
10. [10. Spectral Replication Caused by Sampling](#10-spectral-replication-caused-by-sampling)
11. [11. Anti-Aliasing Filters](#11-anti-aliasing-filters)
12. [12. Why Filtering Must Happen Before the ADC](#12-why-filtering-must-happen-before-the-adc)
13. [13. Why We Cannot Sample Infinitely Fast](#13-why-we-cannot-sample-infinitely-fast)
14. [14. Sampling vs Quantization vs Encoding](#14-sampling-vs-quantization-vs-encoding)
15. [15. The Real ADC Signal Chain](#15-the-real-adc-signal-chain)
16. [16. Worked Examples](#16-worked-examples)
17. [17. Important Equations](#17-important-equations)
18. [18. Common Misconceptions](#18-common-misconceptions)
19. [19. Engineering Perspective](#19-engineering-perspective)
20. [20. Knowledge Checklist](#20-knowledge-checklist)
21. [21. Next Topics](#21-next-topics)

---

# 1. Continuous-Time Signals

## 1.1 Definition

A continuous-time signal is represented as:

\[
x(t)
\]

where \(t\) is a continuous-valued time variable.

For every real-valued time \(t\), the signal can have a corresponding value.

Example:

\[
x(t)=\sin(2\pi f t)
\]

For a 1 kHz sinusoid:

\[
x(t)=\sin(2\pi(1000)t)
\]

The signal exists for all continuous values of \(t\).

Conceptually:

```text
Amplitude
   ^
   |
   |       / \       / \
   |      /   \     /   \
   |_____/     \___/     \____
   |
   +----------------------------> time
```

---

## 1.2 Physical meaning

Real-world quantities are often modeled as continuous-time signals:

- microphone voltage
- antenna voltage
- temperature sensor output
- photodiode current
- accelerometer output
- pressure sensor output
- ECG voltage
- RF waveform
- analog amplifier output

For example, a microphone converts acoustic pressure into an analog electrical signal:

```text
Sound
  ↓
Microphone
  ↓
Analog voltage x(t)
```

That voltage varies continuously with time.

---

# 2. Discrete-Time Signals

## 2.1 Definition

A discrete-time signal is represented as:

\[
x[n]
\]

where \(n\) is an integer index:

\[
n\in\mathbb{Z}
\]

Therefore:

\[
n=0,\pm1,\pm2,\ldots
\]

The signal exists only at discrete time indices.

Conceptually:

```text
Amplitude
   ^
   |
   |      •       •
   |   •     •       •
   | •
   +----------------------------> n
     0  1  2  3  4  5  6
```

---

## 2.2 Relationship between \(x(t)\) and \(x[n]\)

If a continuous-time signal is sampled every \(T_s\) seconds:

\[
\boxed{x[n]=x(nT_s)}
\]

where:

- \(x(t)\) = original continuous-time signal
- \(x[n]\) = sampled discrete-time sequence
- \(T_s\) = sampling period
- \(n\) = integer sample index

The corresponding sampling instants are:

\[
t=0,T_s,2T_s,3T_s,\ldots
\]

---

## 2.3 Example

Suppose:

\[
x(t)=\sin(2\pi 1000t)
\]

and:

\[
f_s=8000\text{ Hz}
\]

Then:

\[
T_s=\frac{1}{f_s}
=\frac{1}{8000}
=125\mu s
\]

Therefore:

\[
x[n]=x(nT_s)
\]

and:

\[
x[n]=\sin\left(2\pi1000nT_s\right)
\]

or:

\[
x[n]=\sin\left(2\pi\frac{1000}{8000}n\right)
\]

Thus:

\[
\boxed{x[n]=\sin\left(\frac{\pi}{4}n\right)}
\]

---

## 2.4 Critical distinction

Do **not** think of \(x[n]\) as merely a continuous waveform with dots drawn on it.

Mathematically:

### Continuous time

\[
x(t)
\]

has a value for every real-valued \(t\).

### Discrete time

\[
x[n]
\]

has values only for integer \(n\).

This distinction becomes fundamental when studying:

- DSP
- ADCs
- DACs
- digital filters
- Fourier transforms
- control systems
- communications
- embedded systems

---

# 3. Sampling

## 3.1 Definition

Sampling is the process of measuring a continuous-time signal at discrete time instants.

If:

\[
T_s=\frac{1}{f_s}
\]

then:

\[
\boxed{x[n]=x(nT_s)}
\]

The sampling operation changes the time representation:

```text
Continuous-time
      x(t)
        ↓
     Sampling
        ↓
Discrete-time
      x[n]
```

---

## 3.2 Sampling does not necessarily quantize amplitude

This distinction is extremely important.

Sampling makes **time discrete**.

It does not inherently make amplitude discrete.

For example, samples could be:

\[
x[0]=1.237\text{ V}
\]

\[
x[1]=1.491\text{ V}
\]

\[
x[2]=0.982\text{ V}
\]

These are discrete in time but can still have arbitrary real-valued amplitudes.

This is a **discrete-time, continuous-amplitude** representation.

---

# 4. Sampling Period and Sampling Frequency

The two most important quantities are:

## Sampling period

\[
\boxed{T_s=\frac{1}{f_s}}
\]

where \(T_s\) is measured in seconds.

## Sampling frequency

\[
\boxed{f_s=\frac{1}{T_s}}
\]

where \(f_s\) is measured in samples per second (often expressed as Hz or S/s).

Examples:

| Sampling rate | Sampling period |
|---:|---:|
| 1 kS/s | 1 ms |
| 10 kS/s | 100 µs |
| 100 kS/s | 10 µs |
| 1 MS/s | 1 µs |
| 100 MS/s | 10 ns |
| 1 GS/s | 1 ns |

---

# 5. The Sampling Theorem

The Nyquist-Shannon sampling theorem states, in its standard form:

> A band-limited continuous-time signal can be perfectly reconstructed from its uniformly spaced samples if the sampling frequency is greater than twice the highest frequency present in the signal.

Mathematically:

\[
\boxed{f_s>2f_{\max}}
\]

where:

- \(f_s\) = sampling frequency
- \(f_{\max}\) = highest frequency component of the signal

The quantity:

\[
\boxed{\frac{f_s}{2}}
\]

is called the **Nyquist frequency**.

---

## 5.1 Example

Suppose:

\[
f_{\max}=10\text{ kHz}
\]

Then the theoretical minimum sampling rate is:

\[
2f_{\max}=20\text{ kHz}
\]

So we require:

\[
\boxed{f_s>20\text{ kHz}}
\]

for the strict form of the condition.

In practical systems, the actual sampling rate is often chosen higher because real anti-aliasing filters have finite transition bands and are not ideal brick-wall filters.

---

# 6. Why the Factor of 2 Appears

The factor of 2 is not an arbitrary rule.

It comes from the behavior of the signal spectrum during sampling.

Suppose a signal is band-limited to:

\[
-f_{\max}\le f\le f_{\max}
\]

Its spectrum occupies:

```text
                  Spectrum
                    ^
                    |
              _____|_____
             /           \
------------/-------------\------------> f
         -fmax             fmax
```

Sampling produces copies of this spectrum centered at multiples of the sampling frequency:

\[
0,\pm f_s,\pm2f_s,\ldots
\]

Conceptually:

```text
          replica        original        replica

             /\             /\             /\
            /  \           /  \           /  \
-----------/----\---------/----\---------/----\--------> f
         -fs              0              fs
```

For the copies not to overlap:

\[
f_s-f_{\max}>f_{\max}
\]

Therefore:

\[
\boxed{f_s>2f_{\max}}
\]

The factor of 2 is therefore a **spectral separation requirement**.

---

# 7. What Happens When the Sampling Condition Is Violated?

Suppose:

\[
f_s<2f_{\max}
\]

Then the spectral replicas overlap.

Conceptually:

```text
               overlapping spectra

                    /\
              /\   /  \
             /  \ /    \
------------/----X------\------------> f
```

Once the spectra overlap, different original analog frequencies can produce the same sampled sequence.

This phenomenon is called:

\[
\boxed{\text{aliasing}}
\]

---

# 8. Aliasing

## 8.1 Definition

Aliasing occurs when different continuous-time frequency components become indistinguishable after sampling.

In practical terms:

> A frequency that is too high for the selected sampling rate appears as a different, lower frequency in the sampled data.

---

## 8.2 Simple example

Suppose:

\[
f_s=10\text{ kHz}
\]

Therefore:

\[
f_N=\frac{f_s}{2}=5\text{ kHz}
\]

Now consider an analog sinusoid at:

\[
f=8\text{ kHz}
\]

Since:

\[
8>5
\]

it is above the Nyquist frequency.

The sampled signal can appear as:

\[
f_{\text{alias}}=|8-10|
\]

\[
\boxed{f_{\text{alias}}=2\text{ kHz}}
\]

So:

\[
\boxed{8\text{ kHz}\rightarrow2\text{ kHz}}
\]

after sampling.

---

## 8.3 Why this is information loss

Suppose:

\[
f_s=10\text{ kHz}
\]

Then the following frequencies can produce the same apparent frequency:

\[
2\text{ kHz}
\]

\[
8\text{ kHz}
\]

\[
12\text{ kHz}
\]

\[
18\text{ kHz}
\]

etc., depending on the folding relation.

The sampled sequence alone cannot tell you which original analog frequency produced it.

Therefore:

\[
\boxed{\text{Aliasing is irreversible after sampling}}
\]

You cannot recover the original frequency merely by digitally filtering the sampled data.

---

# 9. Frequency Folding

Aliasing is often described as **frequency folding**.

The Nyquist frequency:

\[
f_N=\frac{f_s}{2}
\]

acts as the folding boundary.

For example, with:

\[
f_s=100\text{ MHz}
\]

we have:

\[
f_N=50\text{ MHz}
\]

A 70-MHz input aliases to:

\[
|70-100|=30\text{ MHz}
\]

So:

\[
\boxed{70\text{ MHz}\rightarrow30\text{ MHz}}
\]

A 90-MHz input aliases to:

\[
|90-100|=10\text{ MHz}
\]

So:

\[
\boxed{90\text{ MHz}\rightarrow10\text{ MHz}}
\]

---

## 9.1 General alias-frequency relationship

A sampled sinusoid with frequency \(f\) is indistinguishable from frequencies differing by integer multiples of \(f_s\):

\[
\boxed{f' = |f-kf_s|}
\]

where \(k\) is an integer selected so that the resulting frequency is represented in the principal Nyquist interval.

For a real-valued sinusoid, the unique observable frequency can be represented between:

\[
0\le f_{\text{alias}}\le\frac{f_s}{2}
\]

---

# 10. Spectral Replication Caused by Sampling

This is one of the most important conceptual points in DSP.

Sampling a signal causes its frequency-domain spectrum to repeat periodically.

Let:

\[
X(f)
\]

be the Fourier transform of \(x(t)\).

Ideal impulse sampling can be represented by a sampling impulse train:

\[
p(t)=\sum_{n=-\infty}^{\infty}\delta(t-nT_s)
\]

The sampled signal is:

\[
x_s(t)=x(t)p(t)
\]

Multiplication in the time domain corresponds to convolution in the frequency domain.

The Fourier transform of the impulse train is another impulse train:

\[
P(f)=f_s\sum_{k=-\infty}^{\infty}\delta(f-kf_s)
\]

Therefore:

\[
X_s(f)
=
X(f)*P(f)
\]

which produces:

\[
\boxed{
X_s(f)=f_s\sum_{k=-\infty}^{\infty}X(f-kf_s)
}
\]

This equation says:

> The original spectrum is replicated every \(f_s\) Hz.

---

## 10.1 Why aliasing occurs in the frequency domain

If:

\[
f_s>2f_{\max}
\]

the spectral replicas do not overlap.

If:

\[
f_s<2f_{\max}
\]

the replicas overlap.

That overlap is the frequency-domain explanation of aliasing.

---

# 11. Anti-Aliasing Filters

## 11.1 Why they are needed

Real analog signals rarely contain only the frequencies we care about.

A sensor or RF input can contain:

- desired signal
- harmonics
- interference
- noise
- switching artifacts
- RF leakage
- out-of-band energy

If frequencies above the ADC's usable Nyquist band are sampled, they can alias into the desired band.

Therefore, an analog filter is placed before the ADC.

---

## 11.2 Basic structure

```text
Analog signal
     │
     ▼
┌──────────────────┐
│ Analog anti-     │
│ aliasing filter  │
└──────────────────┘
     │
     ▼
┌──────────────────┐
│       ADC        │
└──────────────────┘
     │
     ▼
Digital samples
```

The filter is normally a low-pass filter for a baseband ADC application.

---

## 11.3 Example

Suppose:

\[
f_s=100\text{ MHz}
\]

Then:

\[
f_N=50\text{ MHz}
\]

Suppose the desired signal occupies:

\[
0-20\text{ MHz}
\]

but the analog input also contains:

\[
70\text{ MHz}
\]

Without filtering:

\[
70\text{ MHz}\rightarrow30\text{ MHz}
\]

because:

\[
|70-100|=30\text{ MHz}
\]

The 70-MHz interference has therefore entered the useful digital frequency range.

An anti-aliasing filter should strongly attenuate the 70-MHz component before it reaches the ADC.

---

# 12. Why Filtering Must Happen Before the ADC

This is a fundamental hardware principle.

Suppose the analog input contains:

- real 30-MHz signal
- unwanted 70-MHz signal

and:

\[
f_s=100\text{ MHz}
\]

The 70-MHz signal aliases to:

\[
30\text{ MHz}
\]

After sampling, the ADC output contains a 30-MHz component.

The digital system cannot determine whether that 30-MHz component came from:

- an actual 30-MHz analog signal, or
- a 70-MHz analog signal that aliased down.

Therefore:

\[
\boxed{\text{Anti-aliasing must occur before sampling}}
\]

Once aliasing occurs, the lost information cannot be reconstructed by ordinary digital filtering.

---

# 13. Why We Cannot Sample Infinitely Fast

Theoretically, increasing \(f_s\) makes the Nyquist frequency larger.

In real hardware, however, infinite sampling rate is impossible.

Several physical and engineering limitations exist.

---

## 13.1 ADC conversion speed

An ADC requires physical circuitry to acquire and convert each sample.

A real ADC might operate at:

- kS/s
- MS/s
- hundreds of MS/s
- GS/s

but never at an infinite rate.

---

## 13.2 Power consumption

Higher-speed analog and digital circuits generally require faster switching and greater bandwidth.

Higher performance can increase:

- dynamic power
- analog bias current
- clock power
- data-movement power
- thermal load

This matters especially in:

- mobile SoCs
- sensors
- battery-powered systems
- embedded devices

---

## 13.3 Data-rate explosion

Suppose an ADC has:

\[
16\text{ bits/sample}
\]

and samples at:

\[
100\text{ MS/s}
\]

The raw output rate is:

\[
16\times100\times10^6
\]

\[
=\boxed{1.6\text{ Gbit/s}}
\]

If the ADC operates at:

\[
1\text{ GS/s}
\]

then:

\[
16\times1\times10^9
\]

\[
=\boxed{16\text{ Gbit/s}}
\]

Higher sampling rate therefore increases:

- memory bandwidth requirements
- interconnect bandwidth
- DSP workload
- storage requirements
- power consumption

---

## 13.4 Analog bandwidth limitations

The ADC is not the only limitation.

The entire analog front end has finite bandwidth:

```text
Sensor
  ↓
Amplifier
  ↓
PCB/interconnect
  ↓
Filter
  ↓
ADC input
```

Every stage has physical bandwidth limitations.

---

## 13.5 Clock limitations

High-speed sampling requires a high-quality sampling clock.

Clock uncertainty becomes increasingly important at high input frequencies.

Later, this leads to **sampling-clock jitter** and its effect on SNR.

---

# 14. Sampling vs Quantization vs Encoding

These three concepts must be kept separate.

| Operation | What becomes discrete? | Main consequence |
|---|---|---|
| Sampling | Time | Possible aliasing |
| Quantization | Amplitude | Quantization error |
| Encoding | Digital representation | Binary output |

---

## 14.1 Sampling

Sampling converts:

\[
x(t)
\]

into:

\[
x[n]
\]

It discretizes time.

---

## 14.2 Quantization

Quantization maps continuous-valued sample amplitudes onto a finite set of allowed levels.

Example:

Suppose an ADC has only four levels:

```text
Level 3 ─────────
Level 2 ─────────
Level 1 ─────────
Level 0 ─────────
```

An input of:

\[
1.73\text{ V}
\]

may be represented by the nearest quantization level.

The difference between the original sample and its quantized representation is quantization error.

---

## 14.3 Encoding

The selected quantization level is represented as digital bits.

For example:

```text
Level 0 → 00
Level 1 → 01
Level 2 → 10
Level 3 → 11
```

Thus:

```text
Analog voltage
      ↓
Sampling
      ↓
Discrete-time samples
      ↓
Quantization
      ↓
Discrete amplitude levels
      ↓
Encoding
      ↓
Binary digital output
```

---

# 15. The Real ADC Signal Chain

A simplified practical ADC chain is:

```text
                  ANALOG DOMAIN

Physical source
      │
      ▼
Sensor / RF input
      │
      ▼
Analog front-end
      │
      ▼
Anti-aliasing filter
      │
      ▼
Sample-and-hold / track-and-hold
      │
      ▼
ADC conversion
      │
      ▼
Quantization
      │
      ▼
Digital encoding
      │
      ▼
                  DIGITAL DOMAIN
```

The exact implementation depends on the ADC architecture.

---

# 16. Worked Examples

## Example 1 — Determine minimum sampling rate

Signal bandwidth:

\[
f_{\max}=20\text{ kHz}
\]

Minimum theoretical sampling condition:

\[
f_s>2(20\text{ kHz})
\]

Therefore:

\[
\boxed{f_s>40\text{ kHz}}
\]

---

## Example 2 — Determine whether aliasing can occur

Given:

\[
f_s=50\text{ kHz}
\]

and:

\[
f_{\max}=20\text{ kHz}
\]

Nyquist frequency:

\[
f_N=25\text{ kHz}
\]

Since:

\[
20<25
\]

the signal is within the Nyquist band.

The theoretical sampling condition is satisfied:

\[
50>40
\]

---

## Example 3 — Aliasing

Given:

\[
f_s=50\text{ kHz}
\]

and input:

\[
f=35\text{ kHz}
\]

Nyquist frequency:

\[
25\text{ kHz}
\]

Since:

\[
35>25
\]

aliasing occurs.

Calculate:

\[
f_{\text{alias}}
=
|35-50|
\]

\[
\boxed{f_{\text{alias}}=15\text{ kHz}}
\]

---

## Example 4 — High-frequency interference

ADC:

\[
f_s=100\text{ MHz}
\]

Desired signal:

\[
0-20\text{ MHz}
\]

Interference:

\[
75\text{ MHz}
\]

Nyquist frequency:

\[
50\text{ MHz}
\]

The interference aliases to:

\[
|75-100|=25\text{ MHz}
\]

Therefore:

\[
\boxed{75\text{ MHz}\rightarrow25\text{ MHz}}
\]

Since 25 MHz is inside the digital Nyquist band, the interference can contaminate the digital signal.

An analog anti-aliasing filter must attenuate the 75-MHz component before sampling.

---

# 17. Important Equations

## Sampling period

\[
\boxed{T_s=\frac{1}{f_s}}
\]

## Sampling frequency

\[
\boxed{f_s=\frac{1}{T_s}}
\]

## Sampled sequence

\[
\boxed{x[n]=x(nT_s)}
\]

## Nyquist frequency

\[
\boxed{f_N=\frac{f_s}{2}}
\]

## Sampling theorem

\[
\boxed{f_s>2f_{\max}}
\]

## Alias-frequency relationship

\[
\boxed{f_{\text{alias}}=|f-kf_s|}
\]

with \(k\) chosen to map the frequency into the principal Nyquist interval.

## Spectral replicas

For ideal impulse sampling:

\[
\boxed{
X_s(f)=f_s\sum_{k=-\infty}^{\infty}X(f-kf_s)
}
\]

---

# 18. Common Misconceptions

## Misconception 1: "Nyquist means exactly twice the frequency."

Not quite.

For ideal reconstruction of a band-limited signal, the strict condition is:

\[
\boxed{f_s>2f_{\max}}
\]

Real systems generally require additional design margin.

---

## Misconception 2: "Sampling and quantization are the same."

They are not.

Sampling discretizes **time**.

Quantization discretizes **amplitude**.

---

## Misconception 3: "Aliasing is noise."

Not exactly.

Aliasing is a deterministic consequence of inadequate sampling/filtering in which frequency components are mapped to other frequencies.

It can look like an unwanted signal rather than random noise.

---

## Misconception 4: "We can remove aliasing with a digital filter."

Not after the alias has occurred.

The ADC has already converted the unwanted analog frequency into another digital frequency.

You cannot generally determine its original frequency afterward.

---

## Misconception 5: "The anti-aliasing filter removes everything above \(f_s/2\) perfectly."

Real filters are not ideal brick-wall filters.

They have:

- passband
- transition band
- stopband
- finite attenuation

Therefore, practical systems choose the sampling rate and filter characteristics together.

---

## Misconception 6: "Higher sampling rate always solves everything."

Higher \(f_s\) increases the Nyquist frequency, but it also introduces:

- higher ADC power
- higher data rates
- greater processing requirements
- more demanding clocking
- potentially more difficult analog design

Engineering is a trade-off.

---

## Misconception 7: "A continuous-time signal and an analog signal are exactly the same concept."

They are related but not identical concepts.

"Continuous-time" describes the time variable.

"Analog" commonly refers to continuous-valued physical signals.

A signal can be discussed mathematically in terms of continuous/discrete time and continuous/discrete amplitude separately.

---

# 19. Engineering Perspective

The most useful way to think about this material is as a boundary between the analog and digital worlds.

```text
             PHYSICAL / ANALOG WORLD
                      │
                      │ x(t)
                      ▼
             ┌─────────────────┐
             │ Analog filtering│
             └─────────────────┘
                      │
                      ▼
             ┌─────────────────┐
             │    Sampling     │
             └─────────────────┘
                      │
                      │ x[n]
                      ▼
             ┌─────────────────┐
             │  Quantization   │
             └─────────────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ Digital encoding│
             └─────────────────┘
                      │
                      ▼
                DIGITAL SYSTEM
```

The key engineering question is:

> **What information can safely cross the analog-to-digital boundary?**

The anti-aliasing filter controls the analog bandwidth before sampling.

The sampling frequency determines how frequently the signal is measured.

The ADC resolution determines how precisely each sample's amplitude is represented.

---

# 20. Knowledge Checklist

Before moving to the next topic, you should be able to answer all of these without memorization.

## Signals

- [ ] What is \(x(t)\)?
- [ ] What is \(x[n]\)?
- [ ] What does the index \(n\) represent?
- [ ] What is the relationship \(x[n]=x(nT_s)\)?
- [ ] What is the difference between continuous time and discrete time?

## Sampling

- [ ] What is \(T_s\)?
- [ ] What is \(f_s\)?
- [ ] How are \(T_s\) and \(f_s\) related?
- [ ] What does sampling actually do to a signal?

## Nyquist

- [ ] What is the Nyquist frequency?
- [ ] What is the Nyquist-Shannon sampling theorem?
- [ ] Why does the factor of 2 appear?
- [ ] Why is \(f_s>2f_{\max}\) required?

## Aliasing

- [ ] What is aliasing?
- [ ] Why does a high-frequency signal appear as a lower-frequency signal?
- [ ] What does frequency folding mean?
- [ ] How do you calculate an alias frequency?
- [ ] Why is aliasing irreversible after sampling?

## Frequency domain

- [ ] What happens to the spectrum after sampling?
- [ ] Why do spectral replicas occur?
- [ ] Why does overlap between replicas produce aliasing?

## Anti-aliasing

- [ ] Why is an anti-aliasing filter required?
- [ ] Why must it be analog?
- [ ] Why must it occur before the ADC?
- [ ] Why can't a digital filter undo aliasing after the ADC?
- [ ] Why aren't practical anti-aliasing filters ideal brick-wall filters?

## ADCs

- [ ] What is the difference between sampling and quantization?
- [ ] What is quantization error?
- [ ] What is encoding?
- [ ] What does a real ADC signal chain look like?
- [ ] Why can't we sample infinitely fast?
- [ ] What trade-offs result from increasing \(f_s\)?

---

# 21. Next Topics

The natural progression from here is:

```text
1. Continuous-time signals
        ↓
2. Discrete-time signals
        ↓
3. Sampling
        ↓
4. Sampling theorem
        ↓
5. Spectral replication
        ↓
6. Aliasing
        ↓
7. Anti-aliasing filters
        ↓
8. Quantization
        ↓
9. Quantization error
        ↓
10. ADC resolution / LSB
        ↓
11. ADC SNR
        ↓
12. ENOB
        ↓
13. SFDR
        ↓
14. Sample-and-hold circuits
        ↓
15. ADC architectures
        ├── Flash
        ├── SAR
        ├── Pipeline
        └── Sigma-Delta
        ↓
16. Sampling-clock jitter
        ↓
17. Practical ADC interfaces
        ↓
18. DSP fundamentals
```

---

# Summary

The core chain is:

\[
\boxed{x(t)\rightarrow x[n]\rightarrow\text{quantized samples}\rightarrow\text{digital bits}}
\]

with:

\[
\boxed{x[n]=x(nT_s)}
\]

and:

\[
\boxed{T_s=\frac{1}{f_s}}
\]

For a band-limited signal:

\[
\boxed{f_s>2f_{\max}}
\]

because sampling creates spectral replicas separated by \(f_s\). If those replicas overlap, aliasing occurs.

Aliasing can cause a high-frequency analog signal to appear as a lower-frequency digital signal:

\[
\boxed{f_{\text{alias}}=|f-kf_s|}
\]

Once aliasing occurs, the original frequency generally cannot be recovered from the sampled data.

Therefore a practical ADC system uses an analog anti-aliasing filter before sampling:

\[
\boxed{
\text{Analog signal}
\rightarrow
\text{Anti-alias filter}
\rightarrow
\text{ADC}
\rightarrow
\text{Digital processing}
}
\]

Finally, keep these concepts separate:

\[
\boxed{
\begin{array}{c}
\text{Sampling} \rightarrow \text{discrete time}\\
\text{Quantization} \rightarrow \text{discrete amplitude}\\
\text{Encoding} \rightarrow \text{digital representation}
\end{array}
}
\]

These distinctions form the foundation for understanding real ADCs, DSP systems, communication receivers, RF interfaces, and mixed-signal SoCs.

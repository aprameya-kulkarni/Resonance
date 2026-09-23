# Filters and Anti-Aliasing

## 1. Purpose

A **filter** selectively allows some frequency components of a signal to pass while attenuating others.

Filters are fundamental to analog and digital signal-processing systems.

In an ADC acquisition chain, the most important analog filter is often the **anti-aliasing filter**.

A typical system is:

```text
Analog source
     │
     ▼
Signal conditioning
     │
     ▼
Anti-aliasing filter
     │
     ▼
ADC
     │
     ▼
Digital signal
     │
     ▼
Digital filtering
```

The anti-aliasing filter is placed **before the ADC** because it must remove unwanted analog frequency content before sampling.

---

# 2. Why Filtering Is Necessary

Suppose an ADC samples at:

$$
f_s
$$

Its Nyquist frequency is:

$$
f_N=\frac{f_s}{2}
$$

Frequency components above the usable Nyquist range can alias into the sampled spectrum.

Once aliasing occurs, the original frequency information cannot generally be recovered by digital processing.

Therefore:

```text
Unwanted analog frequencies
          │
          ▼
   Anti-aliasing filter
          │
          ▼
        ADC
          │
          ▼
   Digital processing
```

The filter's job is to ensure that sufficiently little unwanted energy reaches the ADC.

---

# 3. What Is Aliasing?

Aliasing occurs when different analog frequencies produce the same discrete-time samples.

For an input frequency $f_{in}$ and sampling rate $f_s$, a useful alias relationship is:

$$
f_{alias}=|f_{in}-kf_s|
$$

where `k` is selected to place the result in the relevant Nyquist interval.

---

## 3.1 Example

Suppose:

$$
f_s=10\,kHz
$$

Then:

$$
f_N=5\,kHz
$$

An unwanted analog signal at:

$$
f_{in}=7\,kHz
$$

can appear at:

$$
|7-10|=3\,kHz
$$

Therefore:

```text
7 kHz analog signal
        │
        ▼
    ADC at 10 kS/s
        │
        ▼
3 kHz digital component
```

The ADC has no way to determine from the samples alone that the observed component originated at 7 kHz.

---

# 4. Why the Anti-Aliasing Filter Must Be Before the ADC

This is one of the most important concepts in sampled-data systems.

Consider:

```text
Analog signal
      │
      ▼
     ADC
      │
      ▼
Digital filter
```

If a 7 kHz analog signal aliases to 3 kHz during the ADC conversion, the ADC has already represented it as 3 kHz.

A digital filter can remove the resulting 3 kHz component, but it cannot determine whether that component originally came from:

```text
3 kHz
13 kHz
17 kHz
23 kHz
...
```

depending on the sampling frequency and frequency relationships.

The lost frequency identity cannot be reconstructed from the aliased samples.

Therefore:

```text
ANTI-ALIASING
──────────────
Must happen before sampling.
```

A digital filter after the ADC serves a different purpose.

---

# 5. Analog Anti-Aliasing Filter

An anti-aliasing filter is an analog filter placed immediately before, or as part of the analog front end preceding, the ADC.

Its purpose is to limit the analog input bandwidth so that unwanted frequency components are sufficiently attenuated before sampling.

Conceptually:

```text
                     ADC Nyquist
                         │
                         ▼
Amplitude
   │
   │───────────────\
   │                \
   │                 \
   │                  \________
   │
   └──────────────────────────────► Frequency
                  ↑
              transition
```

The exact response depends on the chosen filter topology.

---

# 6. Filter Frequency Response

A filter can be characterized by its frequency response:

$$
H(f)
$$

For a linear time-invariant system:

$$
Y(f)=H(f)X(f)
$$

where:

- $X(f)$ = input spectrum
- $H(f)$ = filter frequency response
- $Y(f)$ = output spectrum

The magnitude response:

$$
|H(f)|
$$

describes how strongly each frequency is passed or attenuated.

---

# 7. Passband

The **passband** is the frequency range intended to pass through the filter with acceptable attenuation or distortion.

For example:

```text
0 Hz ───────────── 20 kHz
        passband
```

For a low-pass anti-aliasing filter, the passband normally contains the highest-frequency signal component that the system wants to preserve.

---

# 8. Stopband

The **stopband** is the frequency range where strong attenuation is required.

For an anti-aliasing filter, the stopband contains frequencies that could otherwise alias into the desired digital bandwidth.

Example:

```text
0 Hz       20 kHz        24 kHz
│──────────│──────────────│──────────► f
 passband    transition     stopband
             band
```

The exact boundaries depend on the system requirements.

---

# 9. Transition Band

A real filter cannot normally change instantaneously from:

```text
0 dB attenuation
```

to:

```text
infinite attenuation
```

at one frequency.

The region between the passband edge and stopband edge is called the **transition band**.

For example:

```text
Passband edge = 20 kHz
Stopband edge = 24 kHz

Transition bandwidth:

24 kHz - 20 kHz = 4 kHz
```

A wider transition band generally makes filter implementation easier.

A narrower transition band generally requires a more selective filter.

---

# 10. Cutoff Frequency

The term **cutoff frequency** must be used carefully because its exact definition depends on the filter specification.

For a common first-order low-pass filter, the cutoff frequency is the frequency at which the magnitude falls to:

$$
\frac{1}{\sqrt{2}}
$$

of the passband voltage magnitude.

This corresponds to:

$$
-3.0103\,dB
$$

and is commonly called the **−3 dB frequency**.

For other filter specifications, the important frequencies may instead be:

- passband edge
- stopband edge
- −3 dB frequency
- −1 dB frequency
- −0.1 dB frequency
- ripple boundary
- attenuation boundary

Therefore, do not automatically equate:

```text
cutoff frequency = passband edge
```

without checking the specification.

---

# 11. Anti-Aliasing Filter Requirements

Suppose:

```text
Desired signal bandwidth = B
Sampling frequency        = fs
Nyquist frequency         = fs/2
```

The filter should:

1. Pass the desired signal with acceptable attenuation.
2. Attenuate frequencies sufficiently close to and above the Nyquist boundary.
3. Provide enough stopband attenuation for the unwanted signal environment.
4. Meet amplitude and phase requirements.
5. Work with the ADC's input impedance and drive requirements.

The fundamental constraint is:

```text
Desired signal
      │
      ▼
Must survive the filter

Unwanted out-of-band signal
      │
      ▼
Must be sufficiently attenuated before sampling
```

---

# 12. Why the Filter Cutoff Is Usually Below Nyquist

A common mistake is:

> "The Nyquist frequency is 24 kHz, so set the low-pass filter cutoff to 24 kHz."

A real filter has a transition band.

If the desired signal extends to 20 kHz and the ADC samples at 48 kS/s:

$$
f_N=24\,kHz
$$

There is only:

$$
24-20=4\,kHz
$$

available for the transition band.

The filter therefore cannot realistically be an ideal brick-wall filter at 24 kHz.

A practical design might specify:

```text
Passband:     0–20 kHz
Transition:  20–24 kHz
Stopband:     ≥24 kHz
```

with a required stopband attenuation.

The exact filter must be designed from the application's allowable signal band and unwanted-signal levels.

---

# 13. Passband Specification

A practical filter specification may be:

```text
Passband: 0–20 kHz
Maximum passband attenuation: 0.5 dB
```

This means the desired signal must remain within the specified amplitude error over the passband.

A stricter requirement might be:

```text
Passband: 0–20 kHz
Maximum attenuation: 0.1 dB
```

The tighter the passband requirement, the more constrained the filter design becomes.

---

# 14. Stopband Specification

A stopband specification might be:

```text
Stopband begins at 24 kHz
Minimum attenuation = 80 dB
```

This means unwanted signals at or above the specified stopband edge must be attenuated by at least approximately 80 dB under the filter's defined conditions.

Stopband attenuation must be considered relative to the amplitude of the unwanted analog signals.

---

# 15. Why Stopband Attenuation Matters

Suppose the desired signal is small but there is a very strong out-of-band interferer.

Example:

```text
Desired signal:       1 mV
Interferer:           1 V
Required attenuation: ?
```

A large out-of-band signal can remain significant even after filtering.

If the interferer is:

$$
1\,V
$$

and the filter provides:

$$
60\,dB
$$

attenuation, the remaining voltage magnitude is approximately:

$$
1\times10^{-60/20}
$$

which is:

```text
1 mV
```

Therefore, stopband attenuation must be selected based on:

```text
maximum expected unwanted input
+
acceptable aliased error
```

not merely by choosing a convenient filter order.

---

# 16. Anti-Aliasing Filter Design Is a System Problem

A filter cannot be designed correctly from sampling frequency alone.

You need to know:

```text
1. Desired signal bandwidth
2. Sampling frequency
3. Maximum unwanted frequency content
4. Maximum unwanted signal amplitude
5. Allowed aliasing error
6. Allowed passband attenuation
7. Allowed passband ripple
8. Required stopband attenuation
9. Phase/group-delay requirements
10. ADC input characteristics
```

---

# 17. Filter Types

Common analog filter families include:

- Butterworth
- Chebyshev Type I
- Chebyshev Type II
- Elliptic
- Bessel

They make different tradeoffs.

---

# 18. Butterworth Filter

A Butterworth filter is designed for a maximally flat magnitude response in the passband.

Characteristics:

```text
Advantages:
- Smooth passband
- No passband ripple
- Simple frequency response

Disadvantages:
- Less steep transition than some higher-selectivity designs
- Higher order may be required for stringent stopband requirements
```

Useful when a smooth magnitude response is important.

---

# 19. Chebyshev Type I

Chebyshev Type I filters allow passband ripple in exchange for a sharper transition.

Characteristics:

```text
Advantages:
- Sharper transition than Butterworth for a given order
- Useful when transition bandwidth is constrained

Disadvantages:
- Passband ripple
- More amplitude variation
```

---

# 20. Chebyshev Type II

Chebyshev Type II filters generally provide:

```text
- Flat passband
- Stopband ripple
- Sharper transition than Butterworth for comparable requirements
```

They trade stopband ripple for selectivity.

---

# 21. Elliptic Filter

Elliptic filters allow ripple in both passband and stopband.

They can achieve a very sharp transition for a given order.

Typical tradeoff:

```text
Excellent selectivity
        ↕
Passband ripple + stopband ripple
```

They can be useful when a narrow transition band is critical.

---

# 22. Bessel Filter

Bessel filters are known for favorable phase and group-delay characteristics.

They provide relatively good transient/waveform preservation but generally have a less sharp magnitude transition than filters such as elliptic filters.

Useful when:

```text
time-domain waveform shape
phase response
group delay
```

are especially important.

---

# 23. Filter Order

Filter order controls the steepness of the transition.

For a simple first-order low-pass filter, the asymptotic magnitude roll-off is approximately:

$$
-20\,dB/decade
$$

or:

$$
-6\,dB/octave
$$

For an idealized Nth-order low-pass response, the asymptotic roll-off is approximately:

$$
-20N\,dB/decade
$$

or:

$$
-6N\,dB/octave
$$

Examples:

| Order | Approx. asymptotic roll-off |
|---:|---:|
| 1 | −20 dB/decade |
| 2 | −40 dB/decade |
| 3 | −60 dB/decade |
| 4 | −80 dB/decade |
| 8 | −160 dB/decade |

The exact response near the cutoff depends on the filter family.

---

# 24. First-Order RC Low-Pass Filter

A simple low-pass filter can be constructed using:

```text
Vin ── R ──┬── Vout
           │
           C
           │
          GND
```

Its transfer function is:

$$
H(s)=\frac{1}{1+sRC}
$$

Its cutoff frequency is:

$$
f_c=\frac{1}{2\pi RC}
$$

At:

$$
f=f_c
$$

the magnitude is:

$$
|H|=\frac{1}{\sqrt{2}}
$$

which corresponds to approximately:

$$
-3.01\,dB
$$

---

# 25. Example RC Filter

Suppose:

$$
R=1\,k\Omega
$$

and:

$$
C=7.96\,nF
$$

Then:

$$
f_c\approx\frac{1}{2\pi(1000)(7.96\times10^{-9})}
$$

approximately:

```text
20 kHz
```

This is useful for intuition, but a single RC stage may not provide enough stopband attenuation for a demanding ADC application.

---

# 26. Cascaded Filter Stages

Multiple filter stages can be cascaded:

```text
Input
  │
  ▼
RC stage
  │
  ▼
RC stage
  │
  ▼
RC stage
  │
  ▼
ADC
```

The overall transfer function becomes the product of the individual transfer functions:

$$
H_{total}(s)=H_1(s)H_2(s)\cdots H_n(s)
$$

Cascading stages increases attenuation outside the passband.

However, loading between stages must be considered.

---

# 27. Active Filters

Active filters use components such as:

- operational amplifiers
- resistors
- capacitors

They can provide:

- gain
- buffering
- higher-order responses
- controlled filter characteristics

Example:

```text
Input
  │
  ▼
RC network
  │
  ▼
Op-amp
  │
  ▼
Next stage / ADC
```

The op-amp must satisfy requirements such as:

- bandwidth
- slew rate
- input noise
- output drive
- stability
- common-mode range
- output swing
- ADC drive requirements

---

# 28. Passive vs Active Filters

## Passive

Uses components such as:

- R
- L
- C

Advantages:

- simple
- no power supply required for the filter itself
- potentially low noise

Limitations:

- cannot provide active gain
- loading can alter response
- inductors can be impractical at some frequencies

## Active

Uses:

- R
- C
- op-amps or other active devices

Advantages:

- gain possible
- buffering
- easier implementation of higher-order filters

Limitations:

- requires power
- op-amp noise
- bandwidth limitations
- distortion
- output-drive limitations

---

# 29. Analog Filter vs Digital Filter

## Analog filter

Operates before digitization.

```text
Analog signal
     │
     ▼
Analog filter
     │
     ▼
ADC
```

Can prevent aliasing.

## Digital filter

Operates after digitization.

```text
ADC
 │
 ▼
Digital samples
 │
 ▼
Digital filter
```

Can:

- remove digital-band noise
- shape bandwidth
- decimate
- interpolate
- suppress known digital interference

But it cannot reverse aliasing that already occurred during sampling.

---

# 30. Anti-Aliasing vs Anti-Imaging

These are related but occur at different sides of a sampling system.

### Anti-aliasing filter

Placed before an ADC:

```text
Analog
  ↓
Anti-aliasing filter
  ↓
ADC
```

Purpose:

```text
Prevent unwanted analog frequencies from aliasing.
```

### Anti-imaging filter

Used after a DAC:

```text
DAC
 ↓
Anti-imaging reconstruction filter
 ↓
Analog output
```

Purpose:

```text
Remove spectral images generated by the DAC's sampling process.
```

Therefore:

```text
ADC → anti-aliasing
DAC → anti-imaging / reconstruction
```

---

# 31. Reconstruction Filter

A reconstruction filter is normally a low-pass filter following a DAC.

A DAC's zero-order-hold or sampling process produces spectral images around multiples of the sampling frequency.

The reconstruction filter suppresses those images and recovers the desired analog-band signal.

Conceptually:

```text
Digital samples
      │
      ▼
     DAC
      │
      ▼
Reconstruction filter
      │
      ▼
Analog signal
```

---

# 32. Filter Specifications

A practical filter specification should include at least:

```text
Passband edge
Passband ripple / attenuation
Stopband edge
Stopband attenuation
Filter type
Filter order
Sampling frequency
Load impedance
Source impedance
Input amplitude
Output amplitude
Phase/group delay requirements
```

Example:

```text
Sampling frequency:       48 kS/s
Passband edge:            20 kHz
Maximum passband loss:    0.5 dB
Stopband edge:            24 kHz
Minimum stopband loss:    80 dB
```

This is a meaningful engineering specification.

---

# 33. Why "Cutoff = Nyquist" Is Not a Complete Design

Suppose:

```text
fs = 48 kS/s
Nyquist = 24 kHz
```

and:

```text
Desired signal = 0–20 kHz
```

An ideal filter could theoretically behave as:

```text
0–20 kHz → perfect pass
>24 kHz    → perfect stop
```

with an instantaneous transition.

A real filter cannot do that.

Therefore, the practical design problem is:

```text
Preserve 0–20 kHz
       ↓
Transition from 20–24 kHz
       ↓
Strongly attenuate ≥24 kHz
```

The required filter order depends on how much attenuation is needed and how narrow the transition band is.

---

# 34. Filter Order Tradeoff

For a given filter family:

```text
Higher order
     ↓
Sharper transition
     ↓
Better rejection near Nyquist
     ↓
More components / complexity
     ↓
Potentially more sensitivity, noise, phase effects, and cost
```

Therefore, simply increasing filter order is not always the complete solution.

---

# 35. Group Delay

The phase response of a filter matters when preserving waveform shape.

Group delay is:

$$
\tau_g(\omega)=-\frac{d\phi(\omega)}{d\omega}
$$

where:

- $\phi(\omega)$ = phase response
- $\tau_g$ = group delay

A strongly frequency-dependent group delay can distort time-domain waveforms.

This is one reason Bessel-type responses may be preferred in applications where waveform shape and timing relationships matter.

---

# 36. Phase Response

Two filters can have similar magnitude responses but very different phase responses.

Therefore:

```text
Magnitude response
```

alone does not completely describe a filter.

For some applications, the important characteristics are:

```text
magnitude
phase
group delay
noise
distortion
stability
```

---

# 37. Filter Loading

A filter designed using ideal component assumptions may behave differently when connected to real circuits.

For example:

```text
Source
  │
  ▼
Filter
  │
  ▼
ADC input
```

The source impedance and ADC input impedance can interact with the filter.

Therefore:

```text
source impedance
+
filter impedance
+
ADC input impedance
```

must be considered together.

---

# 38. ADC Input Driver Considerations

Many high-speed ADCs do not behave like a simple high-impedance voltage measurement device.

The ADC input may contain:

- switched-capacitor networks
- sampling switches
- differential input structures
- internal capacitance
- dynamic input impedance

The analog driver/filter must therefore settle correctly during the acquisition interval.

Important parameters include:

- source impedance
- RC time constants
- amplifier settling
- kickback
- bandwidth
- stability
- distortion

---

# 39. Anti-Aliasing Filter and ADC Sampling Together

The correct system view is:

```text
             ANALOG DOMAIN
──────────────────────────────────────
Signal
  │
  ▼
Sensor / amplifier
  │
  ▼
Anti-aliasing filter
  │
  ▼
ADC sample-and-hold
  │
──────────────────────────────────────
             DIGITAL DOMAIN
  │
  ▼
Digital filtering
  │
  ▼
DSP / FPGA / CPU
```

The analog filter defines what frequency content is allowed to reach the sampler.

The ADC then samples that bandwidth.

---

# 40. Filter Attenuation and Aliasing Budget

Suppose an unwanted interferer has amplitude:

$$
A_{interferer}
$$

and the allowed aliased amplitude is:

$$
A_{allowed}
$$

The required attenuation is approximately:

$$
A_{required}=20\log_{10}\left(\frac{A_{interferer}}{A_{allowed}}\right)
$$

For example, if:

```text
Interferer = 1 V
Allowed aliased component = 10 µV
```

then:

$$
A_{required}
=
20\log_{10}\left(\frac{1}{10\times10^{-6}}\right)
$$

which is approximately:

```text
100 dB
```

This illustrates why filter requirements must be based on actual interference levels.

---

# 41. Filter Noise

An analog filter can introduce or pass noise.

Noise sources can include:

- resistor thermal noise
- op-amp voltage noise
- op-amp current noise
- reference noise
- power-supply noise

A filter should therefore not be evaluated only by its attenuation curve.

A practical design considers:

```text
signal preservation
+
alias rejection
+
noise
+
distortion
+
loading
+
stability
```

---

# 42. Filter Distortion

Active components can introduce nonlinear distortion.

For precision ADC systems, the filter and its driver must have sufficiently low distortion so that the analog front end does not degrade:

- THD
- SINAD
- SFDR
- ENOB

The ADC cannot distinguish distortion introduced by the driver/filter from distortion generated inside the ADC.

---

# 43. Common Filter Mistakes

## Mistake 1 — No anti-aliasing filter

```text
Analog signal → ADC
```

This can allow unwanted out-of-band energy to alias.

---

## Mistake 2 — Putting the anti-aliasing filter after the ADC

```text
Analog → ADC → analog filter
```

This does not prevent aliasing.

---

## Mistake 3 — Setting cutoff exactly at Nyquist

A real filter needs a transition band.

---

## Mistake 4 — Ignoring interferer amplitude

A weak unwanted signal and a very strong unwanted signal require different attenuation.

---

## Mistake 5 — Ignoring ADC input loading

The actual circuit may not match the ideal simulated filter.

---

## Mistake 6 — Looking only at magnitude response

Phase and group delay may matter.

---

## Mistake 7 — Assuming higher ADC resolution solves aliasing

More ADC bits do not remove aliasing.

Aliasing is primarily a sampling-bandwidth problem.

---

## Mistake 8 — Assuming oversampling automatically solves everything

Oversampling can make filtering easier and can improve some noise-related metrics, but unwanted analog content still needs appropriate attenuation before sampling.

---

# 44. Worked Example: 48 kS/s ADC

Suppose:

```text
ADC sampling rate = 48 kS/s
Desired bandwidth = 0–20 kHz
```

Then:

$$
f_N=24\,kHz
$$

A reasonable conceptual specification might be:

```text
Passband:
0–20 kHz

Transition band:
20–24 kHz

Stopband:
≥24 kHz
```

Now suppose the system requires:

```text
Maximum passband attenuation = 0.5 dB
Minimum stopband attenuation = 80 dB
```

The filter designer can use these requirements to determine:

```text
filter family
filter order
component values
topology
```

The correct order cannot be determined from the sampling frequency alone.

---

# 45. Design Workflow

A practical anti-aliasing filter design can follow this process:

## Step 1 — Define useful signal bandwidth

Determine:

$$
f_{pass}
$$

Example:

```text
0–20 kHz
```

## Step 2 — Determine ADC sampling rate

Determine:

$$
f_s
$$

Example:

```text
48 kS/s
```

## Step 3 — Calculate Nyquist frequency

$$
f_N=\frac{f_s}{2}
$$

Example:

```text
24 kHz
```

## Step 4 — Determine transition band

For example:

```text
20–24 kHz
```

## Step 5 — Determine unwanted-signal environment

Find:

```text
maximum out-of-band signal amplitude
frequency range
expected interference
```

## Step 6 — Determine allowed aliasing

Define:

```text
maximum acceptable aliased signal
```

## Step 7 — Calculate required attenuation

Use:

$$
A_{required}
=
20\log_{10}
\left(
\frac{A_{interferer}}{A_{allowed}}
\right)
$$

## Step 8 — Select filter family

Consider:

```text
Butterworth
Chebyshev
Elliptic
Bessel
```

## Step 9 — Determine filter order

Use the required:

```text
passband
stopband
transition width
attenuation
```

## Step 10 — Implement

Choose:

```text
RC
active RC
multiple feedback
Sallen-Key
LC
fully differential
ADC driver + filter
```

as appropriate.

## Step 11 — Verify

Check:

```text
frequency response
phase/group delay
noise
distortion
component tolerances
source/load interaction
ADC settling
```

---

# 46. Filter Tolerance

Real components are not exact.

A resistor marked:

```text
10 kΩ
```

may have a tolerance such as:

```text
±1%
```

A capacitor may have:

- tolerance
- temperature coefficient
- voltage dependence
- aging

Therefore, the real cutoff frequency can differ from the nominal value.

For:

$$
f_c=\frac{1}{2\pi RC}
$$

changes in `R` or `C` change the actual cutoff.

Precision applications should account for component tolerances and temperature.

---

# 47. PCB Layout

At high frequencies or high ADC performance, PCB layout becomes part of the filter/system design.

Important considerations include:

- short signal paths
- controlled return paths
- appropriate grounding
- supply decoupling
- separation of noisy digital traces
- shielding where appropriate
- differential routing where required
- minimizing parasitic capacitance and inductance

A theoretically excellent filter can perform poorly if the physical implementation is poor.

---

# 48. Anti-Aliasing Filter vs Band-Limiting

The fundamental requirement is not necessarily:

> "Build a filter with cutoff exactly at Nyquist."

The actual requirement is:

> **Limit the analog input spectrum sufficiently that frequency components capable of producing unacceptable aliases are adequately suppressed before sampling.**

This distinction is important.

---

# 49. Low-Pass Anti-Aliasing

For a baseband signal:

```text
Desired:
0 → B Hz
```

a low-pass filter is normally appropriate.

Example:

```text
Signal bandwidth = 10 kHz
ADC sampling rate = 32 kS/s

Nyquist = 16 kHz
```

The filter may be specified to:

```text
Pass 0–10 kHz
Transition 10–16 kHz
Strongly attenuate ≥16 kHz
```

---

# 50. Band-Pass Sampling

Not every ADC system is sampling a baseband signal.

For a band-pass signal, the sampling rate can sometimes be chosen so that the desired band aliases intentionally into another non-overlapping band.

This is called:

- band-pass sampling
- undersampling
- harmonic sampling

However, this requires careful spectral planning.

The general principle remains:

```text
Different spectral copies must not overlap in the desired sampled band.
```

An anti-aliasing filter for a band-pass system may therefore be a **band-pass filter**, not a low-pass filter.

---

# 51. Nyquist Zone

The analog frequency spectrum can be divided into Nyquist zones.

For sampling frequency $f_s$:

```text
1st Nyquist zone: 0 → fs/2
2nd Nyquist zone: fs/2 → fs
3rd Nyquist zone: fs → 3fs/2
...
```

Signals in higher Nyquist zones can alias into the first zone.

This is especially important in RF ADC systems.

---

# 52. Practical Mental Model

Remember:

```text
ADC
───
Converts analog measurements into digital numbers.

SAMPLING
────────
Discretizes time.

QUANTIZATION
────────────
Discretizes amplitude.

NYQUIST
───────
fs/2 is the highest frequency in the first Nyquist zone.

ALIASING
────────
Out-of-band analog energy can appear at an incorrect digital frequency.

ANTI-ALIASING FILTER
────────────────────
Suppresses that unwanted analog energy before the ADC.

PASSBAND
────────
Frequencies that must be preserved.

STOPBAND
────────
Frequencies that must be strongly attenuated.

TRANSITION BAND
───────────────
The finite region between acceptable passband and required stopband.

CUTOFF
──────
A defined characteristic frequency; commonly −3 dB for simple low-pass
filters, but the exact definition depends on the specification.
```

---

# 53. Key Equations

### Nyquist frequency

$$
f_N=\frac{f_s}{2}
$$

### Sampling period

$$
T_s=\frac{1}{f_s}
$$

### Alias relationship

$$
f_{alias}=|f_{in}-kf_s|
$$

### Low-pass RC cutoff

$$
f_c=\frac{1}{2\pi RC}
$$

### First-order asymptotic roll-off

$$
-20\,dB/decade
$$

### Nth-order asymptotic roll-off

$$
-20N\,dB/decade
$$

### Voltage attenuation

$$
A_{dB}=20\log_{10}\left(\frac{V_{out}}{V_{in}}\right)
$$

For attenuation magnitude expressed as a positive number:

$$
A_{attenuation,dB}
=
20\log_{10}
\left(
\frac{V_{in}}{V_{out}}
\right)
$$

### Required rejection

$$
A_{required}
=
20\log_{10}
\left(
\frac{A_{interferer}}{A_{allowed}}
\right)
$$

### Group delay

$$
\tau_g(\omega)
=
-\frac{d\phi(\omega)}{d\omega}
$$

---

# 54. Final System-Level Picture

The complete sampled-data chain should be understood as:

```text
                 ANALOG DOMAIN
────────────────────────────────────────────

Physical source
      │
      ▼
Sensor / analog front end
      │
      ▼
Amplification / conditioning
      │
      ▼
Anti-aliasing filter
      │
      ▼
Sample-and-hold / ADC
      │
────────────────────────────────────────────
                 DIGITAL DOMAIN
      │
      ▼
Digital samples x[n]
      │
      ▼
Digital filter
      │
      ▼
Decimation / DSP / FFT / ML / control
```

The critical boundary is the ADC.

Before the ADC:

```text
Signal is continuous in time and amplitude.
```

After the ADC:

```text
Signal is discrete in time and represented by discrete codes.
```

Therefore:

> **Any analog frequency information that aliases during sampling is fundamentally ambiguous after digitization.**

The anti-aliasing filter exists to prevent unacceptable ambiguity from being created in the first place.

---

# 55. Final Checklist

Before considering an ADC front end complete, verify:

```text
[ ] Desired signal bandwidth is known
[ ] ADC sampling rate is known
[ ] Nyquist frequency is calculated
[ ] Out-of-band signal environment is known
[ ] Maximum unwanted interferer amplitude is known
[ ] Maximum acceptable alias level is defined
[ ] Passband edge is defined
[ ] Passband attenuation/ripple is defined
[ ] Stopband edge is defined
[ ] Stopband attenuation is defined
[ ] Transition bandwidth is understood
[ ] Filter family is selected
[ ] Filter order is justified
[ ] Source impedance is considered
[ ] ADC input impedance is considered
[ ] Filter noise is considered
[ ] Filter distortion is considered
[ ] Component tolerance is considered
[ ] Temperature effects are considered
[ ] Phase/group delay requirements are considered
[ ] PCB parasitics are considered
[ ] Final frequency response is simulated/measured
[ ] ADC performance is verified with the complete front end
```

---

# 56. Core Takeaway

The most important relationship in an ADC system is:

```text
Sampling rate
      ↓
Nyquist frequency
      ↓
Allowed analog bandwidth
      ↓
Anti-aliasing filter requirements
      ↓
ADC conversion
      ↓
Digital processing
```

A robust design does not simply ask:

> "What is my ADC sampling rate?"

It asks:

> "What analog information do I need to preserve, what unwanted analog energy exists outside that band, how much of that energy can be allowed to alias, and can the analog filter provide the required attenuation before sampling?"

That is the engineering problem behind anti-aliasing.

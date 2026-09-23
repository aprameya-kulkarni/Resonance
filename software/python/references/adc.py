import numpy as np


def quantize(signal, bits, vmin=-1.0, vmax=1.0):
    """
    Quantize an analog signal into a signed ADC code.

    Parameters
    ----------
    signal : np.ndarray
        Input samples.
    bits : int
        ADC resolution.
    vmin : float
        Minimum input voltage.
    vmax : float
        Maximum input voltage.

    Returns
    -------
    codes : np.ndarray
        Quantized ADC codes.
    reconstructed : np.ndarray
        Reconstructed voltage after quantization.
    """

    levels = 2**bits

    # Prevent values outside ADC range
    clipped = np.clip(signal, vmin, vmax)

    # Normalize to [0, 1]
    normalized = (clipped - vmin) / (vmax - vmin)

    # Convert to ADC code
    codes = np.round(normalized * (levels - 1)).astype(int)

    # Reconstruct voltage from ADC code
    reconstructed = (
        codes / (levels - 1)
    ) * (vmax - vmin) + vmin

    return codes, reconstructed
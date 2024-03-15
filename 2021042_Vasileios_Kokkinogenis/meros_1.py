import numpy as np
import matplotlib.pyplot as plt



def f(M, Pb):
    SNRb = -1/3 * np.log(Pb * M * np.log2(M) / (2 * (M - 1))) * (M**2 - 1) / np.log2(M)
    return SNRb


# x = -2
Pb = 10**-4
m_values = np.arange(1, 11)  # M = 2^m for 1<=m<=10
M_values = 2**m_values

# Calculate SNRb for each M
SNRb_values = [f(M, Pb) for M in M_values]

# Convert SNRb to dB
SNRb_dB_values = 10 * np.log10(SNRb_values)
print (M_values)

# gia epalitheush
# SNRb_linear_values = 10 ** (SNRb_dB_values / 10)
# print(SNRb_linear_values)

# Plot
plt.plot(M_values, SNRb_dB_values, marker='o', linestyle='-', color='b')
plt.xlabel('M')
plt.ylabel('SNRb (dB)')
plt.title('SNRb as a function of M')
plt.grid(True)
plt.show()
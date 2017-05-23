import math
signal = 4000
noise = 4330
SNRlinear= signal // noise
SNR = 10*math.log10(SNRlinear)
print(SNR)

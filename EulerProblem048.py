import time

s = 0
i = 1


time1 = time.time()
while i <=1000:
    s += i**i
    i += 1

time2 = time.time()
delta_t = time2-time1
print('answer:', s)
print('Time required:', delta_t)


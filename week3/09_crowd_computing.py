import matplotlib.pyplot as plt
import statistics

estimates = [ 320, 340, 355, 360, 370, 380, 390, 400, 410, 420, 430, 440, 
             450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 
             570, 580, 590, 600, 610, 620, 250, 275, 290, 700, 750, 800 ]
y = []

for i in range(len(estimates)):
    y.append(5)  
plt.plot(estimates, y, 'r--')

estimates.sort()

tv = int(0.1 * len(estimates))
trimmed_estimates = estimates[tv : len(estimates) - tv]

y_trim = []

for i in range(len(trimmed_estimates)):
    y_trim.append(5)
plt.plot(trimmed_estimates, y_trim, 'r--')

plt.plot(375, 5, 'g^')

mean_value = statistics.mean(trimmed_estimates)
plt.plot(mean_value, 5, 'ro')

median_value = statistics.median(trimmed_estimates)
plt.plot(median_value, 5, 'bs')

plt.show()
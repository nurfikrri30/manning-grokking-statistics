import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from math import sqrt

mu = 98.2  #A
sigma = 0.73  #B
n_values = [31, 60, 100]  #C
x_target = 98.0  #D

fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharey=True)  #E

for i, n in enumerate(n_values):  #F
    mu_sample_means = mu  #G
    sigma_sample_means = sigma / sqrt(n)  #H

    x = np.linspace(mu - 4*sigma_sample_means, mu + 4*sigma_sample_means, 1000)  #I
    y = norm.pdf(x, mu_sample_means, sigma_sample_means)  #J

    prob = norm.cdf(x_target, mu_sample_means, sigma_sample_means)  #K

    axes[i].plot(x, y, label='Sampling Distribution')  #L

    x_fill = np.linspace(mu - 4*sigma_sample_means, x_target, 100)  #M
    y_fill = norm.pdf(x_fill, mu_sample_means, sigma_sample_means)  #N
    axes[i].fill_between(x_fill, y_fill, alpha=0.3, color='red', label=f'P(mean < {x_target}) = {prob:.4f}')  #O

    axes[i].set_title(f'n = {n}')  #P
    axes[i].set_xlabel('Sample Mean')  #Q
    if i == 0:  #R
        axes[i].set_ylabel('Density')  #S
    axes[i].legend()  #T
    axes[i].grid(True, alpha=0.3)  #U

plt.tight_layout()  #V

import os
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.svg')}", transparent=True)
plt.savefig(f"assets/{os.path.basename(__file__).replace('.py', '.png')}", transparent=True)

plt.show()  #W

#A Set population mean to 98.2
#B Set population standard deviation to 0.73
#C Define list of sample sizes: 31, 60, and 100
#D Set target value for probability calculation to 98.0
#E Create figure with three subplots, 15x5 size, sharing y-axis
#F Iterate over sample sizes with index
#G Set mean of sample means to population mean
#H Calculate standard deviation of sample means
#I Generate 1000 x values from mean - 4*std to mean + 4*std
#J Compute normal PDF for x values
#K Calculate probability of sample mean less than target
#L Plot sampling distribution on subplot
#M Generate 100 x values for shading from mean - 4*std to target
#N Compute PDF for shading x values
#O Shade area under curve for sample mean less than target with red fill and 0.3 transparency
#P Set subplot title with sample size
#Q Label x-axis of subplot
#R Check if first subplot
#S Label y-axis for first subplot only
#T Add legend to subplot
#U Add grid to subplot with 0.3 opacity
#V Adjust layout to prevent overlap
#W Display the plot

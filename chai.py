import numpy as np
from scipy.stats import lognorm, gumbel_r
import matplotlib.pyplot as plt
s_lognorm = 0.5 
scale_lognorm = np.exp(1)


loc_gumbel = 2.0
scale_gumbel = 1.0


x = np.linspace(0, 10, 500)

pdf_lognorm = lognorm.pdf(x, s=s_lognorm, scale=scale_lognorm)


pdf_gumbel = gumbel_r.pdf(x, loc=loc_gumbel, scale=scale_gumbel)

plt.figure(figsize=(10, 6))
plt.plot(x, pdf_lognorm, label=f'Log-normal (s={s_lognorm}, scale={scale_lognorm:.2f})', color='blue')
plt.plot(x, pdf_gumbel, label=f'Gumbel (loc={loc_gumbel}, scale={scale_gumbel})', color='red', linestyle='--')

plt.title('Comparison of Log-normal and Gumbel Distributions')
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)
plt.ylim(bottom=0)
plt.xlim(left=0)

plt.show()

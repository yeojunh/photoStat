import scipy.stats as ss
import numpy as np

def z_test(p, x, sigma, n, alpha, two_tailed): 
    sd = sigma/np.sqrt(n)
    z = (x-p)/sd
    
    p = ss.norm.sf(abs(z))

    if (two_tailed == True):
        p *= 2
    
    if (p < alpha): 
        return "p-value of " + str(p) + " is smaller than alpha = " + str(alpha) + "\nReject H0\n"
    else: 
        return "p-value of " + str(p) + " is greater than alpha = " + str(alpha) + "\nFail to reject H0\n"

print(z_test(8.5, 9.26, 1.20, 41, 0.05, True))
# values are a bit off from online sources, but have the same conclusions 
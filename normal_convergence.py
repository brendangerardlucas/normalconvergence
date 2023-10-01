import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import subplots

n = 250 #number of data points

sd = np.zeros(shape=n) #the standard deviation plotted
m = np.zeros(shape=n) #the mean to be plotted
v = np.zeros(shape=n) #the variance to be plotted
x = np.zeros(shape=n) #index of the distribution to be plotted
esd = np.zeros(shape=n) #square error in the standard deviation
em = np.zeros(shape=n) #square error in the mean
ev = np.zeros(shape=n) #square error in the variance

for i in range (0, n):
    dist = np.random.standard_normal(i) #make the data points
    sd[i]= np.std(dist) #add the standard deviation for this n to the plot
    m[i] = np.mean(dist) #add the mean for this n to the plot
    v[i] = np.var(dist) #add the variance for this n to the plot
    x[i] = i #add the index to the plot
    esd[i] = (sd[i] - 1)**2 #error in the standard deviation
    em[i] = (m[i])**2 #square error in the mean
    ev[i] = (v[i]-1)**2 #square error in the variance

fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))

for i, (title, label, data, error) in enumerate(zip(['Mean', 'Standard deviation', 'Variance'],['$\mu$', '$\sigma$', '$V$'], [m, v, sd], [em, ev, esd])):
    #Create a primary y-axis and plot the data
    axes[i].set_title(title)
    axes[i].set_ylabel(label + ' (' + title + ')' )
    line1, = axes[i].plot(x, data, 'bo', label=label)
    axes[i].set_xlabel('$N$ (Sample size)')
    

    # Create a secondary y-axis and plot the error data
    ax2 = axes[i].twinx()
    line2, = ax2.plot(x, error, 'r-', label='Err$^2$ ' + label)
    ax2.set_ylabel('Err$^2$' + label, labelpad=10)

    #Create a readable legend
    handles = [line1, line2]
    labels = [h.get_label() for h in handles]
    axes[i].legend(handles, labels, loc='upper right')

fig.suptitle('As sample size in a standard normal distribution increases, statistical values converge and error reduces to a limit of zero. (Err$^2$ = square error)')
plt.show()
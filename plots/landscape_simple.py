import numpy as np
from matplotlib import pyplot as plt
plt.rc('text', usetex=True)
plt.rc('font', family='serif')


# Collect data
x = np.linspace(0.2, 6, num=1000)
y = -0.4*x + 3.5

# Build figure
fig, ax = plt.subplots(figsize=[4, 3])

# Plot data
ax.plot(x, y, color='black', linewidth=2)
ax.plot(x, y, color='green', alpha=0.5, linewidth=5)
ax.fill_between(x, y, 4.2, facecolor='black', alpha=.05)

# Add texts
ax.text(.5, 2.7, '$w_i > 0$ \n $y=1$', size=8, ha="left", va="center",)
ax.text(5.6, 3.8, r'$\frac{\partial L}{\partial x_i} = -y w_i$', size=8, ha="right", va="top",
        bbox=dict(facecolor='white'))

# Reduce number of ticks
ax.set_xticks([3])
ax.set_xticklabels([r'$x_i$'])
ax.set_yticks([])

# Adjust limits to hing plot standard
ax.set_xlim(-.2, 6.2)
ax.set_ylim(-.2, 4.2)

# Plot vertical line
ymin, ymax = ax.get_ylim()
ax.axvline(3, ymin, ymax, linestyle='--', linewidth=.5, dashes=[10, 4], color='black')

# Set labels
ax.set_xlabel('$x$')
ax.set_ylabel('$L$', rotation=0)

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Thicker axes
ax.spines['left'].set_linewidth(0.3)
ax.spines['bottom'].set_linewidth(0.3)

# Move left y-axis and bottom x-axis to centre, passing through (0,0)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

# Adjust positions of ax labels
ax.xaxis.set_label_coords(1.02, .02)
ax.yaxis.set_label_coords(.05, 1.02)

# Add head arrows to axes
xmin, xmax = ax.get_xlim()
ymin, ymax = ax.get_ylim()
ax.arrow(0, 0, 0, ymax-.1, head_width=.05, head_length=.1, linewidth=.1, color='black')
ax.arrow(0, 0, xmax-.1, 0, head_width=.05, head_length=.1, linewidth=.1, color='black')

# Make equal aspect
ax.set_aspect('equal')
plt.tight_layout()
name, ext = __file__.split('.')
plt.savefig(f'{name}.png', dpi=300)

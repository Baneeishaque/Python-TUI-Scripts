import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Set high DPI for crisp display
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300

# Data from the chart
LABELS = ['March', 'April', 'May', 'June', 'July', 'August (Proj.)']
DATA = [0.8, 1.0, 1.2, 1.5, 2.1, 3.0]
x_pos = np.arange(len(LABELS))

# Colors from the energeticPlayfulPalette
primary_color = '#4F46E5'
primary_color_rgba = (79/255, 70/255, 229/255, 0.1) # Converted for fill_between
text_color = '#1E293B'
neutral_color = '#6B7280'
grid_color = '#E2E8F0'

# Create the plot with larger figure size for better quality on large screens
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(16, 10))  # Increased size for large screens

# Plot the line with tension effect (using a spline for a smooth curve)
x_new = np.linspace(x_pos.min(), x_pos.max(), 300)
spl = make_interp_spline(x_pos, data, k=3)  # k=3 for cubic spline
data_smooth = spl(x_new)

ax.plot(x_new, data_smooth, color=primary_color, linewidth=3)  # Increased line width

# Add the fill color underneath the line
ax.fill_between(x_new, data_smooth, color=primary_color_rgba)

# Add the original data points with larger markers
ax.plot(x_pos, data, 'o', color=primary_color, markersize=12, 
        markerfacecolor=primary_color, markeredgecolor='white', markeredgewidth=2)

# Set titles and labels with larger fonts
ax.set_title("Monthly Sales Revenue Growth", fontsize=28, weight='bold', 
             color=text_color, pad=30)
ax.set_ylabel("Revenue in INR Lakhs", fontsize=18, color=neutral_color)
ax.set_xticks(x_pos)
ax.set_xticklabels(labels, fontsize=16, color='black')

# Increase tick label sizes
ax.tick_params(axis='y', labelsize=14, colors='black')

# Customize grid and spines
ax.grid(color=grid_color, linewidth=1)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color(grid_color)
ax.spines['bottom'].set_color(grid_color)

# Set y-axis to start at zero
ax.set_ylim(0)

# Add data labels on top of the points with larger font
for i, val in enumerate(data):
    ax.text(i, val + 0.1, f'{val:.1f}L', ha='center', va='bottom', 
            fontsize=14, color=primary_color, weight='bold')

plt.tight_layout()

# Save with maximum quality settings
save_kwargs = {
    'dpi': 300,
    'bbox_inches': 'tight',
    'facecolor': 'white',
    'edgecolor': 'none',
    'format': 'png',
    'pad_inches': 0.2
}
plt.savefig('revenue_growth_chart_hq.png', **save_kwargs)

# Also save as PDF for vector graphics (scalable to any size without quality loss)
save_kwargs = {
    'bbox_inches': 'tight',
    'facecolor': 'white',
    'edgecolor': 'none',
    'format': 'pdf',
    'pad_inches': 0.2
}
plt.savefig('revenue_growth_chart_vector.pdf', **save_kwargs)

# Save as SVG for web use (also vector format)
save_kwargs = {
    'bbox_inches': 'tight',
    'facecolor': 'white',
    'edgecolor': 'none',
    'format': 'svg',
    'pad_inches': 0.2
}
plt.savefig('revenue_growth_chart_vector.svg', **save_kwargs)

plt.show()
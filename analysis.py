import pandas as pd
import matplotlib.pyplot as plt

# --- Data Ingestion ---
# Read the hardness data from the CSV file into a pandas DataFrame.
# The 'data/' folder is in the same directory as this script.
data_path = 'data/hardness_data.csv'
df = pd.read_csv(data_path)

# --- Data Visualization ---
# Set the figure size for a nice aspect ratio.
plt.figure(figsize=(10, 6))

# Create a bar plot.
# 'Sample Treatment' is on the x-axis, 'Hardness (HRC)' is on the y-axis.
bars = plt.bar(df['Sample Treatment'], df['Hardness (HRC)'], color='steelblue')

# Add titles and labels for clarity.
plt.title('Hardness Comparison of Heat-Treated Steel Samples', fontsize=16)
plt.xlabel('Heat Treatment Process', fontsize=12)
plt.ylabel('Average Hardness (Rockwell C-Scale)', fontsize=12)
plt.ylim(0, 60) # Set y-axis limit to give some space above the tallest bar.

# Add the exact hardness value on top of each bar.
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 1, int(yval), ha='center', va='bottom')

# Ensure the plot layout is tight and clean.
plt.tight_layout()

# --- Output ---
# Save the generated plot as a PNG image file in the root directory.
# This image is then displayed in the README.md.
output_path = 'hardness_comparison_chart.png'
plt.savefig(output_path)

print(f"Chart successfully generated and saved to '{output_path}'")
import nbformat
import json

with open("Group_notebook.ipynb", "r") as f:
    nb = nbformat.read(f, as_version=4)

# We want to find the cell that contains: "fig, axes = plt.subplots(1, 2, figsize=(13, 4))"
# and the cell that contains "corr_matrix = "

new_eda_code_1 = """\
import seaborn as sns
import matplotlib.pyplot as plt

# Set professional aesthetics
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams.update({
    'font.size': 12,
    'axes.titlesize': 14,
    'axes.labelsize': 12,
    'figure.figsize': (14, 6)
})

# 1. Target Distribution & Hourly Trend
fig, axes = plt.subplots(1, 2, figsize=(15, 5))

# Distribution with KDE
sns.histplot(df[target_col].dropna(), bins=60, kde=True, color="steelblue", ax=axes[0])
axes[0].set_title("Distribution of Solar Radiation (W/m²)", pad=15)
axes[0].set_xlabel("Solar Radiation")
axes[0].set_ylabel("Frequency")

# Hourly Trend
df["_ts"] = pd.to_datetime(df["timestamp"], errors="coerce")
df["_hour"] = df["_ts"].dt.hour
df["_month"] = df["_ts"].dt.month

hourly_stats = df.groupby("_hour")[target_col].agg(['mean', 'std']).reset_index()
axes[1].plot(hourly_stats['_hour'], hourly_stats['mean'], marker="o", color="darkorange", linewidth=2, label="Mean")
axes[1].fill_between(hourly_stats['_hour'], 
                     hourly_stats['mean'] - hourly_stats['std'],
                     hourly_stats['mean'] + hourly_stats['std'],
                     color="darkorange", alpha=0.2, label="±1 Std Dev")

axes[1].set_title("Average Solar Radiation by Hour of Day", pad=15)
axes[1].set_xlabel("Hour of Day")
axes[1].set_ylabel("Mean Radiation (W/m²)")
axes[1].set_xticks(range(0, 24, 2))
axes[1].legend()

sns.despine()
plt.tight_layout()
plt.show()

# 2. Monthly Trend (Boxplot)
plt.figure(figsize=(10, 5))
sns.boxplot(x="_month", y=target_col, data=df, palette="viridis")
plt.title("Solar Radiation Distribution by Month", pad=15)
plt.xlabel("Month")
plt.ylabel("Solar Radiation (W/m²)")
sns.despine()
plt.tight_layout()
plt.show()
"""

new_eda_code_2 = """\
# Correlation Analysis
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
numeric_cols = [c for c in numeric_cols if c not in ["ID", "timestamp", "_ts", "_hour", "_month"]]

corr_matrix = df[numeric_cols].corr()

plt.figure(figsize=(10, 8))
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
sns.heatmap(corr_matrix, mask=mask, annot=True, fmt=".2f", cmap="coolwarm", 
            center=0, square=True, linewidths=.5, cbar_kws={"shrink": .8})
plt.title("Feature Correlation Heatmap", pad=20, size=16)
plt.tight_layout()
plt.show()

# Scatterplots of top features vs Target
plt.figure(figsize=(15, 5))

plt.subplot(1, 2, 1)
sns.scatterplot(x='temperature (degrees Celsius)', y=target_col, data=df, alpha=0.3, color='crimson')
plt.title("Temperature vs Solar Radiation", pad=10)

plt.subplot(1, 2, 2)
sns.scatterplot(x='relativehumidity (-)', y=target_col, data=df, alpha=0.3, color='teal')
plt.title("Relative Humidity vs Solar Radiation", pad=10)

sns.despine()
plt.tight_layout()
plt.show()

# Clean up temporary columns
df.drop(columns=["_ts", "_hour", "_month"], inplace=True)
"""

for cell in nb.cells:
    if cell.cell_type == "code":
        if "fig, axes = plt.subplots(1, 2, figsize=(13, 4))" in cell.source:
            cell.source = new_eda_code_1
            # Clear outputs since we changed code
            cell.outputs = []
            cell.execution_count = None
        elif "corr_matrix =" in cell.source:
            cell.source = new_eda_code_2
            cell.outputs = []
            cell.execution_count = None

with open("Group_notebook_updated.ipynb", "w") as f:
    nbformat.write(nb, f)

print("EDA cells updated via python script.")

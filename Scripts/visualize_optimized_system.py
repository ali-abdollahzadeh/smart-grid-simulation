import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from config import PROCESSED_DATA_DIR, plot_dir

# Load the optimized system data
optimized_system_df = pd.read_csv(f"{PROCESSED_DATA_DIR}/Optimized_System.csv")

# Set the plot style
sns.set_theme(style="darkgrid")

# 🗺️ Function to plot a heatmap of payback period
def plot_payback_period_heatmap():
    pivot_table = optimized_system_df.pivot_table(values="Payback_Period_Years", index="Battery_Size_kWh", columns="PV_Size_kW")

    plt.figure(figsize=(12, 8))
    sns.heatmap(pivot_table, cmap="YlGnBu", annot=True, fmt=".2f", cbar_kws={'label': 'Years'})
    plt.title("Payback Period Heatmap (Years)")
    plt.xlabel("PV System Size (kW)")
    plt.ylabel("Battery Storage Size (kWh)")
    plt.tight_layout()
    plt.savefig(f"{plot_dir}/payback_period_heatmap.png")
    plt.close()
    print("Saved: payback_period_heatmap.png")

# 🗺️ Function to plot a heatmap of ROI (%)
def plot_roi_heatmap():
    pivot_table = optimized_system_df.pivot_table(values="ROI_Percent", index="Battery_Size_kWh", columns="PV_Size_kW")

    plt.figure(figsize=(12, 8))
    sns.heatmap(pivot_table, cmap="RdYlGn", annot=True, fmt=".2f", cbar_kws={'label': 'ROI (%)'})
    plt.title("ROI Heatmap (%)")
    plt.xlabel("PV System Size (kW)")
    plt.ylabel("Battery Storage Size (kWh)")
    plt.tight_layout()
    plt.savefig(f"{plot_dir}/roi_heatmap.png")
    plt.close()
    print("Saved: roi_heatmap.png")

# Main function to run the visualizations
def main():
    plot_payback_period_heatmap()
    plot_roi_heatmap()

if __name__ == "__main__":
    main()

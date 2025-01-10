import pandas as pd
import numpy as np
from config import PROCESSED_SOLAR_FILE, PROCESSED_DEMAND_FILE, PROCESSED_DATA_DIR

# Output file path
OUTPUT_FILE = f"{PROCESSED_DATA_DIR}/Optimal_PV_System.csv"

def optimize_pv_system():
    # Load demand and solar generation data
    demand_df = pd.read_csv(PROCESSED_DEMAND_FILE, parse_dates=['Datetime'])
    solar_df = pd.read_csv(PROCESSED_SOLAR_FILE, parse_dates=['Datetime'])

    # Calculate average daily demand
    daily_demand = demand_df.resample('D', on='Datetime')['Consumption_kWh'].sum()
    avg_daily_demand = daily_demand.mean()

    # Calculate average daily solar generation
    daily_generation = solar_df.resample('D', on='Datetime')['Generation_kWh'].sum()
    avg_daily_generation = daily_generation.mean()

    # Calculate the optimal PV system size (kW) to meet average daily demand
    optimal_pv_size = avg_daily_demand / avg_daily_generation

    # Account for seasonal variations (using monthly data)
    monthly_demand = demand_df.resample('ME', on='Datetime')['Consumption_kWh'].sum()
    monthly_generation = solar_df.resample('ME', on='Datetime')['Generation_kWh'].sum()
    monthly_ratio = monthly_demand / monthly_generation

    # Save results to CSV
    result_df = pd.DataFrame({
        'Month': monthly_ratio.index.strftime('%Y-%m'),
        'Demand_kWh': monthly_demand.values,
        'Generation_kWh': monthly_generation.values,
        'Ratio': monthly_ratio.values
    })

    result_df.to_csv(OUTPUT_FILE, index=False)
    print(f"Optimal PV system size calculated and saved to {OUTPUT_FILE}")
    print(f"Recommended PV system size: {optimal_pv_size:.2f} kW")

if __name__ == "__main__":
    optimize_pv_system()
